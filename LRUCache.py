from collections import OrderedDict



class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        else:
            self.dict.move_to_end(key)
            return self.dict[key]

    def put(self, key: int, value: int) -> None:
        if len(self.dict) > self.capacity - 1:
            self.dict.popitem(last=False)
        else:
            self.dict[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)