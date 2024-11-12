#!/usr/bin/python3
def read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints its content to stdout.

    Parameters:
    filename (str): The path to the file to be read.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
