try:
    def fibonacci(n):
        a, b = 0, 1
        while a < n:
            print(a, end=" ")
            a, b = b, a+b #the first number (a) becomes equal to the previous second number (b), and the second number (b) becomes equal to the sum of the two previous numbers.

    n = int(input("Enter the number: "))
    fibonacci(n)
except ValueError:
    print("Error")