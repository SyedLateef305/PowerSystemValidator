from models.sink import Sink


class SinkParser:
    def __init__(self, section):
        self.section = section

    def parse(self):
        records = []

        for line in self.section:
            text = line.strip()

            if not text or text.startswith("%"):
                continue

            parts = text.split()
            if len(parts) < 5:
                continue

            records.append(
                Sink(
                    area=int(parts[0]),
                    option=int(parts[1]),
                    load_percent=int(parts[2]),
                    location=int(parts[3]),
                    load_type=int(parts[4]),
                )
            )

        return records