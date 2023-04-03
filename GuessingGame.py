#Mini game: Guess the number 1-100
#Author: Dimitris Apostolakis

import random

secret = random.randint(1, 100)
cnt_tries = 1 #Counter for the user's tries.
cnt_limit = 10 #Maximum attempt limit.


print("You have " + str(cnt_limit) + " tries")
guess = int(input("Give your number: "))

while guess != secret:
    if guess > secret:
        print("The secret number is smaller!")
    elif guess < secret:
        print("The secret number is larger!")
    guess = int(input("Give your number: "))
    cnt_tries += 1
    if cnt_tries == cnt_limit:
        print("You have surpass the limit of tries. You lost.")
        break
else:
    print("You found it")
