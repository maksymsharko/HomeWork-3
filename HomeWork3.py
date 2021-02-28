#1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(int_a), id(str_b), id(set_c), id(lst_d), id(dict_e), sep='\n')

#2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)
print(id(lst_d))

#3. Define the type of each object from step 1.
print(type(int_a), type(str_b), type(set_c), type(lst_d), type(dict_e), sep='\n')

#4*. Check the type of the objects by using isinstance.
print(isinstance(int_a, int), isinstance(str_b, str), isinstance(set_c, set), isinstance(lst_d, list), isinstance(dict_e, dict), sep='\n')

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."

numapples = 'nine'
numpeaches = 'thirteen'
#5. With .format and curly braces.
print("Anna has {} apples and {} peaches".format(numapples, numpeaches))

#6. By passing index numbers into the curly braces.
print("Anna has {1} apples and {0} peaches".format(numpeaches, numapples))

#7. By using keyword arguments into the curly braces
print("Anna has {apples} apples and {peaches} peaches".format(apples = numapples, peaches = numpeaches))

#8*. With indicators of field size(5 chars for the first and 3 for the second)
print("Anna has {0:5} apples and {1:3} peaches".format(3, 5))

#9. With f-strings and variables
apples = 11
peaches = 21
print(f"Anna has {apples} apples and {peaches} peaches")

#10. With % operator
print("Anna has %s apples and %s peaches" % (apples, peaches))

#11*. With variable substitutions by name (hint: by using dict)
dict_with_apples_and_peaches = {"apples": numapples, "peaches": numpeaches}
print("Anna has %(apples)s apples and %(peaches)s peaches" % dict_with_apples_and_peaches)

# Comprehensions:

#12. Convert (1) to list comprehension

# (1)
lst = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst)

#13. Convert (2) to regular for with if-else
list_comprehension = []
for num in range(10):
    if num % 2 == 0:
        list_comprehension.append(num // 2)
    else:
        list_comprehension.append(num * 10)
print(list_comprehension)

#14. Convert (3) to dict comprehension.
dict_comprehension = {num:num ** 2 for num in range(1, 11) if num % 2 == 1}
print(dict_comprehension)

#15*. Convert (4) to dict comprehension.
dict_comprehension_1 = {num: num ** 2  if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(dict_comprehension_1)

#16. Convert (5) to regular for with if.
dict_comprehension_regulared = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_comprehension_regulared[x] = x ** 3
print(dict_comprehension_regulared)

#17*. Convert (6) to regular for with if-else.
dict_comprehension_with_if_else = {}
for x_ in range(10):
    if x ** 3 % 4 == 0:
        dict_comprehension_with_if_else[x_] = x ** 3
    else:
        dict_comprehension_with_if_else[x_] = x
print(dict_comprehension_with_if_else)

# Lambda

#18. Convert (7) to lambda function
foo = lambda x, y: x if x < y else y

#19*. Convert (8) to regular function
def foo_(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y

#20. Sort lst_to_sort from min to max
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))

#21. Sort lst_to_sort from max to min
print(sorted(lst_to_sort, reverse=True))

#22. Use map and lambda to update the lst_to_sort by multiply each element by 2
new_updated_list = list(map(lambda x: x * 2, lst_to_sort))
print(new_updated_list)

#23*. Raise each list number to the corresponding number on another list:
List_A = [2, 3, 4]
List_B = [5, 6, 7]
print(list(map(lambda x, y: x + y, List_A, List_B)))

#24. Use reduce and lambda to compute the numbers of a lst_to_sort.
from functools import reduce
print(reduce(lambda x, y: x + y, lst_to_sort))

#25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
print(list(filter(lambda x: x % 2 == 1, lst_to_sort)))

#26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
b = range(-10, 10)
print(list(filter(lambda x: x < 0, b)))

#27*. Using the filter function, find the values that are common to the two lists:
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
print(list(filter(lambda x: x in list_1, list_2)))










