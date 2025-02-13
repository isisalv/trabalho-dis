from flask import Flask
from celery import Celery, Task
from pathlib import Path

_root = Path(__file__).parent.resolve().joinpath('celery')
_backend_folder = _root.joinpath('results')
_backend_folder.mkdir(exist_ok=True, parents=True)

def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.Task = FlaskTask
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(
        CELERY=dict(
            broker_url='filesystem://',
            broker_transport_options={
                'data_folder_in': _root.joinpath('in'),
                'data_folder_out': _root.joinpath('in'),
                'processed_folder': _root.joinpath('processed')
            },
            result_backend = 'file://{}'.format(str(_backend_folder)).replace('\\', '/'),
            task_serializer = 'json',
            persist_results = True,
            result_serializer = 'json',
            accept_content = ['json'],
            imports = ('algo'),
            task_always_eager = False,
            # worker_max_tasks_per_child = 1,
            # broker_pool_limit = 1
        ),
    )
    app.config.from_prefixed_env()
    celery_init_app(app)
    return app