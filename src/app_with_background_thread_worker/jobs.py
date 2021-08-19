from datetime import timedelta

from django.db import transaction
from django.utils import timezone
from django.conf import settings

from utils.job import DaemonThreadJob


class ExampleJob(DaemonThreadJob):
    """Simple job example."""

    def execute(self,  *args, **kwargs):
        """Your execution finction."""
        import app_with_background_thread_worker.models  # e.g. of model importing place

        self.logger.info(f'{self.__class__.__name__} starts executing...')
        return
