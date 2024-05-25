#!/usr/bin/env python3

import math 
from ringbuffer import *
from random import uniform

class GuitarString:
    def __init__(self, frequency: float):
        # Initializes the guitar string object with the given frequency
        self.capacity = math.ceil(44100/frequency)
        self.buffer = RingBuffer(self.capacity)
        self.tick_so_far = 0

        for n in range(self.capacity):
            self.buffer.enqueue(0)

    @classmethod
    def make_from_array(cls, init: list[int]):
        # Initializes a guitar string with the size and initial values of the array
        stg = cls(1000)

        stg.capacity = len(init)
        stg.buffer = RingBuffer(stg.capacity)
        for x in init:
            stg.buffer.enqueue(x)
        return stg

    def pluck(self):
        # Sets the buffer to white noise
        for n in range(self.capacity):
            randomint = uniform(-0.5, 0.5)
            self.buffer.dequeue()
            self.buffer.enqueue(randomint)

    def tick(self):
        # Advances the simulation one time step by applying the Karplus--Strong update
        n1 = self.buffer.peek()
        self.buffer.dequeue()

        n2 = self.buffer.peek()

        n3 = (0.996 * ((n1 + n2) / 2))
        self.buffer.enqueue(n3)

        self.tick_so_far += 1

    def sample(self) -> float:
        # Returns the value at the front of the ring buffer
        return self.buffer.peek()

    def time(self) -> int:
        # Return the number of ticks so far
        return self.tick_so_far