class MyHashMap:

    def __init__(self):
        self.data = [None] * (10**6+1)

    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        return self.data[key] if self.data[key] != None else -1

    def remove(self, key: int) -> None:
        self.data[key] = None
