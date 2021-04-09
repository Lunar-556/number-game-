secret_number = 556
guess_amounts = 0
guess_limit = 3
while guess_amounts < guess_limit:
   guess = int(input("Guess a number 1-1000.   "))
   guess_amounts += 1
   if guess != secret_number:
       continue
   print("you guess the secret number!   ")
   break

if guess_amounts >= guess_limit:
    print("you have run out of guesses. ")