class UpdateFile:
    def __init__(
        self,
        reader,
        system,
        buses,
        lines,
        generators,
        island,
        sources=None,
        sinks=None,
    ):
        self.reader = reader
        self.system = system
        self.buses = buses
        self.lines = lines
        self.generators = generators
        self.island = island
        self.sources = sources or []
        self.sinks = sinks or []

    # ----------------------------------------------------------
    # SYSTEM SPECIFICATION
    # ----------------------------------------------------------
    def update_system_specification(self):
        in_section = False
        data_lines = []

        for i, line in enumerate(self.reader.lines):
            text = line.strip()

            if text.startswith("% Common System Specifications"):
                in_section = True
                continue

            if in_section:
                if text.startswith("% Bus Data"):
                    break
                if text and not text.startswith("%"):
                    data_lines.append(i)

        # Expected order:
        # 0 -> first common spec line
        # 1 -> second common spec line
        # 2 -> island count
        # 3 -> zones/print/plot/baseMVA/frequency
        if len(data_lines) < 4:
            return

        self.reader.lines[data_lines[0]] = (
            f"{self.system.max_bus_id} {self.system.total_buses} "
            f"{self.system.total_two_wdg} {self.system.total_three_wdg} "
            f"{self.system.total_lines} {self.system.total_series_reactors} "
            f"{self.system.total_series_capacitors} {self.system.total_bus_couplers} "
            f"{self.system.total_shunt_reactors} {self.system.total_shunt_capacitors} "
            f"{self.system.total_motors}"
        )

        self.reader.lines[data_lines[1]] = (
            f"{self.system.total_generators} {self.system.total_loads} "
            f"{self.system.total_filters} {self.system.total_hvdc}"
        )

        self.reader.lines[data_lines[2]] = f"{self.system.island_count}"

        self.reader.lines[data_lines[3]] = (
            f"{self.system.zones} {self.system.print_option} {self.system.plot_option} "
            f"{self.system.base_mva} {self.system.frequency}"
        )

    # ----------------------------------------------------------
    # BUS DATA
    # ----------------------------------------------------------
    def update_bus_data(self):
        in_bus = False
        bus_index = 0
        i = 0

        while i < len(self.reader.lines):
            text = self.reader.lines[i].strip()

            if text.startswith("% Bus Data"):
                in_bus = True
                i += 1
                continue

            if in_bus and text.startswith("% Transmission Line Data"):
                break

            if not in_bus or text.startswith("%") or not text:
                i += 1
                continue

            if bus_index >= len(self.buses) or i + 1 >= len(self.reader.lines):
                break

            bus = self.buses[bus_index]

            self.reader.lines[i] = (
                f"{bus.bus_id:4d} {bus.dummy_no:1d} {bus.zone_no:2d} "
                f"{bus.base_voltage:7.3f} {bus.bus_name:>8} "
                f"{bus.voltage:.12e} {bus.angle:.12e}"
            )

            self.reader.lines[i + 1] = (
                f"        {bus.pgen:8.2f} {bus.qgen:8.2f} {bus.pload:8.2f} "
                f"{bus.qload:8.2f} {bus.qcomp:6.2f} \t{bus.island_no}"
            )

            bus_index += 1
            i += 2

    # ----------------------------------------------------------
    # LINE DATA
    # ----------------------------------------------------------
    def update_line_data(self):
        in_section = False
        line_index = 0

        for i, line in enumerate(self.reader.lines):
            text = line.strip()

            if text.startswith("% Transmission Line Data"):
                in_section = True
                continue

            if in_section and text.startswith("% Generator Data"):
                break

            if not in_section or not text or text.startswith("%"):
                continue

            if line_index >= len(self.lines):
                break

            ln = self.lines[line_index]

            self.reader.lines[i] = (
                f"{ln.status} {ln.circuits} {ln.from_bus} {ln.to_bus} "
                f"{ln.resistance:.6f} {ln.reactance:.6f} {ln.charging:.6f}"
            )

            line_index += 1

    # ----------------------------------------------------------
    # GENERATOR DATA
    # ----------------------------------------------------------
    def update_generator_data(self):
        in_section = False
        gen_index = 0

        for i, line in enumerate(self.reader.lines):
            text = line.strip()

            if text.startswith("% Generator Data"):
                in_section = True
                continue

            if in_section and text.startswith("%Valid_Island_No"):
                break

            if not in_section or not text or text.startswith("%"):
                continue

            if gen_index >= len(self.generators):
                break

            gen = self.generators[gen_index]

            attrs = vars(gen)
            values = [str(v) for v in attrs.values()]
            self.reader.lines[i] = " ".join(values)

            gen_index += 1

    # ----------------------------------------------------------
    # ISLAND DATA
    # ----------------------------------------------------------
    def update_island_data(self):
        in_section = False
        written = False

        for i, line in enumerate(self.reader.lines):
            text = line.strip()

            if text.startswith("%Valid_Island_No"):
                in_section = True
                continue

            if in_section:
                if text.startswith("%1 0-Area Wise/1-Bus Wise/2-Zone Wise") \
                   or text.startswith("%Source Details") \
                   or text.startswith("%Sink Details"):
                    break

                if text and not text.startswith("%") and not written:
                    attrs = vars(self.island)
                    values = [str(v) for v in attrs.values()]
                    self.reader.lines[i] = " ".join(values)
                    written = True
                    break

    # ----------------------------------------------------------
    # INTERNAL HELPERS FOR SOURCE / SINK BLOCKS
    # ----------------------------------------------------------
    def _find_section_start(self, header):
        for i, line in enumerate(self.reader.lines):
            if line.strip().startswith(header):
                return i
        return -1

    def _collect_data_line_indexes(self, start_idx, stop_headers):
        """
        Collect non-comment, non-blank line indexes after a section header
        until one of the stop headers is reached.
        """
        indexes = []
        i = start_idx + 1

        while i < len(self.reader.lines):
            text = self.reader.lines[i].strip()

            if any(text.startswith(h) for h in stop_headers):
                break

            if text and not text.startswith("%"):
                indexes.append(i)

            i += 1

        return indexes

    def _write_source_or_sink_blocks(self, records, line_indexes):
        """
        Writes records into an existing multi-line Source/Sink block area.

        Each record is written as:
            header line
            count line
            count bus-increment lines

        Existing file must already have enough data lines allocated.
        """
        ptr = 0

        for rec in records:
            if ptr >= len(line_indexes):
                break

            # Header line
            self.reader.lines[line_indexes[ptr]] = (
                f"{rec.area} {rec.option} {rec.load_percent} "
                f"{rec.location} {rec.load_type}"
            )
            ptr += 1

            # Count line
            if ptr >= len(line_indexes):
                break

            bus_count = rec.bus_count if hasattr(rec, "bus_count") else 0
            self.reader.lines[line_indexes[ptr]] = f"{bus_count}"
            ptr += 1

            # Bus increment rows
            bus_rows = getattr(rec, "bus_increments", [])
            for row_index in range(bus_count):
                if ptr >= len(line_indexes):
                    break

                if row_index < len(bus_rows):
                    row = bus_rows[row_index]
                    self.reader.lines[line_indexes[ptr]] = (
                        f"{row.bus_number} {row.increment:.6f}"
                    )
                else:
                    # keep structure valid even if bus_count > actual rows
                    self.reader.lines[line_indexes[ptr]] = "0 0.000000"

                ptr += 1

    # ----------------------------------------------------------
    # SOURCE DETAILS
    # ----------------------------------------------------------
    def update_source_details(self):
        if not self.sources:
            return

        start = self._find_section_start("%Source Details")
        if start == -1:
            return

        # Source section ends when Sink Details begins, or EOF
        line_indexes = self._collect_data_line_indexes(
            start,
            stop_headers=["%Sink Details"]
        )

        self._write_source_or_sink_blocks(self.sources, line_indexes)

    # ----------------------------------------------------------
    # SINK DETAILS
    # ----------------------------------------------------------
    def update_sink_details(self):
        if not self.sinks:
            return

        start = self._find_section_start("%Sink Details")
        if start == -1:
            return

        # Sink section goes until EOF
        line_indexes = self._collect_data_line_indexes(
            start,
            stop_headers=[]
        )

        self._write_source_or_sink_blocks(self.sinks, line_indexes)

    # ----------------------------------------------------------
    # MASTER UPDATE
    # ----------------------------------------------------------
    def update_all(self):
        self.update_system_specification()
        self.update_bus_data()
        self.update_line_data()
        self.update_generator_data()
        self.update_island_data()
        self.update_source_details()
        self.update_sink_details()