
x = int(input("Enter the number: "))
y = int(input("Enter the power: "))

while True:
    try:
        result = pow(x, y)
        break
    except ValueError:
        print("Error")
print(f"The number is {x} and his power is {y} give us {result}")