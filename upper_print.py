import sys

class UpperPrint:
    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self.stdout

    def write(self, text):
        self.stdout.write(text.upper())
