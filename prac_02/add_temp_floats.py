"""Add Fahrenheit (floats) to temps_input.txt"""

from random import uniform

NUMBER_OF_TEMPERATURE_VALUES = 20
TEMPERATURE_INPUT_FILE = "temps_input.txt"


def main():
    """Print random fahrenheit values into input file."""
    out_file = open(TEMPERATURE_INPUT_FILE, "w")
    for i in range(NUMBER_OF_TEMPERATURE_VALUES):
        fahrenheit = uniform(-200, 200)
        print(fahrenheit, file=out_file)
    out_file.close()


main()
