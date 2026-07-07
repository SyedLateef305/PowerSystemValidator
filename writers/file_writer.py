from config import OUTPUT_FOLDER


class FileWriter:
    def __init__(self, lines):
        self.lines = lines

    def write(self, filename):
        OUTPUT_FOLDER.mkdir(exist_ok=True)

        path = OUTPUT_FOLDER / filename

        with open(path, "w") as f:
            for line in self.lines:
                f.write(line.rstrip() + "\n")

        print(f"\nOutput file saved to: {path}")
        return path