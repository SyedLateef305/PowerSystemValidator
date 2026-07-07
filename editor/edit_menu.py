class EditMenu:

    @staticmethod
    def display(errors):

        print()
        print("=" * 70)
        print("VALIDATION ERRORS")
        print("=" * 70)

        for i, error in enumerate(errors, start=1):

            print(f"{i}. {error['message']}")

        print("\n0. Exit")

        while True:

            try:

                choice = int(input("\nSelect Error Number: "))

                if 0 <= choice <= len(errors):

                    return choice

                print("Invalid Choice.")

            except ValueError:

                print("Enter a valid number.")