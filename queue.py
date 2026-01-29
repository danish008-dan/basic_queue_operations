"""
File Name: queue.py

Purpose:
--------
This file contains the implementation of Queue data structure.
Queue follows the FIFO principle (First In First Out).

Operations supported:
- Enqueue (insert element)
- Dequeue (remove element)
- Front (view front element)
- isEmpty (check if queue is empty)

Time Complexity:
----------------
Enqueue: O(1)
Dequeue: O(1)

Space Complexity:
-----------------
O(n)
"""

from collections import deque


class Queue:
    def __init__(self):
        # Initialize deque for efficient queue operations
        self.queue = deque()

    def enqueue(self, item):
        # Add element to the rear of the queue
        self.queue.append(item)

    def dequeue(self):
        # Remove element from the front of the queue
        if self.is_empty():
            return "Queue is empty"
        return self.queue.popleft()

    def front(self):
        # Return front element without removing it
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def is_empty(self):
        # Check if queue is empty
        return len(self.queue) == 0

    def size(self):
        # Return size of queue
        return len(self.queue)


# ------------------ Example Usage ------------------

q = Queue()

q.enqueue(100)
q.enqueue(200)
q.enqueue(300)

print("Front element:", q.front())
print("Dequeued element:", q.dequeue())
print("Queue size:", q.size())
