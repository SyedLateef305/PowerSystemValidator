class GeneratorEditor:

    def __init__(self, generators, tracker):

        self.generators = generators
        self.tracker = tracker

    def edit_status(self, bus_no):

        for gen in self.generators:

            if gen.bus_no == bus_no:

                print(f"\nCurrent Status : {gen.status}")

                while True:

                    try:

                        value = int(input("Enter New Status (1/2/3): "))

                        if value not in [1,2,3]:

                            print("Status must be 1,2 or 3.")
                            continue

                        old = gen.status

                        gen.status = value

                        self.tracker.add_change(

                            section="Generator",

                            record=f"Bus {bus_no}",

                            field="Status",

                            old_value=old,

                            new_value=value

                        )

                        print("\n✓ Generator Updated.")

                        return

                    except ValueError:

                        print("Enter integer.")