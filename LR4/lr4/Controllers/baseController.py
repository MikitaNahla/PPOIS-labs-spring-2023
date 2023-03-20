from tabulate import tabulate

from lr4.garden.garden import load, Garden
from lr4.garden.plants import whatThePlant, whatTheSeed


class BaseController:
    def __init__(self):
        self.garden = load()

    def get_plants(self):
        return self.garden.model.matrix

    def view(self):
        print(tabulate(self.garden.model.print()))

    def add(self, plant_name: str, x: int, y: int):
        plant = whatThePlant(plant_name)
        self.garden.model.addEntity(plant, x=x, y=y)
        self.garden.model.garbageCollector()
        self.garden.warp(1)
        self.garden.model.save()

    def add_seed(self, seed_name: str, x: int, y: int):
        seed = whatTheSeed(seed_name)
        self.garden.model.addEntity(seed, x, y)
        self.garden.model.garbageCollector()
        self.garden.warp(1)
        self.garden.model.save()

    def remove(self, x: int, y: int):
        self.garden.model.removeEntity(x, y)
        self.garden.model.garbageCollector()
        self.garden.warp(1)
        self.garden.model.save()

    def weather(self, type: str, time: int):
        self.garden.model.weather.type = type
        self.garden.model.weather.time = time
        self.garden.model.garbageCollector()
        self.garden.warp(1)
        self.garden.model.save()

    def warp(self, time: int):
        self.garden.warp(time)
        self.garden.model.garbageCollector()
        self.garden.model.save()
