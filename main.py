from config import INPUT_FILE

from parsers.file_reader import FileReader
from parsers.section_parser import SectionParser
from parsers.system_parser import SystemParser
from parsers.bus_parser import BusParser
from parsers.line_parser import LineParser
from parsers.generator_parser import GeneratorParser
from parsers.island_parser import IslandParser

from validators.system_validator import SystemValidator
from validators.bus_validator import BusValidator
from validators.line_validator import LineValidator
from validators.generator_validator import GeneratorValidator
from validators.island_validator import IslandValidator
from validators.file_validator import FileValidator

from editor.bus_editor import BusEditor
from editor.change_tracker import ChangeTracker
from editor.validator_loop import ValidatorLoop
from editor.system_editor import SystemEditor

from writers.change_logger import ChangeLogger
from writers.file_writer import FileWriter
from writers.update_file import UpdateFile
from writers.report_writer import ReportWriter

from editor.main_menu import MainMenu

def main():

    print("=" * 70)
    print("POWER SYSTEM DATA FILE VALIDATOR")
    print("=" * 70)

    # =====================================================
    # STEP 1 : Read File
    # =====================================================

    reader = FileReader(INPUT_FILE)
    reader.read()
    reader.remove_blank_lines()

    print("\n✓ File loaded successfully.")

    # =====================================================
    # STEP 2 : Split Sections
    # =====================================================

    section_parser = SectionParser(reader.lines)

    sections = section_parser.parse()

    print("\n✓ Sections identified successfully.\n")

    section_parser.summary()

    # =====================================================
    # STEP 3 : Parse Objects
    # =====================================================

    system = SystemParser(
        sections["system_specifications"]
    ).parse()

    buses = BusParser(
        sections["bus_data"]
    ).parse()

    lines = LineParser(
        sections["transmission_line_data"]
    ).parse()

    generators = GeneratorParser(
        sections["generator_data"]
    ).parse()

    island = IslandParser(
        sections["island_data"]
    ).parse()

    # =====================================================
    # STEP 4 : Individual Validations
    # =====================================================

    print("\n" + "=" * 70)
    print("SYSTEM VALIDATION")
    print("=" * 70)

    system_errors = SystemValidator(system).validate()

    if not system_errors:
        print("System Specification is Valid.")
    else:
        for error in system_errors:
            print(error["message"])

    print("\n" + "=" * 70)
    print("TRANSMISSION LINE VALIDATION")
    print("=" * 70)

    line_errors = LineValidator(lines, buses).validate()

    if not line_errors:
        print("All Transmission Lines are Valid.")
    else:
        for error in line_errors:
            print(error["message"])

    print("\n" + "=" * 70)
    print("GENERATOR VALIDATION")
    print("=" * 70)

    generator_errors = GeneratorValidator(
        generators,
        buses
    ).validate()

    if not generator_errors:
        print("All Generators are Valid.")
    else:
        for error in generator_errors:
            print(error["message"])

    print("\n" + "=" * 70)
    print("ISLAND VALIDATION")
    print("=" * 70)

    island_errors = IslandValidator(
        island
    ).validate()

    if not island_errors:
        print("Island Data is Valid.")
    else:
        for error in island_errors:
            print(error["message"])

    # =====================================================
    # STEP 5 : Complete File Validation
    # =====================================================

    validator = FileValidator(
        system,
        buses,
        lines,
        generators,
        island
    )

    errors = validator.validate()

    print("\n" + "=" * 70)
    print("COMPLETE FILE VALIDATION")
    print("=" * 70)

    if not errors:
        print("✓ No validation errors found.")
    else:

        print(f"Total Errors : {len(errors)}\n")

        for i, error in enumerate(errors, start=1):
            print(f"{i}. {error['message']}")

    # =====================================================
    # STEP 6 : Interactive Bus Validation
    # =====================================================

    logger = ChangeLogger()

    while True:

        validator = BusValidator(buses)

        errors = validator.validate()

        print("\n" + "=" * 70)
        print("BUS VALIDATION")
        print("=" * 70)

        if len(errors) == 0:

            print("All Bus Records are Valid.")

            break

        print()

        for i, error in enumerate(errors, start=1):

            print(f"{i}. Bus {error['bus_id']} : {error['message']}")

        choice = input("\nFix first error? (y/n) : ")

        if choice.lower() != "y":

            break

        editor = BusEditor(
            buses,
            logger
        )

        first_error = errors[0]

        if first_error["type"] == "voltage":

            editor.edit_voltage(
                first_error["bus_id"]
            )

        else:

            print("Editor for this validation is not implemented yet.")

            break

    # =====================================================
    # STEP 7 : Validator Loop
    # =====================================================

    tracker = ChangeTracker()

    loop = ValidatorLoop(
        system,
        buses,
        lines,
        generators,
        tracker
    )

    loop.run()

    print("\n")
    tracker.display()

    # =====================================================
    # STEP 8 : Display Parsed Objects
    # =====================================================

    print("\n" + "=" * 70)
    print("SYSTEM SPECIFICATION")
    print("=" * 70)
    print(system)

    print("\n" + "=" * 70)
    print("BUS OBJECTS")
    print("=" * 70)

    for bus in buses:
        print(bus)

    print("\n" + "=" * 70)
    print("TRANSMISSION LINE OBJECTS")
    print("=" * 70)

    for line in lines:
        print(line)

    print("\n" + "=" * 70)
    print("GENERATOR OBJECTS")
    print("=" * 70)

    for generator in generators:
        print(generator)

    print("\n" + "=" * 70)
    print("ISLAND OBJECT")
    print("=" * 70)

    print(island)


    # ============================================
    # MAIN INTERACTIVE MENU
    # ============================================

    while True:

        choice = MainMenu.display()

        # ----------------------------------------
        # BUS EDITOR
        # ----------------------------------------

        if choice == 1:

            print("\n" + "=" * 70)
            print("BUS EDITOR")
            print("=" * 70)

            try:

                bus_id = int(input("Enter Bus ID : "))

                print("\nWhat do you want to edit?")
                print("1. Voltage")
                print("2. Bus Name")
                print("3. Active Power Generation")
                print("4. Reactive Power Generation")
                print("0. Back")

                option = int(input("\nEnter Choice : "))

                bus_editor = BusEditor(
                    buses,
                    tracker
                )

                if option == 1:
                    bus_editor.edit_voltage(bus_id)

                elif option == 2:
                    bus_editor.edit_name(bus_id)

                elif option == 3:
                    bus_editor.edit_pgen(bus_id)

                elif option == 4:
                    bus_editor.edit_qgen(bus_id)

                elif option == 0:
                    continue

                else:
                    print("Invalid Option.")

            except ValueError:

                print("Invalid Input.")

        # ----------------------------------------
        # LINE EDITOR
        # ----------------------------------------

        elif choice == 2:

            print("\nOpening Transmission Line Editor...")

        # ----------------------------------------
        # GENERATOR EDITOR
        # ----------------------------------------

        elif choice == 3:

            print("\nOpening Generator Editor...")

        # ----------------------------------------
        # ISLAND EDITOR
        # ----------------------------------------

        elif choice == 4:

            print("\nOpening Island Editor...")

        # ----------------------------------------
        # SYSTEM EDITOR
        # ----------------------------------------

        elif choice == 5:

            print("\nOpening System Specification Editor...")

            system_editor = SystemEditor(system, tracker)

            print("\nWhat do you want to edit?")
            print("1. Base MVA")
            print("2. Frequency")
            print("3. Maximum Bus ID")
            print("4. Total Buses")
            print("5. Total Transmission Lines")
            print("6. Total Generators")
            print("7. Total Loads")
            print("0. Back")

            try:

                option = int(input("\nEnter Choice : "))

                if option == 1:
                    system_editor.edit_base_mva()

                elif option == 2:
                    system_editor.edit_frequency()

                elif option == 3:
                    system_editor.edit_integer_field(
                        "max_bus_id",
                        "Maximum Bus ID"
                    )

                elif option == 4:
                    system_editor.edit_integer_field(
                        "total_buses",
                        "Total Buses"
                    )

                elif option == 5:
                    system_editor.edit_integer_field(
                        "total_lines",
                        "Total Transmission Lines"
                    )

                elif option == 6:
                    system_editor.edit_integer_field(
                        "total_generators",
                        "Total Generators"
                    )

                elif option == 7:
                    system_editor.edit_integer_field(
                        "total_loads",
                        "Total Loads"
                    )

                elif option == 0:
                    continue

                else:
                    print("Invalid Option.")

            except ValueError:
                print("Invalid Input.")

        # ----------------------------------------
        # SOURCE EDITOR
        # ----------------------------------------

        elif choice == 6:

            print("\nOpening Source Editor...")

        # ----------------------------------------
        # SINK EDITOR
        # ----------------------------------------

        elif choice == 7:

            print("\nOpening Sink Editor...")

        # ----------------------------------------
        # VALIDATE AGAIN
        # ----------------------------------------

        elif choice == 8:

            print("\nRunning Complete Validation...\n")

            validator = FileValidator(
                system,
                buses,
                lines,
                generators,
                island
            )

            errors = validator.validate()

            if len(errors) == 0:

                print("✓ No Validation Errors Found.")

            else:

                print(f"{len(errors)} Validation Errors Found.\n")

                for i, error in enumerate(errors, start=1):

                    print(f"{i}. {error['message']}")

        # ----------------------------------------
        # SAVE
        # ----------------------------------------

        elif choice == 9:

            updater = UpdateFile(
                reader,
                buses
            )

            updater.update_bus_data()

            writer = FileWriter(
                reader.lines
            )

            writer.write(
                "corrected_output.dat"
            )

            logger.save()

            report = ReportWriter(
                tracker
            )

            report.generate()

            print("\n✓ Output File Generated.")
            print("✓ Change Report Generated.")

        # ----------------------------------------
        # EXIT
        # ----------------------------------------

        elif choice == 0:

            print("\nProgram Closed.")

            break

        else:

            print("Invalid Choice.")


if __name__ == "__main__":
    main()