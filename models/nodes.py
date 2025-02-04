from dataclasses import dataclass
from datetime import datetime
from models.utils import SpannerTable
import csv


@dataclass
class Hex:
    id: int
    radius: int

    def __init__(self, hex):
        self.id = int(hex["id"])
        self.radius = int(hex["radius"])

@dataclass
class Hexes(SpannerTable):

    def __init__(self):
        with open("data/Hex.csv") as f:
            reader = csv.DictReader(f)
            self.loadItems([Hex(row) for row in reader])

