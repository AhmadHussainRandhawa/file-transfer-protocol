class Session:
    """
    Represents one connected client.
    """

    def __init__(self):
        self.authenticated = False
        self.username = None

    def login(self, username: str) -> None:
        self.authenticated = True
        self.username = username

    def logout(self) -> None:
        self.authenticated = False
        self.username = None

    def is_authenticated(self) -> bool:
        return self.authenticated