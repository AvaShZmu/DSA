class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * self.capacity
        self.size = 0

    def __hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self.__hash(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1

        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def search(self, key):
        index = self.__hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError

    def delete(self, key):
        index = self.__hash(key)

        previous = None
        current = self.table[index]

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current
            current = current.next
        raise KeyError

    def __str__(self):
        elements = []
        for i in range(self.capacity):
            current = self.table[i]
            while current:
                elements.append((current.key, current.value))
                current = current.next
        return str(elements)

if __name__ == '__main__':
    dictionary = {'apple': 1, 'pear': 2, "cocktail": 3, "hi": 4}
    hash_table = HashTable(3)

    for key, value in dictionary.items():
        hash_table.insert(key, value)

