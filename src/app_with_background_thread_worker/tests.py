from django.test import TestCase
from app_with_background_thread_worker.jobs import ExampleJob


class FakeExampleJob(ExampleJob):
    def run(self):
        pass


class WebhookDeliveryJobTests(TestCase):
    def test_example_job_execution(self):
        FakeExampleJob().execute()
