class GeneratorValidator:

    def __init__(self, generators, buses):

        self.generators = generators
        self.buses = buses
        self.errors = []

    def validate(self):

        self.errors.clear()

        self.check_bus_exists()

        self.check_status()

        self.check_duplicate_generator()

        return self.errors

    # -----------------------------------------
    # Generator Bus Exists
    # -----------------------------------------

    def check_bus_exists(self):

        bus_ids = [bus.bus_id for bus in self.buses]

        for generator in self.generators:

            if generator.bus_no not in bus_ids:

                self.errors.append({

                    "type": "generator_bus",

                    "bus": generator.bus_no,

                    "message": f"Generator Bus {generator.bus_no} does not exist."

                })

    # -----------------------------------------
    # Generator Status
    # -----------------------------------------

    def check_status(self):

        for generator in self.generators:

            if generator.status not in [1, 2, 3]:

                self.errors.append({

                    "type": "generator_status",

                    "bus": generator.bus_no,

                    "message": f"Generator Bus {generator.bus_no} has invalid status."

                })

    # -----------------------------------------
    # Duplicate Generator
    # -----------------------------------------

    def check_duplicate_generator(self):

        visited = set()

        for generator in self.generators:

            if generator.bus_no in visited:

                self.errors.append({

                    "type": "duplicate_generator",

                    "bus": generator.bus_no,

                    "message": f"Duplicate Generator at Bus {generator.bus_no}."

                })

            else:

                visited.add(generator.bus_no)