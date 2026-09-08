class LRUCache:

    def __init__(self, capacity: int):
        self.hmap = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        val = self.hmap.get(key, -1)
        if val != -1:
            del self.hmap[key]
            self.hmap[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            del self.hmap[key]
        self.hmap[key] = value
        if len(self.hmap) > self.capacity:
            del self.hmap[next(iter(self.hmap.keys()))]
        
