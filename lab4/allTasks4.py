from itertools import combinations, groupby

print("Taks 1: ")
string_word = input("Enter your word: ") # enter any word (String)
convert_tuple = tuple(string_word) #translating string to tuple via the tuple command
print("Converted word:", convert_tuple)

print("--------------------------------")
print("Task 2: ")
tuple_word = ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n')
convert_string = ''.join(tuple_word) #here we use the join command since this command combines all the elements and also adds " so that there are no symbols and so on between the elements
print("Output: ", convert_string) # there is just a output



print("--------------------------------")
print("Task 3: ") #in this task, you need to combine two tuples, but only by half, that is, the first half and the second half of the tuple are combined
a = (1, 2, 3, 4, 5, 6, 7)
b = (5, 6, 7, 9, 7, 1, 10, 10)
sum = a[:4] + b[4:] # here in the first tuple we write [:4] because it takes the first 4 elements of the first tuple, similarly to [4:] only here it takes elements starting from the 5th element and up to the end
print(sum) # that is, the digit in this case determines from which element to start or to which element to finish, the sign that defines it :

print("--------------------------------")
print("Task 4: ") # in this task, you need to make a counter of elements that are repeated in tuple
my_tuple = (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6)
element_count = {} # we are creating an empty storage and we will shove the elements that we will find there
for element in my_tuple: #we use the for loop so that it checks the elements as many times as the number of elements in the selected tuple (my_tuple)
    element_count[element] = element_count.get(element, 0) + 1 # the most interesting thing here is that it is used to get the current value of element from element_count, that is, if the element already exists in the dictionary, its value is returned, otherwise 0 is returned, and +1 simply increases the value of element by 1
result_tuple = tuple((k, v) for k, v in element_count.items()) # I'll start with k and v, k is a unique key (unique elements) in element_count, and v is the number of occurrences for each key, and then does the calculations
print("Элементы и их вхождения:", result_tuple) # it's just a output

print("--------------------------------")
print("Task 5:  ")
# this task is about creating a tuple and you need to organize the elements according to this condition
data = (55, 6, 777, 70.0, '7', 'A')
integers = tuple(x for x in data if isinstance(x, int)) # here we use a loop and a conditional operator, a loop in order for it to go through all the elements of a sha so that it checks whether these elements are int.
floats = tuple(x for x in data if isinstance(x, float)) # similarly with float and str, that is, they just check the type of data and outputs
strings = tuple(x for x in data if isinstance(x, str))
print(integers)
print(floats)
print(strings)

print("--------------------------------")
print("Task 6: ")
user_input = input("Enter your word: ")
my_set = {char for char in user_input} #I didn't understand what I did here, I'm kidding, this is a set generator that passes through each char character in the user_input string and adds it to the my_set set
# since in Python the set contains only unique elements, logically all elements that are repeated will be excluded and only unique ones will remain in mychar
print("Созданное множество:", my_set)

print("--------------------------------")
print("Task 7: ")
set_A = {1, 2, 3, 4, 5}
set_B = {5, 7, 8, 9, 2, 10}
difference_set = set_A.difference(set_B) # here we use the difference method, that is, by the name you can understand that it is responsible for the difference of the elements
#in short, difference_set contains elements present in set_A but missing in set_B
print(difference_set)

print("--------------------------------")
print("Task 8: ")
set_A = {1, 2, 3, 4, 5}
set_B = {5, 7, 8, 9, 2, 10}
set_A.difference_update(set_B) #there is a similar scheme here, but there is a difference, in this case we add update, that is, the difference_update method updates (removes) the difference of elements
print(set_A)

print("--------------------------------")
print("Task 9: ")
set_A = {1, 2, 3, 4, 7}
set_B = {8, 7, 9, 4, 2, 0, 10}
set_C = {4, 0, 1}

for element in set_C: #creating a loop to go through all the elements
    if element in set_A: # in if, if the elements are in sata, then we delete them and add them to setbook
        set_A.remove(element)
        set_B.add(element)

print("Updated set A:", set_A)
print("Updated set B:", set_B)

print("----------------------------------------------------------------")
print("Task 10: ") #for this task, we import the itertools library (I do not know what it is called, but in Java these are libraries) to use the combination method
A = {1, 2, 3, 4, 5, 6}
n = 3
m = 5
result = [set(combo) for combo in combinations(A, n)][:m] # here, for each created combination, it is converted into a set (set), this is done for each combination
# also [:m] is a piece that was already earlier, that is, m is just up to which element to leave, in this case m=5, that is, leaves only the first 5 combinations
print(result)

print("----------------------------------------------------------------")
print("Task 11: ") # you will also need itertools here
cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'), ('Fiat', '500'), ('Fiat', 'Panda'), ('Toyota', 'Camry 30')]

sorted_cars = sorted(cars_list, key=lambda x: x[0]) # in this task we are sorting by manufacturer and group of machine models
for manufacturer, group in groupby(sorted_cars, key=lambda x: x[0]): # key=lambda x: x[0] is an anonymous (lambda) function that takes the element x and returns the value x[0], that is, the first element of the tuple, in this case, the brand of the car
    group_list = list(group)
    count = len(group_list)
    models = [car[1] for car in group_list]
    print(f"{manufacturer} {count} - {', '.join(models)}")