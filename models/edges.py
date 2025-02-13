from dataclasses import dataclass
from datetime import datetime
from models.utils import SpannerTable
import csv


@dataclass
class HasAdjacent:
    id: int
    to_id: int
    radius: int

    def __init__(self, edge):
        self.id = int(edge["id"])
        self.to_id = int(edge["to_id"])
        self.radius = int(edge["radius"])


@dataclass
class HasAdjacents(SpannerTable):
    def __init__(self):
        with open("data/HasAdjacent.csv") as f:
            reader = csv.DictReader(f)
            self.loadItems([HasAdjacent(row) for row in reader])

@dataclass
class HasProvider:
    id: int
    to_id: int

    def __init__(self, edge):
        self.id = int(edge["id"])
        self.provider_id = int(edge["to_id"])

@dataclass
class HasProviders(SpannerTable):
    def __init__(self):
        with open("data/HasProvider.csv") as f:
            reader = csv.DictReader(f)
            self.loadItems([HasProvider(row) for row in reader])

@dataclass
class HasConsumer:
    id: int
    to_id: int

    def __init__(self, edge):
        self.id = int(edge["id"])
        self.consumer_id = int(edge["to_id"])

@dataclass
class HasConsumers(SpannerTable):
    def __init__(self):
        with open("data/HasConsumer.csv") as f:
            reader = csv.DictReader(f)
            self.loadItems([HasConsumer(row) for row in reader])
