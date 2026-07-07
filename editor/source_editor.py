class SourceEditor:
    def __init__(self, sources, tracker):
        self.sources = sources
        self.tracker = tracker

    def _get_record(self, index):
        if index < 1 or index > len(self.sources):
            raise ValueError("Invalid source record number.")
        return self.sources[index - 1]

    def edit_area(self, index):
        record = self._get_record(index)
        print(f"Current Area : {record.area}")

        value = int(input("Enter New Area : "))
        old = record.area
        record.area = value

        self.tracker.add_change(
            "Source Details",
            f"Source {index}",
            "Area",
            old,
            value
        )

    def edit_option(self, index):
        record = self._get_record(index)
        print(f"Current Option : {record.option}")

        value = int(input("Enter New Option : "))
        old = record.option
        record.option = value

        self.tracker.add_change(
            "Source Details",
            f"Source {index}",
            "Option",
            old,
            value
        )

    def edit_location(self, index):
        record = self._get_record(index)
        print(f"Current Location : {record.location}")

        value = int(input("Enter New Location : "))
        old = record.location
        record.location = value

        self.tracker.add_change(
            "Source Details",
            f"Source {index}",
            "Location",
            old,
            value
        )

    def edit_load_percent(self, index):
        record = self._get_record(index)
        print(f"Current Load Percent : {record.load_percent}")

        value = int(input("Enter New Load Percent : "))
        old = record.load_percent
        record.load_percent = value

        self.tracker.add_change(
            "Source Details",
            f"Source {index}",
            "Load Percent",
            old,
            value
        )

    def edit_contribution(self, index):
        record = self._get_record(index)
        print(f"Current Contribution : {record.contribution}")

        value = float(input("Enter New Contribution : "))
        old = record.contribution
        record.contribution = value

        self.tracker.add_change(
            "Source Details",
            f"Source {index}",
            "Contribution",
            old,
            value
        )

    def edit_bus_count(self, index):
        """
        Optional helper if you later add a menu item for bus count editing.
        If increased, blank rows are appended with increment 0.0.
        If decreased, extra rows are truncated.
        """
        record = self._get_record(index)
        print(f"Current Bus Count : {record.bus_count}")

        value = int(input("Enter New Bus Count : "))
        if value < 0:
            raise ValueError("Bus count cannot be negative.")

        old = record.bus_count
        record.bus_count = value

        # Resize bus increment list to match new count
        current = len(record.bus_increments)

        if value < current:
            record.bus_increments = record.bus_increments[:value]
        elif value > current:
            from models.source import SourceBusIncrement
            for _ in range(value - current):
                record.bus_increments.append(SourceBusIncrement(bus_number=0, increment=0.0))

        self.tracker.add_change(
            "Source Details",
            f"Source {index}",
            "Bus Count",
            old,
            value
        )

    def edit_bus_increment(self, source_index, bus_row_index):
        """
        Optional helper if you later add menu support for editing the source bus list.
        bus_row_index is 1-based.
        """
        record = self._get_record(source_index)

        if bus_row_index < 1 or bus_row_index > len(record.bus_increments):
            raise ValueError("Invalid source bus increment row number.")

        row = record.bus_increments[bus_row_index - 1]

        print(f"Current Bus Number : {row.bus_number}")
        new_bus = int(input("Enter New Bus Number : "))

        print(f"Current Increment : {row.increment}")
        new_inc = float(input("Enter New Increment : "))

        old_bus = row.bus_number
        old_inc = row.increment

        row.bus_number = new_bus
        row.increment = new_inc

        self.tracker.add_change(
            "Source Details",
            f"Source {source_index} - Bus Row {bus_row_index}",
            "Bus Number",
            old_bus,
            new_bus
        )

        self.tracker.add_change(
            "Source Details",
            f"Source {source_index} - Bus Row {bus_row_index}",
            "Increment",
            old_inc,
            new_inc
        )