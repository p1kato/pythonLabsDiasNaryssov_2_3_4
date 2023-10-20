try:
    n = int(input("Enter a number: "))

    if n < 0:
        print("factorial")
    else:
        factorial = 1 #n must be greater than zero, because the factorial does not work on negative numbers
        a = 1
        while a <= n: #nnside the loop, the current factorial value is multiplied by the value of a each time, and a is incremented by 1
            factorial *= a
            a += 1
        print(f"The factorial of {n} is {factorial}") #I think everything is clear with the string, it is used to ensure that our recorded and output data are combined in the completed code
except ValueError:
    print("Error")