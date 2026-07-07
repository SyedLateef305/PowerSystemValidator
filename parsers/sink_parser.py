from models.sink import Sink, SinkBusIncrement


class SinkParser:
    """
    Parses Sink Details blocks of the form:

        <area> <option> <load_percent> <location> <load_type>
        <count>
        <bus_number> <increment>
        <bus_number> <increment>
        ...

    Example:
        3 2 1 2 0
        1
        3 0.000000
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

            # Every sink record must start with a 5-field header line
            if len(parts) < 5:
                i += 1
                continue

            try:
                area = int(parts[0])
                option = int(parts[1])
                load_percent = int(parts[2])
                location = int(parts[3])
                load_type = int(parts[4])
            except ValueError:
                i += 1
                continue

            sink = Sink(
                area=area,
                option=option,
                load_percent=load_percent,
                location=location,
                load_type=load_type,
                bus_count=0,
                bus_increments=[],
            )

            i += 1

            # Next line should be the count line
            if i < len(lines):
                count_parts = lines[i].split()
                if len(count_parts) >= 1:
                    try:
                        sink.bus_count = int(count_parts[0])
                        i += 1
                    except ValueError:
                        sink.bus_count = 0

            # Next bus_count lines are bus increment rows
            for _ in range(sink.bus_count):
                if i >= len(lines):
                    break

                inc_parts = lines[i].split()
                if len(inc_parts) >= 2:
                    try:
                        sink.bus_increments.append(
                            SinkBusIncrement(
                                bus_number=int(inc_parts[0]),
                                increment=float(inc_parts[1]),
                            )
                        )
                    except ValueError:
                        pass
                i += 1

            records.append(sink)

        return records