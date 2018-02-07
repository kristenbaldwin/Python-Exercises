plain = "abcdefghijklmnopqrstuvwxyz"
cipher_text = "lbh zhfg hayrnea jung lbh unir yrnearq"
offset = 13
decoded = ""

for character in cipher_text:
    ascii_code = ord(character)
    if ascii_code >= 97 and ascii_code <= 122:
        decode_character = ascii_code + offset
        if decode_character >= 122:
            new_character = chr(decode_character - 26)
        else:
            new_character = chr(decode_character)
    else:
        new_character = chr(ascii_code)
    decoded += new_character
print(decoded)