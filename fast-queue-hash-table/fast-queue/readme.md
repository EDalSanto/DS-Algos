# Implement an Efficient Queue

In this exercise you'll be building and comparing the performance of a few implementations of a queue. A queue is a very common data structure, where the first item to enter the structure is the first one to come out. In an intuitive implementation of a queue we might append to the end of, and shift (pop from the front of), a Python list (or similar data structure in another language).

In this exercise you'll implement a queue in two new ways, and compare those strategies to the simple list-based implementation described above. We will find that different implementations perform better and worse in different scenarios.

We have provided a basic test for a basic queue API with 4 functions (enqueue, dequeue, size, is_empty). In addition to this basic correctness test, we have provided a benchmarking simulation that repeatedly enqueues and dequeues items from a provided queue implementation. The simulation we've provided benchmarks the queue implementation under that probabilistically enqueues and dequeues. Each round one, both, or neither of an enqueue operation and a dequeue operation might happen. We test the queues under 3 different scenarios:

* At every cycle there is a 50% chance of an enqueue, and a 50% chance of a dequeue.
* At every cycle there is a 70% chance of an enqueue and a 30% chance of a dequeue.
* At every cycle there is a 30% chance of an enqueue, and a 70% chance of a dequeue.

If you wish to experiment with other probabilities simply add, remove, or modify the tuples found at the bottom of `simulation.py`:

```
prob_pairs = [(.5, .5), (.7, .3), (.3, .7)]
```

## The Simulation

Our primary objective will be to implement a queue data structure that has good performance and memory usage characteristics. The current implementation in queue.py does not! You can use simulation.py to get a sense of how your queue may actually be used in practice. To test your implementations speed and correctness:

```
python3 simulation.py
```

## Getting Started

You can run the simulation by:

```
python3 simulation.py
```

When you run the simulation all the implementations will be run through the tests and benchmark. If one of the implementations throws an error the simulation will halt. Your goal is to complete the two incomplete Python classes `LinkedListQueue` and `RingBufferQueue`. Once you've completed those two classes, based on the benchmark results answer these questions:

* What are the strengths and weaknesses of each implementation?
  * When is each fast?
    - 50 / 50 => PythonListQueue
    - 70enq /  30deq => RingBuffer
    - 30enq / 70deq => PythonList by a bit
  * When is each slow?
    - 50 / 50 => LinkedList
    - 70enq / 30deq => PythonList
    - 30enq / 70deq => RingBuffer
* Is there an obvious winner across all scenarios?
  - I think so
* Can you relate the probabilities of enqueue and dequeuing to real world use cases?
  * What is an example of a situation where our queue might grow very large (higher enqueue probability)?
    - browser back button
  * What is an example of a situation where our queue stay rather small (higher dequeue probability)?
    - sending messages from 1 machine to the next
  * What is an example of a situation where the queues size might be stable (relatively equal probabilities)?
* The simulations we've provided perform operations in random orders...
  * Is there a non-random series of operations you'd expect to be fast or slow for any of these structures?
  * For example, if we performed 2000 enqueues then 2000 dequeues, which structure would you expect to perform the best?
    - PythonListQueue
