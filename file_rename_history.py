#!/usr/bin/python
import os

class StopUndo(Exception):
    pass

class CommandException(Exception):
    pass

class CreateFile(object):
    def __init__(self, file_list):
        self.file_list = file_list
        self.dir_ = os.getcwd()

    def execute(self):
        for each in self.file_list:
            open(self.dir_ + os.sep + each, 'w').close()

    def undo(self):
        for each_file in self.file_list:
            if not os.path.isfile(self.dir_ + os.sep + each_file):
                raise StopUndo("No file found {}".format(each_file))
            os.remove(each_file)


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
    history = History()
    history.execute(CreateFile(["filepath1", "filepath3"]))
    history.execute(RenameFile("filepath1", "filepath2"))
    history.execute(RenameFile("filepath3", "filepath4"))
    history.undo()
    history.undo()
    history.undo()
    
    # below undo will stop undo the history with exception raised
    history.undo()
