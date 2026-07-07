from models.system_specification import SystemSpecification


class SystemParser:
    def __init__(self, section):
        self.section = section

    def parse(self):
        rows = []

        for line in self.section:
            text = line.strip()
            if not text or text.startswith("%"):
                continue
            rows.append(text.split())

        if len(rows) < 4:
            raise ValueError("System specification section is incomplete.")

        first = list(map(int, rows[0][:11]))
        second = list(map(int, rows[1][:4]))
        island_count = int(rows[2][0])

        third = rows[3]
        zones = int(third[0])
        print_option = int(third[1])
        plot_option = int(third[2])
        base_mva = float(third[3])
        frequency = float(third[4])

        return SystemSpecification(
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
            total_hvdc=second[3],
            island_count=island_count,
            zones=zones,
            print_option=print_option,
            plot_option=plot_option,
            base_mva=base_mva,
            frequency=frequency,
        )