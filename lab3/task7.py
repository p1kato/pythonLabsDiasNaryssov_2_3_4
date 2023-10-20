try:
    def reverse_string(input_str):
        reversed_str = ""
        for char in input_str:
            reversed_str = char + reversed_str
        return reversed_str

    input_str = input("Enter a string: ")
    print("Reversed string:", reverse_string(input_str))
except ValueError:
    print("Error")