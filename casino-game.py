secret_number = 9
guess = ""

guess = int(input("Enter guess: "))
while guess != secret_number:
    print("Try again")
    guess = int(input("Enter guess: "))

print("You win! ")










