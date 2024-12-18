def vowel_shift(some_string, n):
    vowels = ['a','e','i','o','u','A','E','I','O','U']

    vowel_positions = [index for index, char in enumerate(some_string) if char in vowels]
    vowel_chars = [char for char in some_string if char in vowels]

    relative_shift = n % len(vowel_chars)
    shifted_vowels = vowel_chars[-relative_shift:] + vowel_chars [:-relative_shift]

    chars_list = list(some_string)
    shifted_positions = zip(vowel_positions, shifted_vowels)

    for index, char in shifted_positions:
        chars_list[index] = char

    shifted_string = ''.join(chars_list)
    return shifted_string
