SUPPORTED_COMMANDS = {
    "PING",
    "HELP",
    "INFO",
    "QUIT",
}


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
