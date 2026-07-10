from commands.handlers import (
    error,
    handle_help,
    handle_info,
    handle_ping,
    handle_quit,
    handle_login,
    handle_logout,
    handle_pwd,
)


AUTH_REQUIRED_COMMANDS = {
    "PWD",
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


COMMAND_HANDLERS = {
    "PING" : handle_ping, 
    "INFO" : handle_info, 
    "HELP" : handle_help, 
    "QUIT" : handle_quit,
    "LOGIN": handle_login,
    "LOGOUT": handle_logout,
    "PWD": handle_pwd,
}


def handle_command(command: str, arguments: list[str], session) -> dict:
    handler = COMMAND_HANDLERS.get(command)

    if handler is None:
        return error("unknown command")
    
    if (command in AUTH_REQUIRED_COMMANDS and not session.is_authenticated()):
        return error("Please login first.")
    
    return handler(arguments, session)


def process_message(message: str, session) -> dict:
    """
    Process a raw client message and return
    a protocol response.
    """

    command, arguments = parse_message(message)

    return handle_command(command, arguments, session)
