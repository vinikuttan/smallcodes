# !/usr/bin/python

from abc import ABCMeta, abstractmethod
from collections import deque

# config values (global level)
call_state = ("READY", "INPROGRESS", "COMPLETED")
receiver_state = ("IDLE", "BUSY")


class CallReceiver(metaclass=ABCMeta):
    def __init__(self):
        self.call_state = None
        self.receiver_state = None
        self.receiver = None
        self.customer = None
        self.employee = None

    @abstractmethod
    def take_call(self, customer):
        try:
            # Db hit to get idle state receiver
            # where condition will be self.receiver and receiver_state
            # return ``None` when all receivers are engaged
            pass
        except:
            #log exceptions and return ``None``
            #so the calls will be queued
            pass
        else:
            # customer.employee = employee
            # customer.receiver = self.receiver
            #self.inprogress_call()
            pass
        return customer

    def inprogress_call(self):
        self.receiver_state = receiver_state[1]
        self.call_state = call_state[1]
        # re-update the ``self.employee`` with ``BUSY`` receiver_state

    def complete_call(self):
        self.receiver_state = receiver_state[0]
        self.call_state = call_state[2]
        # re-update the ``self.employee`` with ``IDLE`` receiver_state


class Level2Receiver(CallReceiver):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.receiver =  "Level2"

    def take_call(self, customer):
        return super(self.__class__, self).take_call()


class Level1Receiver(CallReceiver):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.receiver =  "Level1"

    def take_call(self, customer):
        return super(self.__class__, self).take_call()


class Level0Receiver(CallReceiver):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.receiver =  "Level0"

    def take_call(self, customer):
        return super(self.__class__, self).take_call()


class CallInitiater(object):
    def __init__(self):
        self.call_queue = deque()

    def place_call(self, customer):
        call_object = Level0Receiver.take_call(customer) or
                      Level1Receiver.take_call(customer) or
                      Level2Receiver.take_call(customer)

        if call_object is None:
            self.call_queue(customer)
            return "Call is in queue"

        return call_object

    def escalate_calls(self, customer, employee):
        if employee not in ("Level1", "Level2"):
            raise Exception("call will be escalated to level1 and level2 employees")

        if employee == "Level1":
            return Level1Receiver.take_call(customer)
        return Level2Receiver.take_call(customer)


class Customer(object):
    def __init__(self, *kwargs):
        self.name  = kwargs.get("name", '')
        self.contact = kwargs.get("phone", kwargs.get("email", ''))

    def connect_call(self):
        connect = CallInitiater()
        return connect.place_call(self)
