from models.bus import Bus


class BusParser:

    def __init__(self, section):

        self.section = section

    def parse(self):

        buses = []

        data = [
            line
            for line in self.section
            if not line.startswith("%")
        ]

        i = 0

        while i < len(data):

            first = data[i].split()

            second = data[i + 1].split()

            bus = Bus(

                bus_id=int(first[0]),

                dummy_no=int(first[1]),

                zone_no=int(first[2]),

                base_voltage=float(first[3]),

                bus_name=first[4],

                voltage=float(first[5]),

                angle=float(first[6]),

                pgen=float(second[0]),

                qgen=float(second[1]),

                pload=float(second[2]),

                qload=float(second[3]),

                qcomp=float(second[4]),

                island_no=int(second[5])

            )

            buses.append(bus)

            i += 2

        return buses