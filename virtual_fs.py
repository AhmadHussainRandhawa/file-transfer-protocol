from config import STORAGE_ROOT
from pathlib import Path

class VirtualFileSystem:
    
    def __init__(self):
        self.root = STORAGE_ROOT

    def get_real_path(self, virtual_path: Path) -> Path: 
        """
        Convert a virtual path into a real filesystem path
        while ensuring it remains inside STORAGE_ROOT.
        """
        real_path = (self.root / virtual_path.relative_to("/")).resolve()

        try:
            real_path.relative_to(self.root)
        except ValueError:
            raise("Access outside storage is not allowed.")
        
        return real_path
