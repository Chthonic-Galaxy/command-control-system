from command_control_system.core import dispatcher, command 

@command("add", args=[("x", int, False), ("y", int, False)])
def add(x: int, y: int):
    return x + y

@command("greet", args=[("name", str, False), ("greeting", str, True)])
def greet(name: str, greeting: str = "Hello"):
    return f"{greeting}, {name}!"
