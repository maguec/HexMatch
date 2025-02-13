from dataclasses import dataclass
from datetime import datetime
from models.utils import SpannerTable
import csv


@dataclass
class Hex:
    id: int

    def __init__(self, hex):
        self.id = int(hex["id"])

@dataclass
class Hexes(SpannerTable):

    def __init__(self):
        with open("data/Hex.csv") as f:
            reader = csv.DictReader(f)
            self.loadItems([Hex(row) for row in reader])

@dataclass
class Consumer:
    id: int
    searching: int

    def __init__(self, consumer):
        self.id = int(consumer["id"])
        self.searching = int(consumer["searching"])

@dataclass
class Consumers(SpannerTable):

    def __init__(self):
        with open("data/Consumer.csv") as f:
            reader = csv.DictReader(f)
            self.loadItems([Consumer(row) for row in reader])

@dataclass
class Provider:
    id: int
    available: int
    rating: int

    def __init__(self, producer):
        self.id = int(producer["id"])
        self.searching = int(producer["available"])
        self.rating = int(producer["rating"])

@dataclass
class Providers(SpannerTable):    

    def __init__(self):
        with open("data/Provider.csv") as f:
            reader = csv.DictReader(f)
            self.loadItems([Provider(row) for row in reader])
