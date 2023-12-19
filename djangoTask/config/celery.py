from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoTask.config.settings")
app = Celery("config")
app.config_from_object("django.conf:settings", namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "buy_cars_from_supplier_to_car_dealer": {
        "task": "djangoTask.src.apps.CarDealer.tasks.buy_cars_from_supplier_to_car_dealer",
        "schedule": crontab(minute="*/2"),
    },
    "buy_cars_from_car_dealer_to_client": {
        "task": "djangoTask.src.apps.CarDealer.tasks.buy_cars_from_car_dealer_to_client",
        "schedule": crontab(minute="*/3"),
    },
}
