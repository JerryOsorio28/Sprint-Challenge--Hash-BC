#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    # weights = [ 4, 6, 10, 15, 16 ]
    # length = 5
    # limit = 21
    # # output: [ 3, 1 ]
    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)
        
    weight = [limit - weight for weight in weights]
    matched = [node.key for node in ht.storage if node is not None and node.key in weight]
    answer = [weights.index(num) for num in weights if num in matched]
    
    if len(answer) > 1:
        if answer[0] == answer[1]:
            answer[1] = 1
            answer = sorted(answer, reverse=True)
            return answer
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