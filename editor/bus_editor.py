class BusEditor:

    def __init__(self, buses):
        self.buses = buses

    def edit_voltage(self, bus_id):

        for bus in self.buses:

            if bus.bus_id == bus_id:

                print("\n")
                print("=" * 60)
                print("EDIT BUS VOLTAGE")
                print("=" * 60)

                print(f"Bus ID      : {bus.bus_id}")
                print(f"Bus Name    : {bus.bus_name}")
                print(f"Old Voltage : {bus.voltage}")

                while True:

                    try:

                        value = float(
                            input("Enter New Voltage : ")
                        )

                        if value <= 0:
                            print("Voltage must be greater than 0.")
                            continue

                        bus.voltage = value

                        print("\nVoltage Updated Successfully.")

                        return

                    except ValueError:

                        print("Enter a valid number.")