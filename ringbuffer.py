#!/usr/bin/env python3

class RingBuffer:
    def __init__(self, capacity: int):
        # Initializes an empty ring buffer object with the given max capacity
        self._front = 0
        self._rear = 0
        self.currentsize = 0
        self.MAX_CAP = capacity
        self.buffer = [None] * capacity

    def size(self) -> int:
        # Returns the current size of the ring buffer
        return self.currentsize

    def is_empty(self) -> bool:
        # Checks if the ring buffer is empty
        if self.currentsize == 0: return True
        return False
        
    def is_full(self) -> bool:
        # Checks if the ring buffer is full
        if self.currentsize == self.MAX_CAP: return True
        return False

    def enqueue(self, x: float):
        # Adds a new value to the end of ring buffer
        if self.is_full():
            raise RingBufferFull("Error: Can't enqueue. The buffer is full.")
        else:
            self.buffer[self._rear] = x
            self._rear = (self._rear + 1) % self.MAX_CAP
            self.currentsize += 1

    def dequeue(self) -> float:
        # Returns and removes the item at the front of ring buffer
        if self.is_empty():
            raise RingBufferEmpty("Error: Can't dequeue. The buffer is empty.")
        else:
            item = self.buffer[self._front]
            self.buffer[self._front] = None
            self._front = (self._front + 1) % self.MAX_CAP
            self.currentsize -= 1
            return item

    def peek(self) -> float:
        # Returns the value at the front the ring buffer
        if self.is_empty():
            raise RingBufferEmpty("Error: Can't peek. The buffer is empty.")
        return self.buffer[self._front]

class RingBufferFull(Exception):
    pass

class RingBufferEmpty(Exception):
    pass
