# Simple Python drill that works with while loops and breaking out of them

secret_number = 9
error = 0

while error < 3:
    guessed_number = int(input('Guess a number: '))
    if guessed_number == secret_number:
        print("Congrats!")
        break
    else:
        error = error + 1
        print("Guess again!")

if(error == 3):
    print("Game over!")