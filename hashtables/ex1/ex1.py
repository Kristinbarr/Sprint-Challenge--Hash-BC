#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # iterate through weights
    for i in range(length):
        # insert each weight into hash table w index as value
        hash_table_insert(ht, weights[i], i)

    for i in range(length):

        # to get match, subtract cur weight from limit
        match = limit - weights[i]
        # get index of match
        match_idx = hash_table_retrieve(ht, match)

        # check if match is in ht
        if match_idx is not None:
            # return tuple of indexes, () higher, lower )
            return (match_idx, i)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
