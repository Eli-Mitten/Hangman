import random

words = ["perroflauta", "calistenia", "mermelada"]
secret_word = random.choice(words)
print(secret_word)
display = ["_"] * len(secret_word)

go_on = "true"
while go_on == "true":
	
	letter = input("Select letter: ").lower()
	
	for index, char in enumerate(secret_word):
		if letter == char.lower():
			display[index] = char
			
	if "_" not in display:
		go_on = "false"
		
	print(display)

print("you win")