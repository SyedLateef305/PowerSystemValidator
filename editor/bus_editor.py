class BusEditor:

    def __init__(self, buses, tracker):

        self.buses = buses

        self.tracker = tracker

    def edit_voltage(self, bus_id):

        for bus in self.buses:

            if bus.bus_id == bus_id:

                print()

                print(f"Current Voltage : {bus.voltage}")

                while True:

                    try:

                        value = float(

                            input("Enter New Voltage : ")

                        )

                        if value <= 0:

                            print("Voltage must be greater than zero.")

                            continue

                        old = bus.voltage

                        bus.voltage = value

                        self.tracker.add_change(

                            section="Bus Data",

                            record=f"Bus {bus_id}",

                            field="Voltage",

                            old_value=old,

                            new_value=value

                        )

                        print()

                        print("✓ Voltage Updated Successfully.")

                        return

                    except ValueError:

                        print("Enter a valid number.")