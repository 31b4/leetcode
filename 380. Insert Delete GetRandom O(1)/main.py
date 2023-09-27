class RandomizedSet:

    def __init__(self):
        self.hashMap = {}
        self.dataMap = []

    def insert(self, val: int) -> bool:
        if val in self.hashMap:
            return False
        self.hashMap[val] = len(self.dataMap)
        self.dataMap.append(val)
        return True

    def remove(self, val: int) -> bool:
        if not val in self.hashMap:
            return False
        last_elem_in_list = self.dataMap[-1]
        index_of_elem_to_remove = self.hashMap[val]
        self.hashMap[last_elem_in_list] = index_of_elem_to_remove
        self.dataMap[index_of_elem_to_remove] = last_elem_in_list
        self.dataMap[-1] = val
        del self.dataMap[-1]# del faster than .pop
        del self.hashMap[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.dataMap)
