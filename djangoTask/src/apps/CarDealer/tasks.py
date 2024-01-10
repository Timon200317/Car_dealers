import time
import logging
from celery import shared_task

from djangoTask.src.apps.CarDealer.models import CarDealer
from djangoTask.src.apps.Client.models import Client
from djangoTask.src.core.tools.functions import find_cars_by_specification, get_cars_to_buy, buy_car_from_supplier, \
    find_best_order_in_car_dealer, buy_car_from_car_dealer, get_car_best_price
logger = logging.getLogger(__name__)


@shared_task
def buy_cars_from_supplier_to_car_dealer():
    for car_dealer in CarDealer.objects.filter(is_active=True).exclude(
        specification=None
    ):
        logger.info(f"Car_dealer_car_task {str(car_dealer)}")
        if car_dealer.balance <= 0:
            continue

        cars_to_buy = get_cars_to_buy(car_dealer)
        if not cars_to_buy:
            continue
        best_price = get_car_best_price(cars_to_buy)
        logger.info(f"Best price: {str(best_price)}")
        for car in best_price:
            logger.info(f"Car: {str(car)}")
            if car_dealer.balance >= best_price[car][0]:
                logger.info(f"car_dealer.balance: {str(best_price)}")
                buy_car_from_supplier(
                    car=car,
                    car_dealer=car_dealer,
                    supplier=best_price[car][1],
                    price=best_price[car][0],
                )


@shared_task
def buy_cars_from_car_dealer_to_client():
    for client in Client.objects.filter(is_active=True).exclude(specification=None):
        if client.balance <= 0:
            continue

        for specification in client.specification:
            cars = find_cars_by_specification(specification)
            max_price = specification["max_price"]
            if not cars:
                continue
            best_price = find_best_order_in_car_dealer(cars, max_price)

            for car in best_price:
                if client.balance >= best_price[car][0]:
                    buy_car_from_car_dealer(
                        car=car,
                        client=client,
                        car_dealer=best_price[car][1],
                        price=best_price[car][0],
                    )

