from validators.system_validator import SystemValidator
from validators.bus_validator import BusValidator
from validators.line_validator import LineValidator
from validators.generator_validator import GeneratorValidator

from editor.system_editor import SystemEditor
from editor.bus_editor import BusEditor
from editor.line_editor import LineEditor
from editor.generator_editor import GeneratorEditor

from editor.edit_menu import EditMenu
from editor.island_editor import IslandEditor


class ValidatorLoop:

    def __init__(self,
                 system,
                 buses,
                 lines,
                 generators,
                 tracker):

        self.system = system
        self.buses = buses
        self.lines = lines
        self.generators = generators
        self.tracker = tracker

    def run(self):

        while True:

            errors = []

            # ---------------------------------
            # Validate Everything
            # ---------------------------------

            errors.extend(
                SystemValidator(self.system).validate()
            )

            errors.extend(
                BusValidator(self.buses).validate()
            )

            errors.extend(
                LineValidator(
                    self.lines,
                    self.buses
                ).validate()
            )

            errors.extend(
                GeneratorValidator(
                    self.generators,
                    self.buses
                ).validate()
            )

            # ---------------------------------
            # Show Validation Result
            # ---------------------------------

            print("\n")
            print("=" * 70)
            print("VALIDATION REPORT")
            print("=" * 70)

            if len(errors) == 0:

                print("✓ No Validation Errors Found.")

                break

            for i, error in enumerate(errors, start=1):

                print(f"{i}. {error['message']}")

            # ---------------------------------
            # Ask User
            # ---------------------------------

            print()

            choice = EditMenu.display(errors)

            if choice == 0:

                break

            selected_error = errors[choice - 1]

            if choice.lower() != "y":

                break

            first = errors[0]

            # ---------------------------------
            # System Editing
            # ---------------------------------

            if selected_error["type"] == "base_mva":

                editor = SystemEditor(
                    self.system,
                    self.tracker
                )

                editor.edit_base_mva()

            elif selected_error["type"] == "frequency":

                editor = SystemEditor(
                    self.system,
                    self.tracker
                )

                editor.edit_frequency()

            # ---------------------------------
            # Bus Editing
            # ---------------------------------

            elif selected_error["type"] == "voltage":

                editor = BusEditor(
                    self.buses,
                    self.tracker
                )

                editor.edit_voltage(
                    selected_error["bus_id"]
                )

            # ---------------------------------
            # Line Editing
            # ---------------------------------

            elif selected_error["type"] == "resistance":

                fb, tb = map(
                    int,
                    selected_error["line"].split("-")
                )

                editor = LineEditor(
                    self.lines,
                    self.tracker
                )

                editor.edit_resistance(
                    fb,
                    tb
                )

            elif selected_error["type"] == "reactance":

                fb, tb = map(
                    int,
                    selected_error["line"].split("-")
                )

                editor = LineEditor(
                    self.lines,
                    self.tracker
                )

                editor.edit_reactance(
                    fb,
                    tb
                )

            # ---------------------------------
            # Generator Editing
            # ---------------------------------

            elif selected_error["type"] == "generator_status":

                editor = GeneratorEditor(
                    self.generators,
                    self.tracker
                )

                editor.edit_status(
                    selected_error["bus"]
                )

            else:

                print()

                print("Automatic editor not available for this error.")

                print(selected_error)

                break