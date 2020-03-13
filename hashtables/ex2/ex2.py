#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable, hash_table_insert, hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # put tickets into hashtable, source is key, dest is value
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    trip_list = []

    # retrieve first ticket that has NONE as the source
    cur_ticket = hash_table_retrieve(hashtable, "NONE")  # LAX

    # loop while destination is not NONE
    while cur_ticket != "NONE":

        # put ticket into an array
        trip_list.append(cur_ticket)

        # retrieve the cur_ticket destination to find the matching key
        next_ticket = hash_table_retrieve(hashtable, cur_ticket)

        # reassign cur_ticket
        cur_ticket = next_ticket

    return trip_list
