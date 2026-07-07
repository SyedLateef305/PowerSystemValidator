from validators.system_validator import SystemValidator
from validators.bus_validator import BusValidator
from validators.line_validator import LineValidator
from validators.generator_validator import GeneratorValidator
from validators.island_validator import IslandValidator


class FileValidator:

    def __init__(self, system, buses, lines, generators, island):

        self.system = system
        self.buses = buses
        self.lines = lines
        self.generators = generators
        self.island = island

    def validate(self):

        all_errors = []

        # ------------------------
        # System Validation
        # ------------------------
        system_errors = SystemValidator(self.system).validate()

        # ------------------------
        # Bus Validation
        # ------------------------
        bus_errors = BusValidator(self.buses).validate()

        # ------------------------
        # Line Validation
        # ------------------------
        line_errors = LineValidator(
            self.lines,
            self.buses
        ).validate()

        # ------------------------
        # Generator Validation
        # ------------------------
        generator_errors = GeneratorValidator(
            self.generators,
            self.buses
        ).validate()

        # ------------------------
        # Island Validation
        # ------------------------
        island_errors = IslandValidator(
            self.island
        ).validate()

        all_errors.extend(system_errors)
        all_errors.extend(bus_errors)
        all_errors.extend(line_errors)
        all_errors.extend(generator_errors)
        all_errors.extend(island_errors)

        return all_errors