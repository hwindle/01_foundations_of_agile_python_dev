#!/usr/bin/python3

def caesar_decode(msg, offset):
    letters='abcdefghijklmnopqrstuvwxyz'
    decrypted_message = ''
    for character in msg:
        if character in letters:
            position = letters.find(character)
            new_pos = (position - offset) % 26
            new_char = letters[new_pos]
            decrypted_message += new_char
        else:
            decrypted_message += character
    return decrypted_message


def caesar_encode(msg, offset):
    result = ''
    # iterate over the given text
    for i in range(len(msg)):
        ch = msg[i]
        # add space
        if ch == ' ':
            result += ' '
        # check if a character is uppercase then encrypt it accordingly 
        elif (ch.isupper()):
            result += chr((ord(ch) + offset - 65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly
        
        else:
            result += chr((ord(ch) + offset - 97) % 26 + 97)
    return result

# Vinegere cipher


test_message = 'Hello there!'
encrypt = caesar_encode(test_message, 10)
print(encrypt)
decrypt = caesar_decode(encrypt.lower(), 10)
print(decrypt)