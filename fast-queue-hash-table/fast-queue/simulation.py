#!/usr/bin/env python3

from datetime import datetime, timedelta
from random import random

from queue import PythonListQueue, LinkedListQueue, RingBufferQueue


def run_tests(queue_implementation):
    """
    A few simple assertions to ensure the queue actually works.

    Add your own!
    """
    queue = queue_implementation()
    assert queue.is_empty()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    queue.enqueue(3)
    queue.enqueue(4)
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.dequeue() == 4
    assert queue.is_empty()


def run_simulation(queue_implementation, length=10, p_enqueue=0.5, p_dequeue=0.5):
    """
    Run a simulation where a producer periodically adds to a queue, and
    a consumer periodically pulls from it.
    """
    print('  Running simulation for {}s, P(enq)={}, P(deq)={}'.format(length, p_enqueue, p_dequeue))

    start = last_msg = datetime.now()
    delta = timedelta(seconds=length)
    msg_freq = timedelta(seconds=3)
    num_enqueues = 0
    num_dequeues = 0
    max_queue_size = 0
    queue = queue_implementation()

    while True:
        now = datetime.now()
        if now - start > delta:
            break

        if now - last_msg > msg_freq:
            print('    {} enqueues, {} dequeues, {} max queue size'
                  .format(num_enqueues, num_dequeues, max_queue_size))
            last_msg = now

        if random() < p_enqueue:
            queue.enqueue((now, "New message!"))
            num_enqueues += 1
            max_queue_size = max(max_queue_size, queue.size())

        if random() < p_dequeue:
            if not queue.is_empty():
                queue.dequeue()
                num_dequeues += 1

    ops = (num_enqueues + num_dequeues) / length
    return ops

if __name__ == '__main__':
    for q in [PythonListQueue, LinkedListQueue, RingBufferQueue]:
        print("Testing {}".format(q.__name__))
        run_tests(q)

    print("All implementations passing simple correctness test, benchmarking...\n")

    prob_pairs = [(.5, .5), (.7, .3), (.3, .7), (.9, .1), (.1, .9)]

    for p_enq, p_deq in prob_pairs:
        print("Benchmarking for P(enq)={}, P(deq)={}".format(p_enq, p_deq))
        ops_for_impls = []
        for q in [PythonListQueue, LinkedListQueue, RingBufferQueue]:
            print("{}".format(q.__name__))
            ops = run_simulation(q, length=10, p_enqueue=p_enq, p_dequeue=p_deq)
            print('  Simulation complete, ran {:,} operations per second\n'.format(ops))
            ops_for_impls.append(ops)
        print('Operations per second (bigger is better):')
        print('  Python List: {}\n  Linked List: {}\n  Ring Buffer: {}'.format(*ops_for_impls))
        print('===========================================\n')

        run_tests(q)
