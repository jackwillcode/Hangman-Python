import random
import hangman_art
import hangman_words

#Step 1 

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(hangman_words.word_list)
chosen_word_length = len(chosen_word) 

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []

for x in range(chosen_word_length):
    display.append("_")

#Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters 
#in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

current_number_of_blanks = chosen_word_length
previous_number_of_blanks = chosen_word_length
letter_already_guessed = False

print(hangman_art.logo)

while current_number_of_blanks != 0 and lives != 0:
    #Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess =  input("Guess a letter you think is in the word: ").lower()

    #Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    """
    for letter in chosen_word:
        if letter == guess:
            print("Right")

        else:
            print("Wrong")
    """
    for x in range(chosen_word_length):
        if guess == chosen_word[x]:
            if display[x] == guess:
                print(f"The letter \'{guess}\' has already been guessed. Try again.")
                letter_already_guessed = True
            else:
                display[x] = guess
                current_number_of_blanks -= 1 

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if current_number_of_blanks == previous_number_of_blanks and not letter_already_guessed:
        print(f"The letter \'{guess}\' is not in the word. Try again.")
        lives -= 1
    else:
        previous_number_of_blanks = current_number_of_blanks

    letter_already_guessed = False

    #Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
    print(display)
    print(hangman_art.stages[lives])

if current_number_of_blanks == 0:
    print("You win!")
else:
    print("You lose.")