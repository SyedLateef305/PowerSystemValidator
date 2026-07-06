import os


def print_title(title):
    print("\n" + "=" * 70)
    print(title.center(70))
    print("=" * 70)


def print_success(message):
    print(f"[SUCCESS] {message}")


def print_error(message):
    print(f"[ERROR] {message}")


def pause():
    input("\nPress Enter to continue...")