from datetime import datetime


class ChangeTracker:

    def __init__(self):

        self.changes = []

    def add_change(self,
                   section,
                   record,
                   field,
                   old_value,
                   new_value):

        self.changes.append({

            "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),

            "section": section,

            "record": record,

            "field": field,

            "old": old_value,

            "new": new_value

        })

    def display(self):

        print("\n")
        print("=" * 70)
        print("CHANGE HISTORY")
        print("=" * 70)

        if len(self.changes) == 0:

            print("No Changes Made.")

            return

        for i, change in enumerate(self.changes, start=1):

            print(f"\nChange {i}")

            print(f"Time    : {change['time']}")

            print(f"Section : {change['section']}")

            print(f"Record  : {change['record']}")

            print(f"Field   : {change['field']}")

            print(f"Old     : {change['old']}")

            print(f"New     : {change['new']}")