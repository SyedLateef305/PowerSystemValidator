class IslandEditor:

    def __init__(self, island, tracker):

        self.island = island
        self.tracker = tracker

    def edit_convergence(self):

        print()

        print(f"Current Convergence : {self.island.converged}")

        while True:

            try:

                value = int(input("Enter New Value (0 or 1): "))

                if value not in [0, 1]:

                    print("Must be 0 or 1.")
                    continue

                old = self.island.converged

                self.island.converged = value

                self.tracker.add_change(

                    section="Island",

                    record="Island",

                    field="Convergence",

                    old_value=old,

                    new_value=value

                )

                print("\n✓ Updated Successfully")

                return

            except ValueError:

                print("Enter Integer.")