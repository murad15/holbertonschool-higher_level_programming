#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Roman numeral values
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    # Traverse from right to left
    for ch in reversed(roman_string):
        value = roman_values.get(ch, 0)

        if value < prev_value:
            total -= value     # subtractive case (IV, IX, XL, etc.)
        else:
            total += value     # normal addition case

        prev_value = value

    return total
