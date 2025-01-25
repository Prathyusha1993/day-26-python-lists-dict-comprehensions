numbers = [1,2,3]
new_list = []
for n in numbers:
    add = n + 1
    new_list.append(add)
print(new_list)


# above using list comprehension
new_list = [n+1 for n in numbers]
print(new_list)

# conditional list comprehension
# new_list = [new_item for item in list if test]
names = ['alex', 'beth', 'carolina', 'dave', 'eleanor', 'freddie']
short_names = [n for n in names if len(n) < 5]
print(short_names)

upper_names = [name.upper() for name in names if len(name) > 5 ]
print(upper_names)


list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
print(numbers)
result = [num for num in numbers if num % 2 == 0]
print(result)