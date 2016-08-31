# !/usr/bin/python

__author__ = "vineesh"

class Stack(object):

    def isEmpty(self):
        """."""
        return (self.stacklist == [])

    def peek(self):
        """."""
        if self.isEmpty():
           return 0
        return self.stacklist[-1]

    def push(self, expr):
        """."""
        return self.stacklist.append(expr)

    def pop(self):
        """."""
        return None if self.isEmpty() else self.stacklist.pop()

class BalanceParanthesis(Stack):
    def __init__(self, expr):
        self.expr = expr
        self.op = {'(': ')','[': ']','{': '}'}
        self.exprlist = expr.split()
        self.stacklist= list()


    def __call__(self):
        """."""
        for each in self.exprlist:
            if each in self.op:
                self.push(each)

            elif each in self.op.values():
                keyname = [op for op in self.op if self.op[op] == each]
                if self.pop() == keyname[0] :
                    continue
                raise Exception("Paranthesis is not balanced")

            else:
                continue
        if self.pop():
            raise Exception("Paranthesis is not balanced")

        return "Well Balanced expression"


"""
Input data should have space between every characters
else result will be inappropriate
Eg: ( A + B ) - 5

Because `space` act as delimiter in the input data
"""

data = raw_input("expr : ")
print BalanceParanthesis(data)()
