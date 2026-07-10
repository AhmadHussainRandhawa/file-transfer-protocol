from config import STORAGE_ROOT
from pathlib import Path

class VirtualFileSystem:
    
    def __init__(self):
        self.root = STORAGE_ROOT

    def get_real_path(self, virtual_path: Path) -> Path: 
        return self.root / virtual_path.relative_to("/")