class SectionParser:
    """
    Splits the input file into different logical sections.
    """

    def __init__(self, lines):

        self.lines = lines

        self.sections = {
            "header": [],
            "system_specifications": [],
            "bus_data": [],
            "transmission_line_data": [],
            "generator_data": [],
            "island_data": [],
            "source_details": [],
            "sink_details": []
        }

    def parse(self):

        current_section = "header"

        for line in self.lines:

            text = line.strip()

            # -----------------------------
            # Detect section headers
            # -----------------------------

            if text.startswith("% Common System Specifications"):
                current_section = "system_specifications"

            elif text.startswith("% Bus Data"):
                current_section = "bus_data"

            elif text.startswith("% Transmission Line Data"):
                current_section = "transmission_line_data"

            elif text.startswith("% Generator Data"):
                current_section = "generator_data"

            elif text.startswith("%Valid_Island_No"):
                current_section = "island_data"

            elif text.startswith("%Source Details"):
                current_section = "source_details"

            elif text.startswith("%Sink Details"):
                current_section = "sink_details"

            self.sections[current_section].append(line)

        return self.sections

    def summary(self):

        print("\n" + "=" * 60)
        print("SECTION SUMMARY")
        print("=" * 60)

        for section, lines in self.sections.items():
            print(f"{section:<30} : {len(lines)} lines")

    def display(self, section_name):

        if section_name not in self.sections:
            print("Invalid section name.")
            return

        print("\n" + "=" * 60)
        print(section_name.upper())
        print("=" * 60)

        for line in self.sections[section_name]:
            print(line)