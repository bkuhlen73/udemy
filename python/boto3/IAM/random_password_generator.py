#!/usr/bin/env python3

from random import choice

len_of_password = 8
valid_chars_for_password = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*()?"

# print(choice(valid_chars_for_password))

password = []

'''for each_char in range(len_of_password):
    password.append(choice(valid_chars_for_password))

random_password = ("".join(password))
'''

random_password = "".join(choice(valid_chars_for_password)
                          for each_char in range(len_of_password))

print(random_password)
