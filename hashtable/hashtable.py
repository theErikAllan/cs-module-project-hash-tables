class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"HashTableEntry({repr(self.key)},{repr(self.value)})"


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.bucket = [None for i in range(capacity)]
        self.capacity = capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        byte_array = str(key).encode('utf-8')

        for byte in byte_array:
            # the modulus keeps it 32-bit, python ints don't overflow
            hash = ((hash * 33) ^ byte) % 0x100000000

        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    # def put(self, key, value):
    #     """
    #     Store the value with the given key.

    #     Hash collisions should be handled with Linked List Chaining.

    #     Implement this.
    #     """
    #     # Your code here
    #     index = self.hash_index(key)
    #     self.bucket[index] = value

    def put(self, key, value):
        # First, we determine the index of our desired key:value pair
        index = self.hash_index(key)

        # Then we create a new node with the desired key:value pair
        new_node = HashTableEntry(key, value)

        # We look up the node at the index and set existing_node to it
        existing_node = self.bucket[index]

        # This if statement checks to see if a node exists at [index]
        if existing_node:
            # If there is already a node at [index], we create a variable for the last node and set it to None
            last_node = None

            # Now we loop through the linked list
            while existing_node:
                # We check the key at each node to see if it's equal to the key being passed in
                if existing_node.key == key:
                    # If the key of existing_node is equal to the key being passed in, we have found the right key so we set the value of that node to be the value being passed in
                    existing_node.value = value
                    return

                # Then we set last_node to the node we're inserting and change existing_node to point to its next node, thus moving us down the linked list
                last_node = existing_node
                existing_node = existing_node.next

            # Once we've exited the while loop, we set the next node of last_node to be the node we're inserting
            last_node.next = new_node
        else:
            # If existing_node doesn't exist (aka is None), then [index] is empty so we simply insert new_node
            self.bucket[index] = new_node

    # def delete(self, key):
    #     """
    #     Remove the value stored with the given key.

    #     Print a warning if the key is not found.

    #     Implement this.
    #     """
    #     # Your code here
    #     # self.put(key, None)
    #     index = self.hash_index(key)
    #     self.bucket[index] = None

    def delete(self, key):
        # First we hash the key to get the index
        index = self.hash_index(key)

        # Then we create a variable for the node we want to delete
        existing_node = self.bucket[index]

        # Next, we write an if statement to delete the node in question
        if existing_node:
            # We create a variable for the last node and set it to None
            last_node = None
            # Then we write a while loop that will run as long as the node in question exists
            while existing_node:
                # In our while loop we have another if statement checking the key of the current node to the key being passed in
                if existing_node.key == key:
                    # If there's a match, we have an if statement to check if last_node exists
                    if last_node:
                        # If last_node points to a node, we set last_node's next node to be the next node of the current node, partly removing the current node from the linked list
                        last_node.next = existing_node.next
                    else:
                        # If last_node doesn't point to anything, we set the node at the index in question to be the next node of the node we're trying to delete, partly removing the current node from the linked list
                        self.bucket[index] = existing_node.next

                # Finally, we set last_node to the node we're trying to delete, and then we set existing_node to existing_node.next, which in this case will be None
                last_node = existing_node
                existing_node = existing_node.next

    # def get(self, key):
    #     """
    #     Retrieve the value stored with the given key.

    #     Returns None if the key is not found.

    #     Implement this.
    #     """
    #     # Your code here
    #     index = self.hash_index(key)
    #     return self.bucket[index]

    def get(self, key):
        # First, we hash the key to determine the index our desired key is stored
        index = self.hash_index(key)

        # Then we set existing_node to equal the node at self.bucket[index]
        existing_node = self.bucket[index]

        # Next, we write an if statement checking if existing_node exists
        if existing_node:
            # If it does exist, we have a while loop that kicks in as long as existing_node continues existing in existence
            while existing_node:
                # In the while loop we are checking the key of each node to find the one that matches the key we're trying to find
                if existing_node.key == key:
                    # When we find the node that matches the key we're looking for, we return the value of the node
                    return existing_node.value
                # If the matching key is not found, we set existing_node to its next node and we continue down the linked list
                existing_node = existing_node.next

        # If the desired key cannot be found, we return None
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
