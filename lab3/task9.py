import random

secret_number = random.randint(1, 100)

for attempts in range(1, 6):  # Тут я решил сделать всего 5 попыток ;))

    user = int(input("Guess the number between 1 and 100: ".format(attempts)))

    if user == secret_number:

        print("You found this shit")
        print("You found this shit")
        print("You found this shit")
        break
    elif user < secret_number:
        print("Too small")
    else:
        print("Too large")
else:
    print(" ")
    print("You don't have any chance hihihihi")
    print("You lose this game. LOOOSEEER")