class LineEditor:

    def __init__(self, lines, tracker):

        self.lines = lines
        self.tracker = tracker

    def edit_resistance(self, from_bus, to_bus):

        for line in self.lines:

            if line.from_bus == from_bus and line.to_bus == to_bus:

                print(f"\nCurrent Resistance : {line.resistance}")

                while True:

                    try:

                        value = float(input("Enter New Resistance : "))

                        if value < 0:

                            print("Resistance cannot be negative.")
                            continue

                        old = line.resistance

                        line.resistance = value

                        self.tracker.add_change(

                            section="Transmission Line",

                            record=f"{from_bus}-{to_bus}",

                            field="Resistance",

                            old_value=old,

                            new_value=value

                        )

                        print("\n✓ Resistance Updated.")

                        return

                    except ValueError:

                        print("Enter a valid number.")

    def edit_reactance(self, from_bus, to_bus):

        for line in self.lines:

            if line.from_bus == from_bus and line.to_bus == to_bus:

                print(f"\nCurrent Reactance : {line.reactance}")

                while True:

                    try:

                        value = float(input("Enter New Reactance : "))

                        if value <= 0:

                            print("Reactance must be greater than zero.")
                            continue

                        old = line.reactance

                        line.reactance = value

                        self.tracker.add_change(

                            section="Transmission Line",

                            record=f"{from_bus}-{to_bus}",

                            field="Reactance",

                            old_value=old,

                            new_value=value

                        )

                        print("\n✓ Reactance Updated.")

                        return

                    except ValueError:

                        print("Enter a valid number.")