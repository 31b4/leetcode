class FirstUnique:

    def __init__(self, nums: List[int]):
        self.queue = nums
        self.ptr = 0
        self.counter = Counter(nums)
        self.move_ptr()
    
    def move_ptr(self):
        while self.counter[self.queue[self.ptr]] != 1:
            self.ptr += 1
            if self.ptr == len(self.queue):
                break
        
    def showFirstUnique(self) -> int:
        if self.ptr == len(self.queue):
            return -1
        return self.queue[self.ptr]

    def add(self, value: int) -> None:
        self.queue.append(value)
        self.counter[value] += 1
        self.move_ptr()
