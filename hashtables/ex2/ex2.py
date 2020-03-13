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
    route = []

    """
    YOUR CODE HERE
    """
    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
    
    i = 0
    while len(route) < len(hashtable.storage):
        if i >= 10:
            i = 0
        if hashtable.storage[i] is None:
            i += 1
            continue
        elif hashtable.storage[i].key == 'NONE' and hashtable.storage[i].value not in route:
            route.append(hashtable.storage[i].value)
            i += 1
            continue

        node = hashtable.storage[i]
        while node is not None:
            if node.key in route and node.value not in route:
                route.append(node.value)
                break
            node = node.next
        i += 1

    for i in route:
        if i == 'NONE':
            route.pop(route.index('NONE'))

    # print('route', route)
    return route

    
    # print(hashtable.storage)

# if __name__ == '__main__':
#     reconstruct_trip(tickets, len(tickets))
