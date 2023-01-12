# This code prints  the pattern D 
for i in range(1,6):
    for j in range(i):
        print("*", end='')
    print()

for i in range (4, 0, -1):
    for j in range(i):
        print("*",end='')
    print()

# This program guesses a number between 1 and 9
import random 
number = random.randint(1,9)


guess = int(input("Guess a number a number between 1 and 9: "))
 
while guess != number:
    print("wrong try again. ")
    guess = int(input("Guess a number between 1 and 9: "))

print("you guessed in right! The number was", number)
