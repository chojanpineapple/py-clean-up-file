import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type: str = None, exc_value: str = None, traceback: str = None) -> None:
        if os.exist(self.filename):
            os.remove(self.filename)
        return False
