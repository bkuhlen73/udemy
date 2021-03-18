import random

highest = 100

answer = random.randint(1, highest)
guess = int(input("Please guess a number between 1 and {} ".format(highest)))
count = 1

while guess != answer:
    count += 1
    if guess == 0:
        print("0 exits the game, bye")
        break
    if guess < answer:
        print("Try higher")
    if guess > answer:
        print("Try lower")
    guess = int(input("Please guess a number between 1 and {} ".format(highest)))


print("you guessed it correctly and it took you {} turns to do so".format(count))