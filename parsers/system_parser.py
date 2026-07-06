from models.system_specification import SystemSpecification


class SystemParser:

    def __init__(self, section):
        self.section = section

    def parse(self):

        rows = []

        for line in self.section:

            if line.startswith("%"):
                continue

            rows.append(line.split())

        first = list(map(int, rows[0]))
        second = list(map(int, rows[1]))

        system = SystemSpecification(

            max_bus_id=first[0],
            total_buses=first[1],
            total_two_wdg=first[2],
            total_three_wdg=first[3],
            total_lines=first[4],

            total_series_reactors=first[5],
            total_series_capacitors=first[6],
            total_bus_couplers=first[7],
            total_shunt_reactors=first[8],
            total_shunt_capacitors=first[9],
            total_motors=first[10],

            total_generators=second[0],
            total_loads=second[1],
            total_filters=second[2],
            total_hvdc=second[3]
        )

        return system