import logging
import time
from datetime import datetime

from celery import shared_task

from celery.signals import setup_logging


@setup_logging.connect
def void(*args, **kwargs):
    pass


@shared_task()
def time_consuming_operation():
    time.sleep(12)
    time_consuming_operation_time = datetime.now()
    logging.info(f"The time consuming operation is executed at {time_consuming_operation_time}")


'''
python -m celery -A em_asd worker -l info
'''
