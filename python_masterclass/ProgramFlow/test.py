# number = "9,223;372:036 854,775;807"
# separators = ""
#
# for char in number:
#     if not char.isnumeric():
#         separators = separators + char
#
# separators = list(dict.fromkeys(separators))
# print(separators)
#
# values = "".join(char if char not in separators else " " for char in number).split()
# print([int(val) for val in values])
#
# quote = """
# Alright, but apart from the Sanitation, the Medicine, Education, Wine,
# Public Order, Irrigation, Roads, the Fresh-Water System,
# and Public Health, what have the Romans ever done for us?
# """
#
# # Use a for loop and an if statement to print just the capitals in the quote above.
# for char in quote:
#     if char.isupper():
#         print(char)

#for i in range(1, 13):
#    for j in range(1, 13):
#        print("{0} times {1} is {2}".format(j, i, i*j))
#    print("-----------------")

