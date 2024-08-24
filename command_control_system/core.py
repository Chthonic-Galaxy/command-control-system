from typing import Callable, List, Any, Tuple

from .exceptions import CommandExistsError, CommandNotFound

class Command:
    def __init__(self, name: str, func: Callable, args: List[Tuple[str, type, bool]] = None):
        self.name: str = name
        self.func: Callable = func
        self.args: List[Tuple[str, type, bool]] = args or []

    def execute(self, *args: Any, **kwargs: Any) -> Any:
        if len(args) != len(self.args):
            raise ValueError("Incorrect number of argument")
        
        converted_args = []
        for i, arg in enumerate(args):
            arg_name, arg_type, is_optional = self.args[i]
            try:
                converted_args.append(arg_type(arg))
            except (ValueError, TypeError):
                raise ValueError(f"Invalid argument type for argument {arg_name}")
        
        return self.func(*converted_args)

class CommandDispatcher:
    def __init__(self):
        self._commands: dict[str, Command] = {}

    def register_command(self, command: Command) -> None:
        if command.name in self._commands:
            raise CommandExistsError(command.name)
        self._commands[command.name] = command

    def execute_command(self, command_name: str, *args: Any, **kwargs: Any) -> Any:
        if command_name not in self._commands:
            raise CommandNotFound(command_name)
        command = self._commands[command_name]
        return command.execute(*args, **kwargs)


dispatcher = CommandDispatcher()  # Create a global dispatcher instance

def command(name: str, args: List[Tuple[str, type, bool]] = None):
    """
    Decorator to register a command.

    Args:
        name: The name of the command.
        args: A list of tuples, each defining an argument: (name, type, is_optional).
    """
    def decorator(func: Callable) -> Callable:
        cmd = Command(name, func, args)
        dispatcher.register_command(cmd)
        return func
    return decorator