'''
reverse_string('awesome') # 'emosewa'
reverse_string('Colt') # 'tloC'
reverse_string('Elie') # 'eilE'
'''

# add whatever parameters you deem necessary - good luck!


def reverse_string(str):
    # s = ''
    # print(str[::-1])
    # for i, char in enumerate(str[::-1]):
    #     s += char
    # return s
    s = ''
    s = str[::-1]
    return s


print(reverse_string('awesome'))  # 'emosewa'
