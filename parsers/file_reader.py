from pathlib import Path


class FileReader:

    def __init__(self, filepath):

        self.filepath = Path(filepath)

        self.lines = []

    def read(self):

        if not self.filepath.exists():
            raise FileNotFoundError(f"{self.filepath} not found.")

        with open(self.filepath, "r") as file:

            self.lines = [line.rstrip("\n") for line in file]

        return self.lines

    def remove_blank_lines(self):

        self.lines = [
            line for line in self.lines
            if line.strip()
        ]

        return self.lines