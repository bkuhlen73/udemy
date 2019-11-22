# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]
# answer = {list1[i]: list2[i] for i in range(0, len(list1))}
# print(answer)

# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# answer = {key: value for key, value in person}
# print(answer)


#answer = answer = {char: 0 for char in 'aeiou'}#
# print(answer)


# answer = {count: chr(count) for count in range(65, 91)}
# print(answer)

# def speak(animal='dog'):
#     noises = {'pig': 'oink', 'duck': 'quack', 'cat': 'meow', 'dog': 'woof'}
#     return noises.get(animal, '?')


# print(speak('cat'))

# def product(a, b):
#     return a*b


# print(product(2, 2))
# print(product(2, -2))

# def return_day(day):
#     days = {1: "Monday", 2: "Tuesday", 3: "Wednesday",
#             4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
#     if day > 0 and day <= len(days):
#         return days[day]
#     return None


# print(return_day(7))

# def last_element(l):
#     """ my description """
#     if l:
#         return l[-1]
#     return None


# print(last_element([1, 2]))

# def number_compare(a, b):
#     if a == b:
#         return "Numbers are equal"
#     elif a > b:
#         return "First is greater"
#     return "Second is greater"


# print(number_compare(b=3, a=4))

# def single_letter_count(my_string="var", letter="a"):
#     return my_string.lower().count(letter.lower())


# print(single_letter_count("somedumMystring", 'M'))

# def multiple_letter_count(string):
#     return {letter: string.count(letter) for letter in string}


# print(multiple_letter_count("awesome"))

# def frequency(collection, searchTerm):
#     return collection.count(searchTerm)


# print(frequency([1, 2, 3, 4, 4, 4], 4))

# def capitalize(string):
#     return string[:1].upper() + string[1:]


# print(capitalize("tim"))  # "Tim"
# print(capitalize("matt"))  # "Matt"

# def compact(l):
#     truthy_vals = []
#     for val in l:
#         if val:
#             truthy_vals.append(val)
#     return truthy_vals


# # [1,2, "All done"])
# print(compact([0, 1, 2, "", [], False, {}, None, "All done"]))

# def intersection(list1, list2):
#     return [val for val in set(list1) & set(list2)]


# print(intersection(['a', 'b', 'c', 'c'], ['c', 'd', 'e']))

# def isEven(num):
#     return num % 2 == 0


# def partition(lst, fn):
#     return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]


# print(partition([1, 2, 3, 4], isEven))  # [[2,4],[1,3]]

# def contains_purple(*args):
#     for word in args:
#         word = str(word).lower()
#         if word == "purple":
#             return True
#     return False

# def contains_purple(*args):
#     if "purple" in args:
#         return True
#     return False


# print(contains_purple("bla", 12, True, "Purple", "blue"))
# # contains_purple(2)

# def count_sevens(*args):
#     return args.count(7)

# nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]

# print(count_sevens(1,4,7))
# print(count_sevens(*nums))


# def calculate(**kwargs):
#     '''
#     calculate(make_float=False, operation='add', message='You just added',
#             first=2, second=4) # "You just added 6"
#     calculate(make_float=True, operation='divide',
#             first=3.5, second=5) # "The result is 0.7"
#     '''
#     operation_lookup = {
#         'add': kwargs.get('first', 0) + kwargs.get('second', 0),
#         'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
#         'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
#         'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
#     }
#     is_float = kwargs.get('make_float', False)
#     operation_value = operation_lookup[kwargs.get('operation', '')]
#     if is_float:
#         final = "{} {}".format(kwargs.get(
#             'message', 'The result is'), float(operation_value))
#     else:
#         final = "{} {}".format(kwargs.get(
#             'message', 'The result is'), int(operation_value))
#     return final


# print(calculate(make_float=False, operation='add', message='You just added',
#                 first=2, second=4))

# def square(num):
#     return num*num


# print(square.__name__)

# def cube(num): return num**3


# print(cube(5))

# def decrement_list(l):
#     return list(map(lambda n: n-1, l))


# print(decrement_list([1, 2, 3]))

# def remove_negatives(nums):
#     return list(filter(lambda l: l >= 0, nums))


# l = [1, -2, 3, 4]

# print(remove_negatives(l))

# def is_all_strings(lst):
#     return all(type(l) == str for l in lst)


# lst = ['a', 'b', 2]
# print(is_all_strings(lst))

# def extremes(nums):
#     return(min(nums), max(nums))


# print(extremes([1, 2, 3, 4, 5]))

# def max_magnitude(nums):
#     return max(abs(num) for num in nums)


# print(max_magnitude([100, 200, -300]))

# def sum_even_values(*args):
#     return sum(arg for arg in args if arg % 2 == 0)


# print(sum_even_values(1, 2, 3, 4, 5, 6, 7, 8))

# def sum_floats(*args):
#     return sum(arg for arg in args if type(arg) == float)


# print(sum_floats(2, 3, 1.1, 2.2))


def triple_and_filter(lst):
    #    return list(map(lambda x: x*3, lst))
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))


print(triple_and_filter([1, 2, 3, 4, 5, 6, 7, 8]))
