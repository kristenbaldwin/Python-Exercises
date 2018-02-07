# Exercise 1

my_name = "kristen"
print(my_name.upper())

# Exercise 2

print(my_name.capitalize())

# Exercise 3

greeting = "Hello there and good morning"
def reverse(string):
    return string[::-1]
print(reverse(greeting))

# Exercise 4

#A => 4
#E => 3
#G => 6
#I => 1
#O => 0
#S => 5
#T => 7

text = input("Your text: ").upper()
text = text.replace("A", "4")
text = text.replace("E", "3")
text = text.replace("G", "6")
text = text.replace("I", "1")
text = text.replace("O", "0")
text = text.replace("S", "5")
text = text.replace("T", "7")
print(text)

# Exercise 5

word = input("Your word: ")
word = word.replace("oo", "ooooo")
word = word.replace("ee", "eeeee")
print(word)

# Exercise 6

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