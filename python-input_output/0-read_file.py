#!/usr/bin/python3
"""
This module provides a function to read and print the contents of a UTF-8 encoded text file.
"""

def read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints its content to stdout.

    Parameters:
    filename (str): The path to the file to be read.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            print(f.read(), end="")
    except FileNotFoundError:
        pass  # Silently ignore if the file does not exist
