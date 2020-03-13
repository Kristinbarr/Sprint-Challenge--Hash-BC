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
        # weight is key and index is value
        hash_table_insert(ht, weights[i], i)

    # save an array and add to the array when a match is found
    weight_list = []

    # loop through looking for weights
    for weight in weights:
        weight2 = limit - weight
        
        index2 = hash_table_retrieve(ht, weight2)
        #  weight2 index is valid and not inside the weight list
        if index2 and (index2 not in weight_list):
            weight_list.append(index2)
        elif index2 and (index2 in weight_list):
            for i in range(length):
                if limit - weight2 == weights[i] and (i not in weight_list):
                    weight_list.append(i)

    if len(weight_list) == 0:
        return None
    else:
        weight_list.sort(reverse=True)
        return weight_list


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
