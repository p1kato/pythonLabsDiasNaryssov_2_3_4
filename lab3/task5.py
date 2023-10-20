
a = input("Enter a number: ")

sum_of_digits = 0

for digit in a:
    if digit.isdigit(): # isdigit() is useful when you need to make sure that a string contains only digits
        sum_of_digits += int(digit)

print(f"The sum of the digits is: {sum_of_digits}")