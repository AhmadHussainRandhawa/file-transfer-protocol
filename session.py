class Session:
    """
    Represents one connected client.
    """

    def __init__(self):
        self.authenticated = False
        self.username = None