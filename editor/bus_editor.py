class BusEditor:
    def __init__(self, buses, tracker):
        self.buses = buses
        self.tracker = tracker

    def _find_bus(self, bus_id):
        for bus in self.buses:
            if bus.bus_id == bus_id:
                return bus
        raise ValueError(f"Bus {bus_id} not found.")

    def _edit_float(self, bus_id, attr, label, allow_zero=True):
        bus = self._find_bus(bus_id)

        print(f"\nCurrent {label} : {getattr(bus, attr)}")

        while True:
            try:
                value = float(input(f"Enter New {label} : "))

                if (allow_zero and value < 0) or (not allow_zero and value <= 0):
                    print(f"{label} is out of range.")
                    continue

                old = getattr(bus, attr)
                setattr(bus, attr, value)

                self.tracker.add_change(
                    "Bus Data",
                    f"Bus {bus_id}",
                    label,
                    old,
                    value
                )

                print(f"\n✓ {label} Updated Successfully.")
                return

            except ValueError:
                print("Enter a valid number.")

    def edit_voltage(self, bus_id):
        self._edit_float(bus_id, "voltage", "Voltage", allow_zero=False)

    def edit_pgen(self, bus_id):
        self._edit_float(bus_id, "pgen", "PGen")

    def edit_qgen(self, bus_id):
        self._edit_float(bus_id, "qgen", "QGen")

    def edit_name(self, bus_id):
        bus = self._find_bus(bus_id)

        print(f"\nCurrent Bus Name : {bus.bus_name}")

        while True:
            value = input("Enter New Bus Name : ").strip()

            if not value:
                print("Bus name cannot be empty.")
                continue

            old = bus.bus_name
            bus.bus_name = value

            self.tracker.add_change(
                "Bus Data",
                f"Bus {bus_id}",
                "Bus Name",
                old,
                value
            )

            print("\n✓ Bus Name Updated Successfully.")
            return