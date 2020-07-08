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
    A hash table with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.storage = [None] * capacity
        self.count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        load_factor = (self.count/self.capacity)
        return load_factor

    def fnv1(self, key, seed=0):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        # Constants
        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037

        # FNV-1a Hash Function
        hash = offset_basis + seed
        for char in key:
            hash = hash * FNV_prime
            hash = hash ^ ord(char)
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # We need to find the slot where the passed in value will be stored
        slot = self.hash_index(key)

        # Then we create a variable to point to the element in the slot
        current_node = self.storage[slot]

        # We create a node using the key:value pair being passed in
        new_node = HashTableEntry(key, value)

        # We use a conditional to check if the index is already occupied
        if current_node:
            # If so, we establish a head node so we can traverse the linked list in said index/slot
            prev_node = None
            # We use a while loop to traverse the bucket array
            while current_node:
                # Then we check to see if the occupied element's key matches the key being passed in
                if current_node.key == key:
                    # If it does, then we update the value of the key:value pair
                    current_node.value = value
                    return
                # If it does not match, we change the head node variable to point to the current node
                prev_node = current_node
                # And we change the current node variable to point to the current node's next node
                current_node = current_node.next
                # So we traverse
            # After the while loop finishes, there is no duplicate key, so we add the new node to the end of the bucket
            # And increment the counter (for load factor calculation)
            prev_node.next = new_node
            self.count += 1
        # If the current node points to None, we pass the new node into the bucket
        # And increment the counter (for load factor calculation)
        else:
            self.storage[slot] = new_node
            self.count += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # First, we hash the key to get the slot containing the node we want to delete
        slot = self.hash_index(key)
        # Then we create a variable to point to the node in that slot
        current_node = self.storage[slot]
        # We use a conditional statement to check if the contents at slot exist
        if current_node:
            # Conditional to check if the first node is the node we're looking for
            if current_node.key == key:
                self.storage[slot] = current_node.next
                return
            # We create a variable to point to the previous node and set it to None
            prev_node = None
            # If something exists in that slot, we use a while loop to traverse its contents
            while current_node:
                # At each node, we check to see if the node's key matches the key we're looking for
                if current_node.key == key:
                    # If we find the node with a matching key, we point the previous node's next node to the current node's next node
                    prev_node.next = current_node.next
                    return
                # If it doesn't, we increment the previous node and current node to the next nodes
                prev_node = current_node
                current_node = current_node.next
        # If something doesn't exist in that slot, we return None
        else:
            return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # First, we find the slot where the node in question could be
        slot = self.hash_index(key)

        # Then we create a variable, current_node, to point to the contents of the slot
        current_node = self.storage[slot]

        # We use a conditional to check if the current node is pointing to a node
        if current_node:
            # If it's pointing to a node, we want to traverse the contents (linked list) until we find the key we are looking for
            # So we use a while loop
            while current_node:
                # At each node, we have a conditional to check if the node's key matches the key being passed in
                if current_node.key == key:
                    # If we find a match, we return the node's value
                    return current_node.value
                # If the current node doesn't contain the droid we are looking for, we increment the current_node to current_node.next, traversing the linked list as a result
                current_node = current_node.next
        # If we don't find a match, we return None
        else:
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # First, we create a copy of the current list
        storage_copy = self.storage

        # Then we update self.storage with the new capacity
        self.capacity = new_capacity
        self.storage = [None] * self.capacity

        # We iterate through the copy and rehash the contents into the updated self.storage
        for slot in range(len(storage_copy)):
            if storage_copy[slot]:
                current_node = storage_copy[slot]
                while current_node:
                    self.put(current_node.key, current_node.value)
                    current_node = current_node.next
        
        return self.get_load_factor()


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
