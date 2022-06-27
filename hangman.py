
def main():
    import time
    import random

    #welcoming the user
    name = input(f"What is your name? ")
    print (f"Hello, {name} Time to play Hangman!")
    print(f"You have only 30 seconds to play!!")
    print ("")

    #wait for 1 second
    time.sleep(1)

    print (f"Start guessing...")
    time.sleep(0.5)

    print("Done!")

    secret_Word = ("stacktrek", "bootcamp","league", "coding", "programmer", "fullstack", "stacked")
    secret_Word = random.choice(secret_Word)
    print(secret_Word)

    letter_Guessed = ""

    # The number of turns before the player loses
    failure_Count = 5

    # Time Clock
    time_Limit = 30
    start_Time = time.time()
    
    while failure_Count > 0:
        # get the guessed letter from the player
        guess = input("Enter a letter: ").lower()
        # Timer
        elapsed_Time = time.time() - start_Time
        print(time_Limit - int(elapsed_Time))
        if elapsed_Time > time_Limit:
            print(f"Game Over {elapsed_Time} Times Up!")
            start_Again = input("Do you want to try again? [yes/no] ").lower()
            if start_Again == "yes":
                main()
        if guess in secret_Word:
            # player guessed a correct answer
            print(f"Correct! There is one or more {guess} in the secret word.")
            # if guess in secret_Word:
        else:
            failure_Count -= 1
            print(f"Incorrect! There is no {guess} in the secret word. {failure_Count} turn(s) left.")
        
        # Maintain a list of all Letters guessed
        letter_Guessed = letter_Guessed + guess
        wrong_Letter_Count = 0

        for letter in secret_Word:
            if letter in letter_Guessed:
                print(f"{letter}", end="")
            else:
                print("-", end="")
                wrong_Letter_Count += 1
        print("")
        # If there no wrong letters, then the player won!
        if wrong_Letter_Count == 0:
            print(f"Congratulations! The secret word was: {secret_Word}. You Won!:)")
            break
    else:
        print(f"Sorry, You Didn't win this time.The secret word is: {secret_Word}")   

    play_again = input("Do you want to try again? [yes/no] ").lower()

    if play_again == "yes":
        main()
    else:
        exit()

main()

