class MyCircularDeque:
    def __init__(self, k: int):
        self.v = [-1] * k  # Initialize deque with -1
        self.front = 0
        self.back = 0
        self.size = 0  # Keeps track of the current number of elements
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        # Way - 01
        if self.front == 0:
            self.front = self.capacity - 1  # Wrap around to the end
        else:
            self.front -= 1  # Simply decrement front

        # Way - 02 (Alternative method commented out)
        # self.front = (self.front - 1 + self.capacity) % self.capacity

        self.v[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.v[self.back] = value

        # Way - 01
        if self.back == self.capacity - 1:
            self.back = 0  # Wrap around to the beginning
        else:
            self.back += 1  # Simply increment back

        # Way - 02 (Alternative method commented out)
        # self.back = (self.back + 1) % self.capacity

        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.v[self.front] = -1

        # Way - 01
        if self.front == self.capacity - 1:
            self.front = 0  # Wrap around to the beginning
        else:
            self.front += 1  # Simply increment front

        # Way - 02 (Alternative method commented out)
        # self.front = (self.front + 1) % self.capacity

        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        if self.back == 0:
            self.back = self.capacity - 1  # Wrap around to the end
        else:
            self.back -= 1  # Simply decrement back

        self.v[self.back] = -1
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.v[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        if self.back == 0:
            return self.v[self.capacity - 1]  # Wrap around to the last valid element
        else:
            return self.v[self.back - 1]  # Get the last element

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
