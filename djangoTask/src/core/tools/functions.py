import logging

from django.db.models import Q, Count

from djangoTask.src.apps.Car.models import CarDealerCar, Car
from djangoTask.src.apps.History.models import SupplierSalesHistory, SalesDealerHistory
from djangoTask.src.apps.Supplier.models import SupplierCars

# Настройка логгера
logger = logging.getLogger(__name__)


def buy_car_from_supplier(car, car_dealer, supplier,price, count=1):
    try:
        car_dealer_car_price = (
            CarDealerCar.objects.filter(car_dealer__id=car_dealer.id)
            .select_related("car")
            .get(car__id=car.id)
        )
        logger.info(f"Car_dealer_car_try {str(car_dealer_car_price)}")
    except CarDealerCar.DoesNotExist:
        car_dealer_car_price = None
    if car_dealer_car_price:
        car_dealer_car_price.count += 1
        car_dealer_car_price.save()
    else:
        car_dealer_car_price = CarDealerCar.objects.create(
            car=car,
            car_dealer=car_dealer,
            price=price,
            count=1,
        )
        logger.info(f"Car_dealer_car {str(car_dealer_car_price)}")
        car_dealer_car_price.save()
    SupplierSalesHistory.objects.create(
        car=car,
        supplier=supplier,
        car_dealer=car_dealer,
        price=price,
        count=count
    )
    car_dealer.balance -= price
    car_dealer.save()
    return


def get_car_best_price(cars):
    best_price = {}

    for car in cars:
        logger.info(f"Car_in_get_car_best_price {str(car)}")
        car_price = SupplierCars.objects.filter(car=car).order_by("price_with_discount")
        logger.info(f"Car_in_get_car_best_price(car_price) {str(car_price)}")
        print(list(car_price.values()))
        if not car_price:
            continue
        else:
            price = car_price[0].price_with_discount
            supplier = car_price[0].supplier
            best_price[car] = [price, supplier]
            logger.info(f"Car_in_get_car_best_price(car_price[0].provider) {str(best_price[car])}")
    logger.info(f"Final_best_price {str(best_price)}")
    return best_price


def get_cars_to_buy(car_dealer):
    cars_to_buy = []
    for specification in car_dealer.specification:
        cars = find_cars_by_specification(specification)
        cars_sold = (
            cars.filter(salesdealerhistory__car_dealer=car_dealer)
            .annotate(total_sales=Count("salesdealerhistory"))
            .order_by("-total_sales")
        )
        cars_not_sold = cars.exclude(id__in=cars_sold.values_list("id", flat=True))
        logger.info(f"Cars_not_sold {str(cars_not_sold)}")
        cars_to_buy.extend(cars_sold)
        cars_to_buy.extend(cars_not_sold)
        logger.info(f"Cars_extend {str(cars_not_sold)}")

    return cars_to_buy


def find_cars_by_specification(specification):
    filter_query = Q()
    for key in specification.keys():
        value = specification.get(key)
        if key != "max_price":
            filter_query &= Q(**{key: value})

    logger.info(f"Searching cars with specification: {specification}")
    cars = Car.objects.filter(filter_query)
    logger.info(f"Found {len(cars)} cars matching the specification")
    logger.info(f"Found {str(cars)} cars matching the specification")
    return cars


def find_best_order_in_car_dealer(cars, max_price):
    best_price = {}
    logger.info(f"Best order car: {str(cars)}")
    for car in cars:
        try:
            car_price = (
                CarDealerCar.objects
                .filter(car=car, price_with_discount__lte=max_price)
                .order_by("price_with_discount")
                .first()
            )

            if car_price:
                best_price[car] = [car_price.price, car_price.car_dealer]

        except CarDealerCar.DoesNotExist:
            continue

    return best_price


def buy_car_from_car_dealer(car, car_dealer, client, price, count=1):
    SalesDealerHistory.objects.create(
        car=car,
        car_dealer=car_dealer,
        price=price,
        count=1
    )
    client.balance -= price * count
    client.save()
    return
