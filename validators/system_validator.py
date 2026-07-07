class SystemValidator:

    def __init__(self, system):

        self.system = system
        self.errors = []

    def validate(self):

        self.errors.clear()

        self.check_max_bus_id()

        self.check_total_buses()

        self.check_total_lines()

        self.check_total_generators()

        self.check_total_loads()

        self.check_base_mva()

        self.check_frequency()

        return self.errors

    # ---------------------------------
    # Max Bus ID
    # ---------------------------------

    def check_max_bus_id(self):

        if self.system.max_bus_id <= 0:

            self.errors.append({

                "type": "max_bus_id",

                "message": "Max Bus ID must be greater than zero."

            })

    # ---------------------------------
    # Total Buses
    # ---------------------------------

    def check_total_buses(self):

        if self.system.total_buses <= 0:

            self.errors.append({

                "type": "total_buses",

                "message": "Total Buses must be greater than zero."

            })

    # ---------------------------------
    # Total Lines
    # ---------------------------------

    def check_total_lines(self):

        if self.system.total_lines < 0:

            self.errors.append({

                "type": "total_lines",

                "message": "Total Lines cannot be negative."

            })

    # ---------------------------------
    # Total Generators
    # ---------------------------------

    def check_total_generators(self):

        if self.system.total_generators < 0:

            self.errors.append({

                "type": "total_generators",

                "message": "Total Generators cannot be negative."

            })

    # ---------------------------------
    # Total Loads
    # ---------------------------------

    def check_total_loads(self):

        if self.system.total_loads < 0:

            self.errors.append({

                "type": "total_loads",

                "message": "Total Loads cannot be negative."

            })

    # ---------------------------------
    # Base MVA
    # ---------------------------------

    def check_base_mva(self):

        if hasattr(self.system, "base_mva"):

            if self.system.base_mva <= 0:

                self.errors.append({

                    "type": "base_mva",

                    "message": "Base MVA must be greater than zero."

                })

    # ---------------------------------
    # Frequency
    # ---------------------------------

    def check_frequency(self):

        if hasattr(self.system, "frequency"):

            if self.system.frequency not in [50, 50.0, 60, 60.0]:

                self.errors.append({

                    "type": "frequency",

                    "message": "Frequency should be either 50 Hz or 60 Hz."

                })