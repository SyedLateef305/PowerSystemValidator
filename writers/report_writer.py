from datetime import datetime
from config import REPORT_FOLDER


class ReportWriter:
    def __init__(self, tracker):
        self.tracker = tracker

    def generate(self):
        REPORT_FOLDER.mkdir(exist_ok=True)

        path = REPORT_FOLDER / datetime.now().strftime(
            "ValidationReport_%d%m%Y_%H%M%S.txt"
        )

        with open(path, "w") as report:
            report.write("POWER SYSTEM CHANGE REPORT\n")
            report.write("=" * 60 + "\n\n")

            if not self.tracker.changes:
                report.write("No Changes Made.\n")
            else:
                for i, c in enumerate(self.tracker.changes, 1):
                    report.write(f"Change {i}\n")
                    report.write(f"Time: {c['time']}\n")
                    report.write(f"Section: {c['section']}\n")
                    report.write(f"Record: {c['record']}\n")
                    report.write(f"Field: {c['field']}\n")
                    report.write(f"Old: {c['old']}\n")
                    report.write(f"New: {c['new']}\n\n")

        print(f"Report generated: {path}")
        return path