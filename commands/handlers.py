SUPPORTED_COMMANDS = {
    "PING",
    "HELP",
    "INFO",
    "QUIT",
    "LOGIN"
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


def handle_ping(arguments: list[str], session) -> dict:
    return ok("PONG")


def handle_info(arguments: list[str], session) -> dict:
    username = session.username or "Anonymous"

    authenticated = "Yes" if session.authenticated else "No"
    

    message = (
        "miniFTP server v0.2\n"
        f"User: {username}\n"
        f"Authenticated: {authenticated}\n"
    )

    return ok(message)


def handle_help(arguments: list[str], session) -> dict: 
    commands = ", ".join(sorted(SUPPORTED_COMMANDS))
    return ok(f"Supported commands {commands}")


def handle_quit(arguments: list[str], session) -> dict:
    return ok("Goodbye")


def handle_login(arguments: list[str], session) -> dict:
    if len(arguments) != 1:
        return error("Usage: LOGIN <username>")
    
    username = arguments[0]
    session.username = username
    session.authenticated = True

    return ok(f'Welcome {username}')