#!/usr/bin/python

class Node(object):
    def __init__(self, data=None, obj = None):
        self.data = data
        self.obj = obj

    def get_data(self):
        return self.data

    def set_next(self, obj):
        self.obj = obj

    def get_next(self):
        return self.obj



class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        obj = Node(data)
        obj.set_next(self.head)
        self.head = obj


    def search(self, data):
        current = self.head
        found = False

        while current:

            if current.get_data() == data:
                found = True
                return "Data Found"
            else:
                current = current.get_next()

        return "No data found" 


     def delete(self, data):
         current = self.head
         previous = None
         found = False

         while current and not found:
             if current.get_data() == data:
                 found = True

             else:
                 previous = current
                 current = current.get_next()

         if found:
             previous.set_next(current.get_next())
             print "data deleted"

         else:
             print "No data found"
