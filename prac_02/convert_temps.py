"""
Convert Fahrenheit temperatures from temps_input.txt
to Celsius temperatures and write to temps_output.txt.
"""

TEMPERATURE_INPUT_FILE = "temps_input.txt"
TEMPERATURE_OUTPUT_FILE = "temps_output.txt"


def main():
    """Read Fahrenheit from input file and write Celsius to output file."""
    in_file = open(TEMPERATURE_INPUT_FILE, "r")
    out_file = open(TEMPERATURE_OUTPUT_FILE, "w")
    for line in in_file:
        fahrenheit = float(line.strip())
        celsius = convert_fahrenheit_to_celsius(fahrenheit)
        print(celsius, file=out_file)
    in_file.close()
    out_file.close()


def convert_fahrenheit_to_celsius(fahrenheit):
    """Calculate Celsius value based on Fahrenheit."""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
