from abc import ABC, abstractmethod
from datetime import timedelta
import logging
import threading
import time

from django.utils import timezone
from django.conf import settings


class DaemonThreadJob(ABC):
    """ABC class for a job to be initiated in app.ready() by a run() method.
    The job executes after each interval that you specify on initialization.

    Warning:
    - To use django app models inside execute() of the class
    you probably need to import the models locally inside execute() method.
    """
    _HEARTBEAT_TIMEDELTA = timedelta(seconds=600)

    def __init__(self, interval: int = settings.THREAD_JOB_DEFAULT_INTERVAL, *args, **kwargs):
        self.interval = interval
        self.args = args
        self.kwargs = kwargs
        self.logger = logging.getLogger(self.__class__.__name__)
        self.last_heartbeat = None

    def _job(self):
        while True:
            try:
                self.execute(*self.args, **self.kwargs)
            except Exception as e:
                self.logger.exception(e)
            finally:
                self._log_heartbeat()
                time.sleep(self.interval)

    def run(self):
        threading.Thread(
            name=self.__class__.__name__,
            target=self._job,
            daemon=True
        ).start()

    def _log_heartbeat(self):
        now = timezone.now()
        if not self.last_heartbeat:
            self.last_heartbeat = now
            return

        if self.last_heartbeat < now - self._HEARTBEAT_TIMEDELTA:
            self.logger.debug(f'heartbeat for the thread job: {self.__class__.__name__}')
            self.last_heartbeat = now

    @abstractmethod
    def execute(self,  *args, **kwargs):
        pass
