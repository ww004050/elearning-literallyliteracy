import time

from celery import shared_task
from celery.utils.log import get_task_logger

from django.core import management

logger = get_task_logger(__name__)


@shared_task
def task_example(task_type):
    time.sleep(int(task_type) * 10)
    return True


@task()
def user_email_reminder():
    try:
        """
        sends an email to users who have not logged in for 2 weeks
        """
        management.call_command("enroll_reminder", "20", verbosity=0)
    except:
        print("error")
