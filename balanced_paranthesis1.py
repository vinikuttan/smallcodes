#!/usr/bin/python

class Stack(object):
    """ Stack """
    def __init__(self):
        self.items = list()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def balanced_paranthesis(expression):
    """ Simple algorithm to find balance paranthesis """

    stack = Stack()
    for i in expression:
        if i  == "(":
            stack.push(i)

        elif i == ")":
            if stack.is_empty():
                return False
            stack.pop()

    return True if stack.is_empty() else False


if __name__=="__main__":
    expression = "((A+B)-(C+D))"
    if balanced_paranthesis(expression):
        print "Paranthesis balanced in expression"
    else:
        print "Imbalanced Paranthesis"
