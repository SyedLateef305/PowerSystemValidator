class BusValidator:

    def __init__(self, buses):
        self.buses = buses
        self.errors = []

    def validate(self):
        self.check_duplicate_bus_ids()
        self.check_negative_bus_ids()
        self.check_empty_names()
        self.check_voltage()

        return self.errors

    def check_duplicate_bus_ids(self):

        ids = set()

        for bus in self.buses:

            if bus.bus_id in ids:

                self.errors.append({
                    "type": "duplicate_bus_id",
                    "bus_id": bus.bus_id,
                    "message": "Duplicate Bus ID"
                })

            ids.add(bus.bus_id)

    def check_negative_bus_ids(self):

        for bus in self.buses:

            if bus.bus_id <= 0:

                self.errors.append({
                    "type": "negative_bus_id",
                    "bus_id": bus.bus_id,
                    "message": "Invalid Bus ID"
                })

    def check_empty_names(self):

        for bus in self.buses:

            if bus.bus_name.strip() == "":

                self.errors.append({
                    "type": "empty_name",
                    "bus_id": bus.bus_id,
                    "message": "Bus Name is Empty"
                })

    def check_voltage(self):

        for bus in self.buses:

            if bus.voltage <= 0:

                self.errors.append({
                    "type": "voltage",
                    "bus_id": bus.bus_id,
                    "message": "Invalid Voltage"
                })