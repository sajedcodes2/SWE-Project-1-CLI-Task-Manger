# Start your CLI app here.
#
# Run it with:  python3 src/main.py
#
# The brief is in PROJECT.md.

from menu import show_menu


def start_app():
    print()
    print("Do you know the United States Capitals Quiz Game!\n")
    show_menu()
    print("Goodbye!")


if __name__ == "__main__":
    start_app()
