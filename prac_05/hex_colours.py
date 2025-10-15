"""Hex Colours"""

COLOUR_TO_HEX = {
    "Aqua": "00ffff",
    "Coral Pink": "f88379",
    "Zomp": "39a78e",
    "Gray35": "595959",
    "Magic Mint": "aaf0d1",
    "Palatinate Purple": "682860",
    "School Bus Yellow": "ffd800",
    "Tumbleweed": "deaa88",
    "Van Dyke Brown": "664228",
    "Bright Green": "66ff00",
    "AliceBlue": "f0f8ff",
}

# Change each colour string in new dict to lowercase for case-independency.
lowercase_colour_to_proper = {colour.lower(): colour for colour in COLOUR_TO_HEX}

colour = input("Enter a colour: ").lower()
while colour != "":
    try:
        colour_name = lowercase_colour_to_proper[colour]
        hex_code = COLOUR_TO_HEX[colour_name]
        print(f"Hex code is #{hex_code}")
    except KeyError:
        print("Invalid colour name.")
    colour = input("Enter a colour: ").lower()
print("Finished")
