from config import STORAGE_ROOT
from pathlib import Path
from exceptions import PathTraversalError, DirectoryNotFoundError


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
            raise PathTraversalError("Access outside storage is not allowed.")
        
        return real_path


    def resolve_virtual_path(self, current_directory, target: str,) -> Path:
        """
        Resolve a client-supplied path into a normalized
        virtual path.
        """

        target_path = Path(target)

        if target_path.is_absolute():
            virtual_path = target_path
        else:
            virtual_path = current_directory / target_path

        parts = []

        for part in virtual_path.parts:
            if part == "" or part == ".":
                continue            # Ignore, and move on to the next iteration

            if part == "..":
                if parts:
                    parts.pop()
                continue

            parts.append(part)

        return Path("/") / Path(*parts)

    
    def directory_exists(self, virtual_path: Path) -> bool:
        """
        Return True if the virtual directory exists.
        """
        real_path = self.get_real_path(virtual_path)

        if not real_path.is_dir():
            raise DirectoryNotFoundError(f"Directory '{virtual_path}' does not exist.")

        return True


    def list_directory(self, virtual_path) -> list[str]:
        real_path = self.get_real_path(virtual_path)

        entries = []

        for entry in real_path.iterdir():
            if entry.is_dir():
                entries.append(f"/{entry.name}")
            else:
                entries.append(entry.name)

        return sorted(entries)
        