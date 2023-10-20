
odd_sum = 0

while True:
    try:
        a = input("Enter a number or you can enter the 'q' to quit): ")

        if a.lower() == 'q':
            break

        number = int(a)

        if number % 2 == 0:
            print("Even number, skipping:", number)
            continue

        odd_sum += number

    except ValueError:
        print("Error")

print("Sum of odd numbers:", odd_sum)