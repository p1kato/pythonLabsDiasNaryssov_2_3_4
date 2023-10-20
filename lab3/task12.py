
N = int(input("Enter a number: "))

if N < 2:
    print("Are you really? ")
else:
    print(f"Prime numbers in the range from 1 to {N} are: ")

    number = 2

    while number <= N:
        a = True

        number += 1

        divisor = 2
        while divisor * divisor <= number:
            if number % divisor == 0:
                a = False
                break
            divisor += 1

        if a:
            print(number, end=" ")