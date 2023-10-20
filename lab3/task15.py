def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            shifted_char_code = ord(char) + shift

            if char.islower() and shifted_char_code <= ord('z'):
                result += chr(shifted_char_code)
            elif char.isupper() and shifted_char_code <= ord('Z'):
                result += chr(shifted_char_code)
            else:
                result += chr(shifted_char_code - 26)
        else:
            result += char

    return result