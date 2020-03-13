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

    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
    
    # check if there is a ticket in the hashtable with the source None
    for i in range(length):
        if hashtable.storage[i].key == 'NONE':
            route.append(hashtable.storage[i].value)
            route.pop(0)
        if hashtable.storage[i].key in route:
            route.append(hashtable.storage[i].value)
            route.pop(0)
            
    for i in route:
        if i == 'NONE':
            route.pop(route.index('NONE'))

    print(route)
    return route
    
    # print(hashtable.storage)

# if __name__ == '__main__':
#     reconstruct_trip(tickets, len(tickets))
