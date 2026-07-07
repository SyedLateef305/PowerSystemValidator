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