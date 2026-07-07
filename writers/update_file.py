class UpdateFile:

    def __init__(self, reader, buses):

        self.reader = reader
        self.buses = buses

    def update_bus_data(self):

        bus_index = 0

        for i in range(len(self.reader.lines)):

            line = self.reader.lines[i]

            if line.strip().startswith("%"):
                continue

            if bus_index >= len(self.buses):
                break

            parts = line.split()

            if len(parts) >= 7:

                try:

                    bus_id = int(parts[0])

                except:

                    continue

                bus = self.buses[bus_index]

                line1 = (
                    f"{bus.bus_id:4d} "
                    f"{bus.dummy_no:2d} "
                    f"{bus.zone_no:2d} "
                    f"{bus.base_voltage:8.3f} "
                    f"{bus.bus_name:>8} "
                    f"{bus.voltage:.12e} "
                    f"{bus.angle:.12e}"
                )

                line2 = (
                    f"    "
                    f"{bus.pgen:10.2f}"
                    f"{bus.qgen:10.2f}"
                    f"{bus.pload:10.2f}"
                    f"{bus.qload:10.2f}"
                    f"{bus.qcomp:10.2f}"
                    f"{bus.island_no:6d}"
                )

                self.reader.lines[i] = line1

                self.reader.lines[i + 1] = line2

                bus_index += 1