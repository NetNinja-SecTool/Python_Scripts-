# filename: command_line_argument.py
import sys

if len(sys.argv) > 1:
    print("Command-line argument:", sys.argv[1])
else:
    print("No command-line argument provided.")
