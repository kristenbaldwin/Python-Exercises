height = int(input("Height? "))
lines = 0

for i in range(0, height):
    lines += 1
    
    blank_space = height - lines
    increase_char = lines + (lines - 1)
    print(" " * blank_space, "*" * increase_char, sep="")