# FEEL FREE TO ADD MORE FUNCTIONS AS PER YOUR NEED
# THERE IS NO UNCHANGEABLE "MAIN" FUNCTION IN THIS HW

import time
import random
import matplotlib.pyplot as plt

# Implement HashMap in this class
# Do not use built in dictionary
# Implement own hashing function using division/multiplication method
class HashMap:
    def __init__(self, size=101):
        self.size = size
        self.table = [[] for _ in range(size)]

    # here retrieving value associated with the key
    def search(self, key):
        index = self._hash(key)

        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v

        return None

    # insert the key value pair into the hash tables
    def insert(self, key, value):
        index = self._hash(key)

        bucket = self.table[index]

        # checking if key already exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))


    # remove the key value pair from the hash table
    def delete(self, key):
        index = self._hash(key)

        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return True

        return False 

    # optional for open addressing collision method so not using this
    def dynamicResizing(self):
        pass

    # hashing methods
    def _hash(self, key, method="division"):
        # Implement division method
        # Implement multiplication method
        # converting key into integer
        if isinstance(key, str):
            key = sum(ord(c) for c in key)

        if method == "division":
            return key % self.size

        elif method == "multiplication":
            A = 0.6180339887
            return int(self.size * ((key * A) % 1))



# Problem 2: Performance Analysis

def generate_keys(distribution, n):
    # uniform, skewed, or sequential
    if distribution == "uniform":
        return [random.randint(1, 1000000) for _ in range(n)]

    elif distribution == "skewed":
        return [int(random.expovariate(0.01)) for _ in range(n)]

    elif distribution == "sequential":
        return list(range(n))

    else:
        return []

def measure_search_time(hashmap, keys):
    # use time.perf_counter()
    pass

def run_experiments():
    # test across different table sizes and load factors
    pass
