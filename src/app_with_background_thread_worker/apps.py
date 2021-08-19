import logging
from django.apps import AppConfig

from app_with_background_thread_worker.jobs import ExampleJob

logger = logging.getLogger(__name__)


class AppWithBackgroundThreadWorkerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_with_background_thread_worker'

    def ready(self):
        logging.debug('Initiate thread jobs...')
        ExampleJob().run()
