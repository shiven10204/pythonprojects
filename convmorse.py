morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}


morse_dict_reverse = {v: k for k, v in morse_dict.items()}


# Convert Morse code to a message
def from_morse_code(morse_code):
    morse_words = morse_code.split(' ')
    message = ''
    for morse_word in morse_words:
        if morse_word in morse_dict_reverse:
            message += morse_dict_reverse[morse_word]
    return message


# Driver code
def main():
    message = "Python Programming"
    morse_code = to_morse_code(message)

    print("Message: ", message)
    print("Morse code sequence: ", morse_code)

    decoded_message = from_morse_code(morse_code)
    print("Decoded message: ", decoded_message)


if __name__ == "__main__":
    main()
