class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_map = {}

    def insert(self, key: str, val: int) -> None:
        self.hash_map[key] = val

    def sum(self, prefix: str) -> int:
        result = 0
        for key in self.hash_map.keys():
            if len(key) >= len(prefix):
                match = True
                for i in range(len(prefix)):
                    if prefix[i] != key[i]:
                        match = False
                if match:
                    result += self.hash_map[key]


        return result

print('ab' in 'aab')


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)