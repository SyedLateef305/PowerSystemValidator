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

    def edit_load_type(self, index):
        record = self._get_record(index)
        print(f"Current Load Type : {record.load_type}")

        value = int(input("Enter New Load Type : "))
        old = record.load_type
        record.load_type = value

        self.tracker.add_change(
            "Source Details",
            f"Source {index}",
            "Load Type",
            old,
            value
        )