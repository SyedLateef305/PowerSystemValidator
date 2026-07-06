from models.generator import Generator


class GeneratorParser:

    def __init__(self, section):
        self.section = section

    def parse(self):

        generators = []

        for row in self.section:

            if row.startswith("%"):
                continue

            x = row.split()

            generator = Generator(

                bus_no=int(x[0]),
                status=int(x[1])

            )

            generators.append(generator)

        return generators