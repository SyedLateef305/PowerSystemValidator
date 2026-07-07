import os


class FileWriter:

    def __init__(self, lines):

        self.lines = lines

    def write(self, filename):

        os.makedirs("output", exist_ok=True)

        path = os.path.join("output", filename)

        with open(path, "w") as file:

            for line in self.lines:

                file.write(line.rstrip() + "\n")

        print()

        print("=" * 70)
        print("OUTPUT FILE SAVED")
        print("=" * 70)

        print(path)