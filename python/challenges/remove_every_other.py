'''
remove_every_other([1,2,3,4,5]) # [1,3,5] 
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1] 
'''


def remove_every_other(lst):
    #    return [val for i, val in enumerate(lst) if i % 2 == 0]
    #    return [val for val in (lst) if val % 2 == 0]
    # for val in enumerate(lst):
    #     if val[0] % 2 == 0:
    #         print(val)
    return [val[1] for val in enumerate(lst) if val[0] % 2 == 0]


print(remove_every_other([1, 2, 3, 4, 5]))  # [1,3,5] )
