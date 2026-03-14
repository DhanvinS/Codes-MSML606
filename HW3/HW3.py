# FEEL FREE TO ADD MORE FUNCTIONS AS PER YOUR NEED
# THERE IS NO UNCHANGEABLE "MAIN" FUNCTION IN THIS HW

import time
import random

# Implement HashMap in this class
# Do not use built in dictionary
# Implement own hashing function using division/multiplication method
class HashMap:
    def __init__(self, size=101):
        pass

    # retrieve a value associated with the key
    def search(self,key):
        pass 

    # insert the key value pair into the hash tables
    def insert(self,key,value):
        pass 

    # remove the key value pair from the hash table
    def delete(self,key):
        pass 

    # optional for open addressing collision method
    # if you choose chaining, don't forget to discuss it in the report
    def dynamicResizing(self):
        pass

    # hashing methods
    def _hash(self, key, method="division"):
        # Implement division method
        # Implement multiplication method
        pass


# Problem 2: Performance Analysis

def generate_keys(distribution, n):
    # uniform, skewed, or sequential
    pass

def measure_search_time(hashmap, keys):
    # use time.perf_counter()
    pass

def run_experiments():
    # test across different table sizes and load factors
    pass
