from random import randint


def intro():
    print("Hello")
    print("Welcome to the game, here we will be asking you to guess a number between 1 and 100")
    print("You will only get 4 guesses, if you guess correctly you will have won the game.")
    user_input = input("Shall we begin? (Yes)")
    while user_input.lower() != str("yes"):
        print("That is incorrect, please try again")
        user_input = input("Shall we begin? (please enter yes)")

    print("okay")


def random_number_generator(min_number,max_number):
    answer = randint(min_number, max_number)
    return answer


def number_guessing_game():
    max_guess = 6
    max_number = 100
    min_number = 0
    victory = False
    counter = 0

    intro()

    target = random_number_generator(min_number,max_number)

    while not victory:
        value_guessed = input("Please guess a value between 1 and 100: ")
        try:
            value_guessed = int(value_guessed)
        except ValueError:
            print("Error converting type to int, please try again")
        else:
            if value_guessed <= min_number:
                print("This value is below the bottom value")
            elif value_guessed > max_number:
                print("This value is above the top value")
            else:
                counter += 1
                if counter == max_guess:
                    print(f' You guessed {counter} and weren\'t able to complete the game, you loser.')
                    break
                elif value_guessed < target:
                    print("That guess is too low")
                elif value_guessed > target:
                    print("That guess is too high")
                else:
                    print(f'congratulations! You were able to complete the game in {counter} guesses')
                    victory = True


if __name__ == "__main__":
    number_guessing_game()
