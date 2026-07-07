class LineValidator:

    def __init__(self, lines, buses):

        self.lines = lines
        self.buses = buses
        self.errors = []

    def validate(self):

        self.errors.clear()

        self.check_status()

        self.check_circuits()

        self.check_bus_numbers()

        self.check_same_bus()

        self.check_resistance()

        self.check_reactance()

        self.check_charging()

        self.check_duplicate_lines()

        return self.errors

    # ----------------------------------------
    # Valid Status
    # ----------------------------------------

    def check_status(self):

        for line in self.lines:

            if line.status not in [1, 2, 3]:

                self.errors.append({

                    "type": "status",

                    "line": f"{line.from_bus}-{line.to_bus}",

                    "message": "Invalid Line Status"

                })

    # ----------------------------------------
    # Number of Circuits
    # ----------------------------------------

    def check_circuits(self):

        for line in self.lines:

            if line.circuits <= 0:

                self.errors.append({

                    "type": "circuits",

                    "line": f"{line.from_bus}-{line.to_bus}",

                    "message": "Number of circuits must be greater than zero."

                })

    # ----------------------------------------
    # Bus Numbers
    # ----------------------------------------

    def check_bus_numbers(self):

        bus_ids = [bus.bus_id for bus in self.buses]

        for line in self.lines:

            if line.from_bus not in bus_ids:

                self.errors.append({

                    "type": "from_bus",

                    "line": f"{line.from_bus}-{line.to_bus}",

                    "message": f"From Bus {line.from_bus} does not exist."

                })

            if line.to_bus not in bus_ids:

                self.errors.append({

                    "type": "to_bus",

                    "line": f"{line.from_bus}-{line.to_bus}",

                    "message": f"To Bus {line.to_bus} does not exist."

                })

    # ----------------------------------------
    # Same Bus
    # ----------------------------------------

    def check_same_bus(self):

        for line in self.lines:

            if line.from_bus == line.to_bus:

                self.errors.append({

                    "type": "same_bus",

                    "line": f"{line.from_bus}-{line.to_bus}",

                    "message": "From Bus and To Bus cannot be same."

                })

    # ----------------------------------------
    # Resistance
    # ----------------------------------------

    def check_resistance(self):

        for line in self.lines:

            if line.resistance < 0:

                self.errors.append({

                    "type": "resistance",

                    "line": f"{line.from_bus}-{line.to_bus}",

                    "message": "Resistance cannot be negative."

                })

    # ----------------------------------------
    # Reactance
    # ----------------------------------------

    def check_reactance(self):

        for line in self.lines:

            if line.reactance <= 0:

                self.errors.append({

                    "type": "reactance",

                    "line": f"{line.from_bus}-{line.to_bus}",

                    "message": "Reactance must be greater than zero."

                })

    # ----------------------------------------
    # Charging
    # ----------------------------------------

    def check_charging(self):

        for line in self.lines:

            if line.charging < 0:

                self.errors.append({

                    "type": "charging",

                    "line": f"{line.from_bus}-{line.to_bus}",

                    "message": "Charging cannot be negative."

                })

    # ----------------------------------------
    # Duplicate Lines
    # ----------------------------------------

    def check_duplicate_lines(self):

        visited = set()

        for line in self.lines:

            key = tuple(sorted((line.from_bus, line.to_bus)))

            if key in visited:

                self.errors.append({

                    "type": "duplicate",

                    "line": f"{line.from_bus}-{line.to_bus}",

                    "message": "Duplicate transmission line."

                })

            else:

                visited.add(key)