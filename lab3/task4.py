try:
    words = input("Write a something: ")

    count_of_a = 0 #first, we add a variable to use it in the future.

    # for is a keyword that indicates the beginning of a loop.
    # word is a variable of a loop
    # in is a keyword that indicates that the loop will iterate over elements from the sequence described after this keyword.
    # words is a sequence, the elements of which will be iterated over in the loop.
    for word in words:
        if word == 'a' or word == 'A':
            count_of_a += 1 # we also state that if the letter "a" occurs in the string, the number will increase by 1

        print(f"The number of 'a' in word is: {count_of_a}")
except ValueError:
    print("Error")