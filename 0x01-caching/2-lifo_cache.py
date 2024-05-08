#!/usr/bin/env python3
"""
LIFO Caching
"""

BaseCaching = __import__('base_caching').BaseCaching

class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching and implements a LIFO caching system.
    """

    def __init__(self):
        """
        Initialize the LIFOCache instance.
        """
        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key for the item.
            item: The item to be stored.

        Returns:
            None
        """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.key_indexes.remove(key)
                else:
                    del self.cache_data[self.key_indexes[self.MAX_ITEMS - 1]]
                    item_discarded = self.key_indexes.pop(self.MAX_ITEMS - 1)
                    print("DISCARD:", item_discarded)

            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value associated with the given key, or None if the key doesn't exist.
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None

