from config import INPUT_FILE

from parsers.file_reader import FileReader
from parsers.section_parser import SectionParser
from parsers.system_parser import SystemParser
from parsers.bus_parser import BusParser
from parsers.line_parser import LineParser
from parsers.generator_parser import GeneratorParser
from parsers.island_parser import IslandParser
from parsers.source_parser import SourceParser
from parsers.sink_parser import SinkParser

from validators.file_validator import FileValidator

from editor.change_tracker import ChangeTracker
from editor.validator_loop import ValidatorLoop
from editor.bus_editor import BusEditor
from editor.system_editor import SystemEditor
from editor.line_editor import LineEditor
from editor.generator_editor import GeneratorEditor
from editor.island_editor import IslandEditor
from editor.source_editor import SourceEditor
from editor.sink_editor import SinkEditor
from editor.main_menu import MainMenu

from writers.update_file import UpdateFile
from writers.file_writer import FileWriter
from writers.report_writer import ReportWriter


def load_project_data():
    reader = FileReader(INPUT_FILE)
    reader.read()
    reader.remove_blank_lines()

    sections = SectionParser(reader.lines).parse()

    system = SystemParser(sections["system_specifications"]).parse()
    buses = BusParser(sections["bus_data"]).parse()
    lines = LineParser(sections["transmission_line_data"]).parse()
    generators = GeneratorParser(sections["generator_data"]).parse()
    island = IslandParser(sections["island_data"]).parse()
    sources = SourceParser(sections["source_details"]).parse()
    sinks = SinkParser(sections["sink_details"]).parse()

    return reader, system, buses, lines, generators, island, sources, sinks


def print_validation(system, buses, lines, generators, island):
    errors = FileValidator(system, buses, lines, generators, island).validate()

    print("\n" + "=" * 70)
    print("COMPLETE FILE VALIDATION")
    print("=" * 70)

    if not errors:
        print("✓ No validation errors found.")
    else:
        print(f"Total Errors : {len(errors)}\n")
        for i, e in enumerate(errors, 1):
            print(f"{i}. {e['message']}")

    return errors


def main():
    print("=" * 70)
    print("POWER SYSTEM DATA FILE VALIDATOR")
    print("=" * 70)

    reader, system, buses, lines, generators, island, sources, sinks = load_project_data()
    tracker = ChangeTracker()

    print_validation(system, buses, lines, generators, island)

    while True:
        choice = MainMenu.display()

        # --------------------------------------------------
        # BUS EDITOR
        # --------------------------------------------------
        if choice == 1:
            bus_id = int(input("Enter Bus ID : "))

            print("1. Voltage")
            print("2. Bus Name")
            print("3. Active Power Generation")
            print("4. Reactive Power Generation")
            print("0. Back")

            option = int(input("Enter Choice : "))
            editor = BusEditor(buses, tracker)

            if option == 1:
                editor.edit_voltage(bus_id)
            elif option == 2:
                editor.edit_name(bus_id)
            elif option == 3:
                editor.edit_pgen(bus_id)
            elif option == 4:
                editor.edit_qgen(bus_id)

        # --------------------------------------------------
        # LINE EDITOR
        # --------------------------------------------------
        elif choice == 2:
            from_bus = int(input("Enter From Bus : "))
            to_bus = int(input("Enter To Bus : "))

            print("1. Resistance")
            print("2. Reactance")
            print("0. Back")

            option = int(input("Enter Choice : "))
            editor = LineEditor(lines, tracker)

            if option == 1:
                editor.edit_resistance(from_bus, to_bus)
            elif option == 2:
                editor.edit_reactance(from_bus, to_bus)

        # --------------------------------------------------
        # GENERATOR EDITOR
        # --------------------------------------------------
        elif choice == 3:
            bus_id = int(input("Enter Generator Bus ID : "))

            print("1. Status")
            print("0. Back")

            option = int(input("Enter Choice : "))
            editor = GeneratorEditor(generators, tracker)

            if option == 1:
                editor.edit_status(bus_id)

        # --------------------------------------------------
        # ISLAND EDITOR
        # --------------------------------------------------
        elif choice == 4:
            print("1. Convergence")
            print("0. Back")

            option = int(input("Enter Choice : "))
            editor = IslandEditor(island, tracker)

            if option == 1:
                editor.edit_convergence()

        # --------------------------------------------------
        # SYSTEM EDITOR
        # --------------------------------------------------
        elif choice == 5:
            editor = SystemEditor(system, tracker)

            print("1. Base MVA")
            print("2. Frequency")
            print("3. Maximum Bus ID")
            print("4. Total Buses")
            print("5. Total Transmission Lines")
            print("6. Total Generators")
            print("7. Total Loads")
            print("0. Back")

            option = int(input("Enter Choice : "))

            if option == 1:
                editor.edit_base_mva()
            elif option == 2:
                editor.edit_frequency()
            elif option == 3:
                editor.edit_integer_field("max_bus_id", "Maximum Bus ID")
            elif option == 4:
                editor.edit_integer_field("total_buses", "Total Buses")
            elif option == 5:
                editor.edit_integer_field("total_lines", "Total Transmission Lines")
            elif option == 6:
                editor.edit_integer_field("total_generators", "Total Generators")
            elif option == 7:
                editor.edit_integer_field("total_loads", "Total Loads")

        # --------------------------------------------------
        # SOURCE EDITOR
        # --------------------------------------------------
        elif choice == 6:
            if not sources:
                print("No source records found.")
                continue

            index = int(input(f"Enter Source Record Number (1-{len(sources)}) : "))

            print("1. Area")
            print("2. Option")
            print("3. Load Percent")
            print("4. Location")
            print("5. Load Type")
            print("0. Back")

            option = int(input("Enter Choice : "))
            editor = SourceEditor(sources, tracker)

            if option == 1:
                editor.edit_area(index)
            elif option == 2:
                editor.edit_option(index)
            elif option == 3:
                editor.edit_load_percent(index)
            elif option == 4:
                editor.edit_location(index)
            elif option == 5:
                editor.edit_load_type(index)

        # --------------------------------------------------
        # SINK EDITOR
        # --------------------------------------------------
        elif choice == 7:
            if not sinks:
                print("No sink records found.")
                continue

            index = int(input(f"Enter Sink Record Number (1-{len(sinks)}) : "))

            print("1. Area")
            print("2. Option")
            print("3. Load Percent")
            print("4. Location")
            print("5. Load Type")
            print("0. Back")

            option = int(input("Enter Choice : "))
            editor = SinkEditor(sinks, tracker)

            if option == 1:
                editor.edit_area(index)
            elif option == 2:
                editor.edit_option(index)
            elif option == 3:
                editor.edit_load_percent(index)
            elif option == 4:
                editor.edit_location(index)
            elif option == 5:
                editor.edit_load_type(index)

        # --------------------------------------------------
        # VALIDATE
        # --------------------------------------------------
        elif choice == 8:
            ValidatorLoop(
                system,
                buses,
                lines,
                generators,
                island,
                tracker
            ).run()

        # --------------------------------------------------
        # SAVE
        # --------------------------------------------------
        elif choice == 9:
            updater = UpdateFile(
                reader,
                system,
                buses,
                lines,
                generators,
                island,
                sources,
                sinks
            )
            updater.update_all()

            FileWriter(reader.lines).write("corrected_output.dat")
            ReportWriter(tracker).generate()
            print("✓ Output file generated.")

        # --------------------------------------------------
        # EXIT
        # --------------------------------------------------
        elif choice == 0:
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()