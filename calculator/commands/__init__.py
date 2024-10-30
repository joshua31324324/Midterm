from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, params=None):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, user_input: str):
        """ Look before you leap (LBYL) - Use when its less likely to work
        if command_name in self.commands:
            self.commands[command_name].execute()
        else:
            print(f"No such command: {command_name}")
        """
        """Easier to ask for forgiveness than permission (EAFP) - Use when its going to most likely work"""
        if not user_input:
            return
            
        command_name = user_input.split()[0]
        if len(user_input.split()) > 1:
            params = user_input.split()[1:]
            try:
                self.commands[command_name].execute(params)
            except KeyError:
                print(f"No such command: {command_name}")
        else:
            try:
                self.commands[command_name].execute()
            except KeyError:
                print(f"No such command: {command_name}")
