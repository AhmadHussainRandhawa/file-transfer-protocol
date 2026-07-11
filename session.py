from pathlib import Path


UPLOAD_WAITING_FOR_SIZE = "WAITING_FOR_SIZE"
UPLOAD_RECEIVING_FILE = "RECEIVING_FILE"


class Session:
    """
    Represents one connected client.
    """

    def __init__(self):
        self.authenticated = False
        self.username = None
        self.current_directory = Path("/")
        self.pending_download = None
        self.pending_upload = None
        self.pending_upload_size = None
        self.upload_state = None

    def login(self, username: str) -> None:
        self.authenticated = True
        self.username = username

    def logout(self) -> None:
        self.authenticated = False
        self.username = None

    def is_authenticated(self) -> bool:
        return self.authenticated

    def start_download(self, virtual_path):
        self.pending_download = virtual_path

    def finish_download(self):
        self.pending_download = None
    
    def start_upload(self, virtual_path):
        self.pending_upload = virtual_path
        self.upload_state = UPLOAD_WAITING_FOR_SIZE
    
    def finish_upload(self):
        self.pending_upload = None
        self.upload_state = None 

    def set_upload_size(self, size):
        self.pending_upload_size = size

    def begin_receiving_file(self, file_size):
        self.pending_upload_size = file_size
        self.upload_state = UPLOAD_RECEIVING_FILE