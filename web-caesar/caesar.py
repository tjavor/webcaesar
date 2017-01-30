def alphabet_position(letter):
    asciilower = "abcdefghijklmnopqrstuvwxyz"
    asciiupper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter in asciilower:
        num_pos = asciilower.find(letter)
        return num_pos
    else:
        if letter in asciiupper:
            num_pos = asciiupper.find(letter)
            return num_pos
        else:
            return letter

def rotate_character(char, rot):
    asciilower = "abcdefghijklmnopqrstuvwxyz"
    asciiupper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a = alphabet_position(char)
    if char in asciilower:
        afterrot = (a + rot) % 26
        return asciilower[afterrot]
    else:
        if char in asciiupper:
            afterrot = (a + rot) % 26
            return asciiupper[afterrot]
        else:
            return char

def encrypt(message, rot):
    encrypted_text = ""
    for c in message:
        encrypted_c = rotate_character(c, rot)
        encrypted_text += encrypted_c
    return encrypted_text
