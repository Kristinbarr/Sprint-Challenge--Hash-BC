#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # insert tickets into table
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    destinations = []

    # find start of ticket with source of "NONE"
    current_destination = hash_table_retrieve(hashtable, "NONE")

    # loop = while the destination is not NONE
    while current_destination is not "NONE":
        # append destination to output list
        destinations.append(current_destination)
        # update the current ticket
        current_source = hash_table_retrieve(hashtable, current_destination)
        current_destination = current_source

    return destinations

