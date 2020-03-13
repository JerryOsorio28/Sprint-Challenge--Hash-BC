#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    
    # Loop to insert weights in the hashtable
    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)
    # Captures the weight difference between the weight limit and the weights by substracting the weights from the limit.
    weight = [limit - weight for weight in weights]
    # This list verifies if the difference numbers are a match in the hashtable
    matched = [node.key for node in ht.storage if node is not None and node.key in weight]
    # And this list grabs the index of such values in the hastable
    answer = [weights.index(num) for num in weights if num in matched]
    
    # we check if the answer is not empty, if it is we return None
    if len(answer) > 1:
        # if it is not empty, we check if the values are the same
        if answer[0] == answer[1]:
            # if they are we set the index of the index in 0 to 1, since it's needed in reversed order.
            answer[0] = 1
            # and return it
            return answer
        # if values are not the same, we sort them in reverse and return them.
        else:
            answer = sorted(answer, reverse=True)
            return answer
    else:
        return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


if __name__ == "__main__":
    print(HashTable)