from commands.handlers import (
    error,
    handle_help,
    handle_info,
    handle_ping,
    handle_quit,
)


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


COMMAND_HANDLERS = {
    "PING" : handle_ping, 
    "INFO" : handle_info, 
    "HELP" : handle_help, 
    "QUIT" : handle_quit,
}


def handle_command(command: str, arguments: list[str]) -> str:
    handler = COMMAND_HANDLERS.get(command)

    if handler is None:
        return error("UNKNOWN COMMAND")
    
    return handler(arguments)

