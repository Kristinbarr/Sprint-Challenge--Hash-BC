#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # loop through weight arr and insert into hash table
    for i in range(length):
        print('\nWEIGHT:', weights[i])
        # weight is key and index is value
        hash_table_insert(ht, weights[i], i)

    weight1 = weights[0]
    weight2 = weights[0]

    # loop through looking for weights
    while 
    
    # if both indexes are the same, no match was found, return None
    if weight1.value == weight2.value:
        return None
    else:
        # returns a tuple of 2 weights
        if weight2 > weight1:
            weight1, weight2 = weight2, weight1
        return (weight, weight)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
