from dataclasses import dataclass
from datetime import datetime
from models.utils import SpannerTable
import csv


@dataclass
class HasAdjacent:
    id: int
    to_id: int

    def __init__(self, edge):
        self.id = int(edge["id"])
        self.to_id = int(edge["to_id"])


@dataclass
class HasAdjacents(SpannerTable):
    def __init__(self):
        with open("data/HasAdjacent.csv") as f:
            reader = csv.DictReader(f)
            self.loadItems([HasAdjacent(row) for row in reader])
