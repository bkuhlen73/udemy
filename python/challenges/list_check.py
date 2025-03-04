'''
list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True
'''


def list_check(vals):
    #    print(list(l for l in vals))
    return all(type(l) == list for l in vals)


# list_check([[], [1], [2, 3]])  # True
print(list_check([[], [1], [2, 3]]))  # True)
print(list_check([1, True, [], [1], [2, 3]]))  # False)
