import random
play_again = "Y"

while play_again == "Y":
    my_random_number = random.randint(1, 10)
    number_of_guesses = 5
    # secret_number = 5
    print("I am thinking of a number between 1 and 10.")

    while number_of_guesses > 0:
        print(f"You have {number_of_guesses} guesses left.")
        number_guess = int(input("What's the number? "))
        if number_guess < my_random_number:
            number_of_guesses -= 1
            print(f"{number_guess} is too low.")
        elif number_guess > my_random_number:
            number_of_guesses -= 1
            print(f"{number_guess} is too high.")
        else:
            print("Yes! You win!")
            play_again = input("Do you want to play again (Y or N)? ")
            break

        if number_of_guesses == 0:
            print("You ran out of guesses!")
            play_again = input("Do you want to play again (Y or N)? ")
            break

    while True:
        if play_again == "Y":
            number_of_guesses = 5
            break
        elif play_again == "N":
            print("Bye!")
            break