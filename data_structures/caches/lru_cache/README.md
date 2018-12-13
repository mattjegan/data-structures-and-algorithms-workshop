# LRU Cache

LRU Caches or Least Recently Used Caches are a data structure used to store values similarly to hash tables in that you can both set and read values quickly. The key difference between a LRU Cache and a hash table is that the cache has a fixed number of items it can hold and has a mechanism to select and remove certain values when the limit is reached. In the LRU Cache, that mechanism will trigger when the size of the cache reaches its limit and then it will select and remove the value in the cache that was least recently used or least recently accessed.

The LRU Cache in this project has the following methods you need to implement:
* `set_value(self, key, item)`: Adds an item to the cache using the key provided and if there isn't enough room, selects and removes the least recently used item.
* `get_value(self, key)`: Looks up the item in the cache using the provided key and returns it if it exists. If not, returns `None`. 