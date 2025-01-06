"""This module contains a function that takes a list of cardinal directions
and simplifies them by removing combinations of directions that result in
ending up in the same place."""
def simplify_directions(directions):
    acceptable_directions = ["NORTH", "SOUTH", "EAST", "WEST"]

    for direction in directions:
        if direction.upper() not in acceptable_directions:
            raise ValueError("Please check your directions!")

    upper_directions = [direction.upper() for direction in directions]

    if "NORTH" in upper_directions and "SOUTH" in upper_directions:
        upper_directions.remove("NORTH")
        upper_directions.remove("SOUTH")
    if "EAST" in upper_directions and "WEST" in upper_directions:
        upper_directions.remove("EAST")
        upper_directions.remove("WEST")

    if (("NORTH" in upper_directions and "SOUTH" in upper_directions)
        or ("EAST" in upper_directions and "WEST") in upper_directions):
        return simplify_directions(upper_directions)

    return upper_directions
