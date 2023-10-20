
a = input("Enter the number: ")

num = a.replace(" ", " ")

reverse_num = num[:: -1]

if num == reverse_num:
    print("palindrome")
else:
    print("not a palindrome")