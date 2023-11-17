from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def init(self):
        self.size = 0
        self.buckets = [[] for i in range(8)]

    # Computes hash value for a word (a string)
    def get_hash(self, word):
        hash = 0
        for i in range(len(word)):
            hash += i * ord(word[i])
        # for c in word:
        #     hash += ord(c)
        return hash % self.bucket_list_size()

    # Doubles size of bucket list
    def rehash(self):
        words = []
        for bucket in self.buckets:
            for element in bucket:
                words.append(element)
        new_size = self.size * 2
        self.buckets = [[] for i in range(new_size)]
        self.size = 0
        for word in words:
            self.add(word)

    # Adds a word to set if not already added
    def add(self, word):
        hash = self.get_hash(word)
        if word not in self.buckets[hash]:
            self.buckets[hash].append(word)
            self.size += 1
            if self.size == self.bucket_list_size():
                self.rehash()

    # Returns a string representation of the set content
    def to_string(self):
        s = '{ '
        for bucket in self.buckets:
            for e in bucket:
                s += e + ' '
        return s + '}'

    # Returns current number of elements in set
    def get_size(self):
        return self.size

    # Returns True if word in set, otherwise False
    def contains(self, word):
        hash = self.get_hash(word)
        if word in self.buckets[hash]:
            return True
        else:
            return False

    # Returns current size of bucket list
    def bucket_list_size(self):
        return len(self.buckets)

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        hash = self.get_hash(word)
        if word in self.buckets[hash]:
            self.buckets[hash].remove(word)
            self.size -= 1

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        size = 0
        for bucket in self.buckets:
            bucket_size = len(bucket)
            if bucket_size > size:
                size = bucket_size
        return size
