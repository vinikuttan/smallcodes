#!/usr/bin/python

import os

class StopUndo(Exception):
    pass


class CommandException(Exception):
    pass


class CreateFile(object):
    def __init__(self, file_list):
        self.file_list = file_list

    def execute(self):
        dir_ = os.getcwd()
        for each in self.file_list:
            file_ = open(dir_ + os.sep + each, 'w')
            file_.close()


class RenameFile(object):
    def __init__(self, from_, to_):
        self.from_ = from_
        self.to_ = to_

    def execute(self):
        os.rename(self.from_, self.to_)

    def undo(self):
        os.rename(self.to_, self.from_)


class History(object):

    def __init__(self):
        self.commands = list()

    def execute(self, command):
        self.commands.append(command)
        if not isinstance(command, RenameFile):
            raise CommandException("Please enter appropriate rename object")
        command.execute()

    def undo(self):
        if not len(self.commands) > 0:
            raise StopUndo("No more items to undo")
        self.commands.pop().undo()

if __name__=="__main__":
    CreateFile(["filepath1", "filepath3"]).execute()
    history = History()
    history.execute(RenameFile("filepath1", "filepath2"))
    history.execute(RenameFile("filepath3", "filepath4"))
    history.undo()
    history.undo()
    history.undo()
