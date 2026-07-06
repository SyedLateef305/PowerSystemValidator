from config import INPUT_FILE

from parsers.file_reader import FileReader
from parsers.section_parser import SectionParser
from parsers.bus_parser import BusParser
from parsers.system_parser import SystemParser
from parsers.line_parser import LineParser
from parsers.generator_parser import GeneratorParser
from parsers.island_parser import IslandParser

from validators.bus_validator import BusValidator
from editor.bus_editor import BusEditor


def main():

    print("=" * 70)
    print("POWER SYSTEM DATA FILE VALIDATOR")
    print("=" * 70)

    # =====================================================
    # Step 1 : Read Input File
    # =====================================================

    reader = FileReader(INPUT_FILE)
    reader.read()
    reader.remove_blank_lines()

    print("\n✓ File loaded successfully.")

    # =====================================================
    # Step 2 : Split File into Sections
    # =====================================================

    section_parser = SectionParser(reader.lines)
    sections = section_parser.parse()

    print("\n✓ Sections identified successfully.\n")

    section_parser.summary()

    # =====================================================
    # Step 3 : Parse System Specification
    # =====================================================

    system = SystemParser(
        sections["system_specifications"]
    ).parse()

    # =====================================================
    # Step 4 : Parse Bus Data
    # =====================================================

    buses = BusParser(
        sections["bus_data"]
    ).parse()

    # =====================================================
    # Step 5 : Validate Bus Data
    # =====================================================

    while True:

        validator = BusValidator(buses)
        errors = validator.validate()

        print("\n" + "=" * 70)
        print("BUS VALIDATION")
        print("=" * 70)

        if len(errors) == 0:
            print("All Bus Records are Valid.")
            break

        print("\nValidation Errors:\n")

        for i, error in enumerate(errors, start=1):
            print(f"{i}. Bus {error['bus_id']} : {error['message']}")

        choice = input("\nFix the first error? (y/n): ")

        if choice.lower() != "y":
            break

        first_error = errors[0]

        editor = BusEditor(buses)

        if first_error["type"] == "voltage":
            editor.edit_voltage(first_error["bus_id"])

        else:
            print("Automatic editing not implemented for this error type.")
            break

    # =====================================================
    # Step 6 : Parse Transmission Lines
    # =====================================================

    lines = LineParser(
        sections["transmission_line_data"]
    ).parse()

    # =====================================================
    # Step 7 : Parse Generator Data
    # =====================================================

    generators = GeneratorParser(
        sections["generator_data"]
    ).parse()

    # =====================================================
    # Step 8 : Parse Island Data
    # =====================================================

    island = IslandParser(
        sections["island_data"]
    ).parse()

    # =====================================================
    # Display Parsed Objects
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


if __name__ == "__main__":
    main()