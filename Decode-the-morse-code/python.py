def decode_the_morse_code(morse_code):
    message = "".join(
        [MORSE_CODE[i] if i in MORSE_CODE else " " for i in morse_code.split(" ")]
    )
    return message.replace("  ", " ").strip()
