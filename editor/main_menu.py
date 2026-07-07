class MainMenu:
    @staticmethod
    def display():
        print("\n" + "=" * 70)
        print("POWER SYSTEM EDIT MENU")
        print("=" * 70)
        print("1. Edit Bus Data")
        print("2. Edit Transmission Line")
        print("3. Edit Generator")
        print("4. Edit Island")
        print("5. Edit System Specification")
        print("6. Edit Source Details")
        print("7. Edit Sink Details")
        print("8. Validate Entire File")
        print("9. Save Corrected File")
        print("0. Exit")

        while True:
            try:
                return int(input("\nEnter Choice : ").strip())
            except ValueError:
                print("Please enter a valid number.")