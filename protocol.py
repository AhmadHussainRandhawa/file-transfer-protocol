SUPPORTED_COMMANDS = {
    "PING",
    "HELP",
    "INFO",
    "QUIT",
}


def parse_message(message: str) -> tuple[str, list[str]]:
    """
    Convert a raw client message into:
        command, arguments

    Example:
        "PING"
            -> ("PING", [])

        "LOGIN ahmad secret"
            -> ("LOGIN", ["ahmad", "secret"])
    """

    parts = message.strip().split()

    if not parts:
        return "", []

    command = parts[0].upper()
    arguments = parts[1:]

    return command, arguments


def handle_ping(arguments: list[str]) -> str:
    return "OK PONG"


def handle_info(arguments: list[str]) -> str:
    return "OK miniFTP Server v0.2"


def handle_help(arguments: list[str]) -> str: 
    commands = ", ".join(sorted(SUPPORTED_COMMANDS))
    return f"OK Supported commands {commands}"


def handle_quit(arguments: list[str]) -> str:
    return "OK Goodbye"


COMMAND_HANDLERS = {
    "PING" : handle_ping, 
    "INFO" : handle_info, 
    "HELP" : handle_help, 
    "QUIT" : handle_quit,
}


def handle_command(command: str, arguments: list[str]) -> str:
    handler = COMMAND_HANDLERS.get(command)

    if not handler:
        return "ERROR unknown command"
    
    return handler(arguments)

