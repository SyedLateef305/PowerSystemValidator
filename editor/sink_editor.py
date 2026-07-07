class SinkEditor:
    def __init__(self, sinks, tracker):
        self.sinks = sinks
        self.tracker = tracker

    def _get_record(self, index):
        if index < 1 or index > len(self.sinks):
            raise ValueError("Invalid sink record number.")
        return self.sinks[index - 1]

    def edit_area(self, index):
        record = self._get_record(index)
        print(f"Current Area : {record.area}")

        value = int(input("Enter New Area : "))
        old = record.area
        record.area = value

        self.tracker.add_change(
            "Sink Details",
            f"Sink {index}",
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
            "Sink Details",
            f"Sink {index}",
            "Option",
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
            "Sink Details",
            f"Sink {index}",
            "Load Percent",
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
            "Sink Details",
            f"Sink {index}",
            "Location",
            old,
            value
        )

    def edit_load_type(self, index):
        record = self._get_record(index)
        print(f"Current Load Type : {record.load_type}")

        value = int(input("Enter New Load Type : "))
        old = record.load_type
        record.load_type = value

        self.tracker.add_change(
            "Sink Details",
            f"Sink {index}",
            "Load Type",
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
            from models.sink import SinkBusIncrement
            for _ in range(value - current):
                record.bus_increments.append(SinkBusIncrement(bus_number=0, increment=0.0))

        self.tracker.add_change(
            "Sink Details",
            f"Sink {index}",
            "Bus Count",
            old,
            value
        )

    def edit_bus_increment(self, sink_index, bus_row_index):
        """
        Optional helper if you later add menu support for editing the sink bus list.
        bus_row_index is 1-based.
        """
        record = self._get_record(sink_index)

        if bus_row_index < 1 or bus_row_index > len(record.bus_increments):
            raise ValueError("Invalid sink bus increment row number.")

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
            "Sink Details",
            f"Sink {sink_index} - Bus Row {bus_row_index}",
            "Bus Number",
            old_bus,
            new_bus
        )

        self.tracker.add_change(
            "Sink Details",
            f"Sink {sink_index} - Bus Row {bus_row_index}",
            "Increment",
            old_inc,
            new_inc
        )