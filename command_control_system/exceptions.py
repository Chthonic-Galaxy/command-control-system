class CommandError(Exception):
    """Base class for all command-related exceptions."""

class CommandExistsError(CommandError):
    """Command already exists."""

    def __init__(self, command_name: str):
        super().__init__(f"Command '{command_name}' already exists.")
        self.command_name = command_name
        
class CommandNotFound(CommandError):
    """Command not found."""
    
    def __init__(self, command_name: str):
        super().__init__(f"Command '{command_name}' not found.")
        self.command_name = command_name