a = input("")

while True:

    try:
        num = int(a)
        if num == 42:
            print("you found this shit")
            break #in general, I think everything is clear, but I will explain about break. break is a code that stops the loop and terminates the code. let's say we enter the number 42, but without using break, then the cycle will continue indefinitely.
        else:
            break
    except ValueError:
        print("Error")