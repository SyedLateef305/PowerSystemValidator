from validators.file_validator import FileValidator
from editor.edit_menu import EditMenu
from editor.system_editor import SystemEditor
from editor.bus_editor import BusEditor
from editor.line_editor import LineEditor
from editor.generator_editor import GeneratorEditor
from editor.island_editor import IslandEditor


class ValidatorLoop:
    def __init__(self, system, buses, lines, generators, island, tracker):
        self.system = system
        self.buses = buses
        self.lines = lines
        self.generators = generators
        self.island = island
        self.tracker = tracker

    def run(self):
        while True:
            errors = FileValidator(
                self.system,
                self.buses,
                self.lines,
                self.generators,
                self.island
            ).validate()

            print("\n" + "=" * 70)
            print("VALIDATION REPORT")
            print("=" * 70)

            if not errors:
                print("✓ No Validation Errors Found.")
                return

            choice = EditMenu.display(errors)

            if choice == 0:
                return

            err = errors[choice - 1]
            error_type = err["type"]

            if error_type == "voltage":
                BusEditor(self.buses, self.tracker).edit_voltage(err["bus_id"])

            elif error_type == "empty_name":
                BusEditor(self.buses, self.tracker).edit_name(err["bus_id"])

            elif error_type == "resistance":
                fb, tb = map(int, err["line"].split("-"))
                LineEditor(self.lines, self.tracker).edit_resistance(fb, tb)

            elif error_type == "reactance":
                fb, tb = map(int, err["line"].split("-"))
                LineEditor(self.lines, self.tracker).edit_reactance(fb, tb)

            elif error_type == "generator_status":
                GeneratorEditor(self.generators, self.tracker).edit_status(err["bus"])

            elif error_type == "convergence":
                IslandEditor(self.island, self.tracker).edit_convergence()

            elif error_type in {
                "max_bus_id",
                "total_buses",
                "total_lines",
                "total_generators",
                "total_loads"
            }:
                field_map = {
                    "max_bus_id": "Maximum Bus ID",
                    "total_buses": "Total Buses",
                    "total_lines": "Total Transmission Lines",
                    "total_generators": "Total Generators",
                    "total_loads": "Total Loads",
                }
                SystemEditor(self.system, self.tracker).edit_integer_field(
                    error_type,
                    field_map[error_type]
                )

            elif error_type in {"base_mva", "frequency"}:
                editor = SystemEditor(self.system, self.tracker)
                getattr(editor, f"edit_{error_type}")()

            else:
                print(f"Automatic editor not available for: {err['message']}")
                return