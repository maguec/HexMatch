#!/usr/bin/env python

from models.nodes import *
from models.edges import *
from google.cloud import spanner

if __name__ == "__main__":
    s = spanner.Client()
    instance = s.instance("hexmatch")
    client = instance.database("hexmatchdb")

    hexes = Hexes()
    hexes.load(client)

    hex_adjacents = HasAdjacents()
    hex_adjacents.load(client)

    producers = Providers()
    producers.load(client)

    consumers = Consumers()
    consumers.load(client)

    provider_adjacents = HasProviders()
    provider_adjacents.load(client)

    consumer_adjacents = HasConsumers()
    consumer_adjacents.load(client)

