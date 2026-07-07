import os
from datetime import datetime


class ChangeLogger:

    def __init__(self):

        self.changes = []

    def add_change(self, section, record, field, old_value, new_value):

        self.changes.append({

            "section": section,
            "record": record,
            "field": field,
            "old": old_value,
            "new": new_value

        })

    def save(self, filename="reports/changes.log"):

        os.makedirs("reports", exist_ok=True)

        with open(filename, "w") as f:

            f.write("POWER SYSTEM VALIDATION REPORT\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"Generated : {datetime.now()}\n\n")

            if len(self.changes) == 0:

                f.write("No Changes Made.\n")

            else:

                for c in self.changes:

                    f.write(f"Section : {c['section']}\n")
                    f.write(f"Record  : {c['record']}\n")
                    f.write(f"Field   : {c['field']}\n")
                    f.write(f"Old     : {c['old']}\n")
                    f.write(f"New     : {c['new']}\n")
                    f.write("-" * 40 + "\n")

        print(f"Change log saved as: {filename}")