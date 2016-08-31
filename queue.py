#!/usr/bin/python

class Queue(object):
    """ Queue implementation """
    def __init__(self):
        """ Intialization """
        self.elements = list()

    def is_empty(self):
        """ check stack empty """
        return (len(self.elements) == 0)

    def enqueue(self, item):
        """ inserted to queue """
        self.elements.append(item)

    def dequeue(self):
        """ Deleting from queue """
        if not self.is_empty():
            return self.elements.pop(0)

        raise Exception("Queue is underflowing")


class IndexQueue(object):
    """ Queue structure based on indices """

    def __init__(self):
        self.elements = list()
        self.tail = 0
        self.head = 0

    def is_empty(self):
        return (len(self.elements) == 0)

    def enqueue(self, item):
       """ enqueue operation """
       self.elements.insert(self.tail, item)

       if self.tail + 1 == len(self.elements):
           self.tail = 0
       else:
           self.tail += 1

    def dequeue(self):
        """ dequeue operation """
        if not self.is_empty():
            return self.elements.pop(self.head)

        raise Exception("Queue is underflowing")

queue = IndexQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.dequeue()
queue.dequeue()
queue.dequeue()
