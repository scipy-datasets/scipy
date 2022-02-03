import os


def _has_hash(path, expected_hash):
    """Check if the provided path has the expected hash."""
    if not os.path.exists(path):
        return False
    return file_hash(path) == expected_hash

