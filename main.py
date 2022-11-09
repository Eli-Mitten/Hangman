import random
from graphics import hang_man

lives = 6

words = ["escorbuto", "calistenia", "majaderias"]
secret_word = random.choice(words)
## print(secret_word)
display = ["_"] * len(secret_word)

end_of_game = False
while not end_of_game and lives > 0:

    letter = input("Select letter: ").lower()

    lose_live = True
    for index, char in enumerate(secret_word):
        if letter == char.lower():
            display[index] = char
            lose_live = False

    if lose_live:
        lives -= 1

    print(hang_man[lives])
    print(display)
	
    if "_" not in display:
        end_of_game = True
        print("You win")
        
    if lives == 0:
        print("You Lose!!")