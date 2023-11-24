import random


def get_random_specification():
    cars_models = {
        "BMW": ["X5", "XM", "X6M"],
        "Mers": ["S500", "E200"],
        "Audi": ["A6", "RS6", "A7"],
        "Ford": ["F-Series", "Fiesta", "Focus"],
    }
    brand = random.choice(list(cars_models))
    model = random.choice(cars_models[brand])
    color = ["WHITE", "BLACK", "YELLOW", "GREEN", "PURPLE", "SPACE GRAY"]
    specification = {
        "brand": brand,
        "model": model,
        "year": random.uniform(1900, 2023),
        "color": random.choice(color),
    }
    return specification
