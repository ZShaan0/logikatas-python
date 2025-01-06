"""This module contains a function that takes a number and
returns a roman numeral string representation of the number"""
def roman_numeral_encoder(num):
    roman_numerals = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
            ]

    roman_string = ""

    for value, roman_char in roman_numerals:
        while num >= value:
            roman_string += roman_char
            num -= value

    return roman_string
