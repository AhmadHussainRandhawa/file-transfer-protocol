class VirtualFileSystemError(Exception):
    """Base exception for the Virtual File System."""


class PathTraversalError(VirtualFileSystemError):
    """Raised when a path escapes the storage root."""


class DirectoryNotFoundError(VirtualFileSystemError):
    """Raised when a directory does not exist."""
