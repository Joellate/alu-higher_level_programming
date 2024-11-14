python3 1-write_file.py
def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of characters written."""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)

if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)
