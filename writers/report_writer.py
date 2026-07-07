import os
from datetime import datetime


class ReportWriter:

    def __init__(self, tracker):

        self.tracker = tracker

    def generate(self):

        os.makedirs("reports", exist_ok=True)

        filename = datetime.now().strftime(
            "ValidationReport_%d%m%Y_%H%M%S.txt"
        )

        path = os.path.join("reports", filename)

        with open(path, "w") as report:

            report.write("=" * 60 + "\n")

            report.write("POWER SYSTEM VALIDATION REPORT\n")

            report.write("=" * 60 + "\n\n")

            report.write(
                f"Generated : {datetime.now()}\n\n"
            )

            if len(self.tracker.changes) == 0:

                report.write("No Changes Made.\n")

            else:

                for i, change in enumerate(
                        self.tracker.changes,
                        start=1):

                    report.write(f"Change {i}\n")

                    report.write(
                        f"Time      : {change['time']}\n"
                    )

                    report.write(
                        f"Section   : {change['section']}\n"
                    )

                    report.write(
                        f"Record    : {change['record']}\n"
                    )

                    report.write(
                        f"Field     : {change['field']}\n"
                    )

                    report.write(
                        f"Old Value : {change['old']}\n"
                    )

                    report.write(
                        f"New Value : {change['new']}\n"
                    )

                    report.write("\n")

        print()

        print("=" * 70)

        print("REPORT GENERATED")

        print("=" * 70)

        print(path)