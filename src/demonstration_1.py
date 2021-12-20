"""
Your task is create your own HashTable without using a built-in library.

Your HashTable needs to have the following functions:

- put(key, value) : Inserts a (key, value) pair into the HashTable. If the
value already exists in the HashTable, update the value.
- get(key): Returns the value to which the specified key is mapped, or -1 if
this map contains no mapping for the key.
- remove(key) : Remove the mapping for the value key if this map contains the
mapping for the key.

Example:

```plaintext
hash_table = MyHashTable();
hash_table.put("a", 1);
hash_table.put("b", 2);
hash_table.get("a");            // returns 1
hash_table.get("c");            // returns -1 (not found)
hash_table.put("b", 1);         // update the existing value
hash_table.get("b");            // returns 1
hash_table.remove("b");         // remove the mapping for 2
hash_table.get("b");            // returns -1 (not found)
```
"""
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.count = 0

    def hash_index(self, key):
        # take an arbitriray key and return a valid integer index at which to store the (key, value)
        # A standard hashing function: DJB2
        # Cast the key to a string and get bytes
        str_key = str(key).encoded()

        # Start from an arbitrary large prime
        hash_value = 5381

        # Bit-shift and sum for each character
        for b in str_key:
            hash_value = ((hash_value << 5) + hash_value) + b
            hash_value &= 0xffffffff # DJB2 is a 32-bit hash, only keep 32 bits

        return hash_value % self.capacity

    def put(self, key, value):
        # Store the value with the given key.
        # In the event of a collision, simply overwrite the previous value

        # calculate the index hash_index(key)
        index = self.hash_index(key)

        # look through the linked list at sotrage[index] to see if this key is already in the table
        currentNode = self.storage[index]
        while currentNode:
            if currentNode.key == key: # found key in list
                currentNode.value = value # update value
                return
            currentNode = currentNode.next

        # otherwise, append a new ListNode(key, value) to the linked list
        newNode = ListNode(key, value)
        newNode.next = self.storage[index]
        self.storage[index] = newNode

        # increment the item count (if there wasn't something there before)
        if self.storage[index] == None:
            self.count += 1

        # assign value to storage[index]
        self.storage[index] = value
        return


    def get(self, key):
        # Your code here


    def remove(self, key: int) -> None:
        # Your code here

