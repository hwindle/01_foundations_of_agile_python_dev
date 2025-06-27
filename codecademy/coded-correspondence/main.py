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


def generate_key(msg, key):
    # Vigenere cipher key, generates: keykeykey... 
    key = list(key)
    if len(msg) == len(key):
        return key
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return ''.join(key)


def vigenere_encode(msg, key):
    encrypted_text = []
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            encrypted_char = char
        encrypted_text.append(encrypted_char)
    return ''.join(encrypted_text)
    


def decrypt_vigenere(msg, key):
    decrypted_text = []
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
        elif char.islower():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            decrypted_char = char
        decrypted_text.append(decrypted_char)
    return ''.join(decrypted_text)


test_message = 'Hello there!'
encrypt = caesar_encode(test_message, 10)
print(encrypt)
decrypt = caesar_decode(encrypt.lower(), 10)
print(decrypt)