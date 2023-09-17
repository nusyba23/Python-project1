#Hangman Game
import sys
import random

f = open(str(sys.argv[0]))
words = []
for word in f:
    word = word.strip()
    if (word != ''):
        words.append(word)

print("Welcome to Hangman Game!")
print()
remaining = 8
secret = ""
while (len(secret) < 4):
    i = random.randint(0, len(words))
    secret = words[i]
letters = []
for i in range(0,len(secret)):
    letters.append("-")
guess = ""
bad = []
while (remaining !=0):
    print("The secret word looks like: ", end = "")
    for i in letters:
        print(i, end = "")
    if (len(bad) > 0):
        print("\nYour bad guesses so far: ", end = "")
        for i in bad:
            print(i + " ", end = "")
    print("\nYou have " + str(remaining) + " guesses remaining.")
    guess = input("What's your next guess? ")
    if (guess in secret):
        print("Nice guess!")
        for i in range(0, len(secret)):
             if (guess == secret[i]):
                 letters[i] = guess
        if ("".join(letters) == secret):
            print("\nCongratulations!\nYou guessed the secret word: " + secret)
            break
    else:
        remaining -= 1
        bad.append(guess)
        if (remaining == 0):
                print("\nYou Lose!\nThe secret word was: " + secret)
    print()