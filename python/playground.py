#list1 = ["CA", "NJ", "RI"]
#list2 = ["California", "New Jersey", "Rhode Island"]
#answer = {list1[i]: list2[i] for i in range(0, len(list1))}
# print(answer)

#person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
#answer = {key: value for key, value in person}
# print(answer)


#answer = answer = {char: 0 for char in 'aeiou'}#
# print(answer)


#answer = {count: chr(count) for count in range(65, 91)}
# print(answer)

def speak(animal='dog'):
    noises = {'pig': 'oink', 'duck': 'quack', 'cat': 'meow', 'dog': 'woof'}
    return noises.get(animal, '?')


print(speak('cat'))
