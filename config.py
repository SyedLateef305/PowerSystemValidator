from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
INPUT_FILE = PROJECT_ROOT / "sample_files" / "sample.dat"

# Keep one canonical output folder
OUTPUT_FOLDER = PROJECT_ROOT / "output"
LOG_FOLDER = PROJECT_ROOT / "logs"
REPORT_FOLDER = PROJECT_ROOT / "reports"

# Match the actual folder in the project ZIP
BACKUP_FOLDER = PROJECT_ROOT / "backup"