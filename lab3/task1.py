
try:
    n = int(input("Enter a number: "))
    number = 1

    while number <= n:
        if number % 2 == 0: # in each iteration of the loop, its checked whether the current number (number) is divisible by 2 without remainder (which means that it is an even number)
            print(number, end = " ") #end=" " is used to print numbers in a line separated by a space
        number += 1 #also this cycle we increment by 1 to reach the "n" number
except ValueError:
    print("Error")