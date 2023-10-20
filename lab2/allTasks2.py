try:
    print("Task 1: ")
    number = int(input("number:"))
    number1 = int(input("number:"))
    number2 = int(input("number:"))
    number3 = int(input("number:"))

    check1 = 0
    check2 = 0

    check1 = number + number3
    check2 = number1 - number2
    if check2 < 0:
        check2 = number2 - number1

    if check1 == check2:
        print("Yes")

    else:
        print("No")

except ValueError:
    print("Error")

print("----------------------------------------------------------------")

print("Task 2: ")
try:
    age = int(input("age:"))

    if age >= 18:
        print("Access allowed")

    else:
        print("Access denied")

except ValueError:
    print("Error")

print("----------------------------------------------------------------")

print("Task 3: ")
try:
    n = int(input("n:"))
    n1 = int(input("n:"))
    n2 = int(input("n:"))

    const = 0
    const1 = 0

    const = n2 - n1
    const1 = n1 - n

    if const == 1 and const1 == 1:
        print("Yes")
    else:
        print("No")


except ValueError:
    print("Error")

print("----------------------------------------------------------------")
print("Task 4: ")
try:
    position_col = int(input("position: "))
    position_row = int(input("position: "))
    position_col1 = int(input("position: "))
    position_row1 = int(input("position: "))

    if position_col == position_col1 or position_row == position_row1:
        print("Yes")
    else:
        print("No")
except ValueError:
    print("Error")
print("----------------------------------------------------------------")
print("Task 5: ")
try:
    king_col = int(input("position: "))
    king_row = int(input("position: "))
    king_col1 = int(input("position: "))
    king_row1 = int(input("position: "))

    if abs(king_col - king_col1) <= 1 and abs(king_row - king_row1) <= 1:
        print("Yes")
    else:
        print("No")
except ValueError:
    print("Error")

print("----------------------------------------------------------------")
print("Task 6: ")

try:
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    largest = max(a, b, c)
    smallest = min(a, b, c)

    average = (smallest + largest) / 2

    print(average)

except ValueError:
    print("Error")

print("----------------------------------------------------------------")
print("Task 7: ")

try:

    month = int(input("month: "))
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if 1 <= month <= 12:
        num_days = days_in_month[month - 1]
        print(num_days)
    else:
        print("error")

except ValueError:
    print("Error")

print("----------------------------------------------------------------")
print("Task 8: ")

try:
    weight = int(input("weight: "))

    if weight <= 60:
        print("Light weight babyyy")

    if weight <= 64 and weight >= 60:
        print("First welterweight")

    if weight <= 69 and weight >= 64:
        print("Welterweight")

except ValueError:
    print("Error")
print("----------------------------------------------------------------")
print("Task 9: ")
try:
    password = input("password: ")
    password_check = input("password: ")

    if password_check == password:
        print("Password accepted ")
    else:
        print("Password not accepted ")
except ValueError:
    print("Error")

print("----------------------------------------------------------------")
print("Task 10: ")

try:
    n = int(input("Number: "))

    if n % 2 == 0:
        print("Even number")

    else:
        print("odd")

except ValueError:
    print("Error")

print("----------------------------------------------------------------")
print("Task 11: ")

try:
    s = int(input("Number: "))
    l = int(input("Number: "))

    min_number = min(s, l)

    print(min_number)

except ValueError:
    print("Error")

print("----------------------------------------------------------------")
print("Task 12: ")

try:

    age_number = int(input("Age: "))

    if age_number <= 13:
        print("inclusive-childhood")

    if age_number >= 14 and age_number <= 24:
        print("youth")

    if age_number >= 25 and age_number <= 59:
        print("maturity")

    if age_number >= 60:
        print("old age")
except ValueError:
    print("Error")

print("----------------------------------------------------------------")
print("Task 13: ")
try:
    t = int(input("Number: "))
    j = int(input("Number: "))
    o = int(input("Number: "))

    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("Equilateral")
        elif a == b or a == c or b == c:
            print("Isosceles")
        else:
            print("Versatile")


except ValueError:
    print("Error")