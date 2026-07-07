class SystemEditor:

    def __init__(self, system, tracker):

        self.system = system
        self.tracker = tracker

    # -------------------------------------------------
    # Generic Integer Editor
    # -------------------------------------------------

    def edit_integer_field(self, field_name, display_name):

        current = getattr(self.system, field_name)

        print(f"\nCurrent {display_name} : {current}")

        while True:

            try:

                value = int(input(f"Enter New {display_name} : "))

                if value < 0:

                    print("Value cannot be negative.")
                    continue

                setattr(self.system, field_name, value)

                self.tracker.add_change(

                    section="System Specification",

                    record="System",

                    field=display_name,

                    old_value=current,

                    new_value=value

                )

                print(f"\n✓ {display_name} Updated.")

                return

            except ValueError:

                print("Enter valid integer.")

    # -------------------------------------------------
    # Base MVA
    # -------------------------------------------------

    def edit_base_mva(self):

        print(f"\nCurrent Base MVA : {self.system.base_mva}")

        while True:

            try:

                value = float(input("Enter New Base MVA : "))

                if value <= 0:

                    print("Must be greater than zero.")
                    continue

                old = self.system.base_mva

                self.system.base_mva = value

                self.tracker.add_change(

                    section="System Specification",

                    record="System",

                    field="Base MVA",

                    old_value=old,

                    new_value=value

                )

                print("\n✓ Base MVA Updated.")

                return

            except ValueError:

                print("Enter valid number.")

    # -------------------------------------------------
    # Frequency
    # -------------------------------------------------

    def edit_frequency(self):

        print(f"\nCurrent Frequency : {self.system.frequency}")

        while True:

            try:

                value = float(input("Enter Frequency (50/60): "))

                if value not in [50, 60]:

                    print("Frequency should be 50 or 60.")
                    continue

                old = self.system.frequency

                self.system.frequency = value

                self.tracker.add_change(

                    section="System Specification",

                    record="System",

                    field="Frequency",

                    old_value=old,

                    new_value=value

                )

                print("\n✓ Frequency Updated.")

                return

            except ValueError:

                print("Enter valid number.")