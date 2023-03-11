# Define Morse code dictionary
MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                   '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}


# Define function to convert string to Morse code
def string_to_morse_code(s):
    morse_message = ''
    for char in s:
        if char.upper() in MORSE_CODE_DICT:
            morse_message += MORSE_CODE_DICT[char.upper()] + ' '
        else:
            morse_message += ' '
    return morse_message.strip()


# Get input string from user
input_string = input('Enter a string to convert to Morse code: ')

# Convert string to Morse code
morse_code = string_to_morse_code(input_string)

# Print the Morse code
print(morse_code)
