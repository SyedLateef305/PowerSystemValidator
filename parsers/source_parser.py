from models.source import Source, SourceBusIncrement


class SourceParser:
    """
    Parses Source Details blocks of the form:

        <area> <option> <location> <load_percent> <contribution>
        <count>
        <bus_number> <increment>
        <bus_number> <increment>
        ...

    Example:
        3 1 2 1 100.0
        2
        1 50.0
        2 50.0
    """

    def __init__(self, section):
        self.section = section

    def _clean_lines(self):
        cleaned = []
        for line in self.section:
            text = line.strip()
            if not text or text.startswith("%"):
                continue
            cleaned.append(text)
        return cleaned

    def parse(self):
        records = []
        lines = self._clean_lines()
        i = 0

        while i < len(lines):
            parts = lines[i].split()

            # Every source record must start with a 5-field header line
            if len(parts) < 5:
                i += 1
                continue

            try:
                area = int(parts[0])
                option = int(parts[1])
                location = int(parts[2])
                load_percent = int(parts[3])
                contribution = float(parts[4])
            except ValueError:
                i += 1
                continue

            source = Source(
                area=area,
                option=option,
                location=location,
                load_percent=load_percent,
                contribution=contribution,
                bus_count=0,
                bus_increments=[],
            )

            i += 1

            # Next line should be the count line
            if i < len(lines):
                count_parts = lines[i].split()
                if len(count_parts) >= 1:
                    try:
                        source.bus_count = int(count_parts[0])
                        i += 1
                    except ValueError:
                        source.bus_count = 0

            # Next bus_count lines are bus increment rows
            for _ in range(source.bus_count):
                if i >= len(lines):
                    break

                inc_parts = lines[i].split()
                if len(inc_parts) >= 2:
                    try:
                        source.bus_increments.append(
                            SourceBusIncrement(
                                bus_number=int(inc_parts[0]),
                                increment=float(inc_parts[1]),
                            )
                        )
                    except ValueError:
                        pass
                i += 1

            records.append(source)

        return records