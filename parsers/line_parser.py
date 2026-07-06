from models.transmission_line import TransmissionLine


class LineParser:

    def __init__(self, section):
        self.section = section

    def parse(self):

        lines = []

        for row in self.section:

            if row.startswith("%"):
                continue

            x = row.split()

            line = TransmissionLine(

                status=int(x[0]),
                circuits=int(x[1]),
                from_bus=int(x[2]),
                to_bus=int(x[3]),
                resistance=float(x[4]),
                reactance=float(x[5]),
                charging=float(x[6])

            )

            lines.append(line)

        return lines