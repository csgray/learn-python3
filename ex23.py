# Import the entire system module
import sys
# Set variables to those passed when the script is called
script, encoding, error = sys.argv

# Defines a function 'main'
def main(language_file, encoding, errors):
    # Reads the file until it encounters a new-line character
    line = language_file.readline()

    # If there was anything to read...
    if line:
        # Calls the 'print_line' function
        print_line(line, encoding, errors)
        # Calls 'main' again to continue reading the file
        return main(language_file, encoding, errors)

# Defines a function 'print_line'
def print_line(line, encoding, errors):
    # Removes any leading and trailing whitespace characters from the line
    next_lang = line.strip()
    # Encodes the line using the specified encoding
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # Decodes the encoded bytes
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    # Outputs the encoded and decoded strings side-by-side
    print(raw_bytes, "<===>", cooked_string)

# Opens the source file
languages = open("languages.txt", encoding="utf-8")

# Calls 'main' to start decoding the source file
main(languages, encoding, error)