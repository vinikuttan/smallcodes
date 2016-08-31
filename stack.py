#!/usr/bin/python

__author__ = "vineesh"

class Stack(object):
    """ Stack implementation"""

    def __init__(self):
        """ Initialization"""
        self.elements = list()

    def is_empty(self):
        return (len(self.elements) == 0)

    def push(self, item):
        """ insert elements to stack """
        self.elements.append(item)

    def pop(self):
        """ delete elements from stack """
        if self.is_empty():
            return self.elements.pop()

        raise Exception("Stack is underflowing")
