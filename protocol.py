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


def ok(message: str) -> dict:
    return {
        "status": 'OK',
        "message": message,
    }


def error(message: str) -> dict:
    return {
        "status": 'ERROR',
        "message": message,
    }


def handle_ping(arguments: list[str]) -> str:
    return ok("PONG")


def handle_info(arguments: list[str]) -> str:
    return ok("miniFTP server v0.2")


def handle_help(arguments: list[str]) -> str: 
    commands = ", ".join(sorted(SUPPORTED_COMMANDS))
    return ok(f"Supported commands {commands}")


def handle_quit(arguments: list[str]) -> str:
    return ok("Goodbye")


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

