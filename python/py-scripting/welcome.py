# name = input('Please enter your name')
# message = "Hello {} Welcome to python scripting".format(name)
# print(message)

# one = input('Please enter number1\n')
# two = input('Please enter number2\n')
# result = int(one)+int(two)
# message = 'Sum of {} and {} is {}'.format(one,two,result)
# print(message)

# x = 'Java Home Cloud'.split()

# for data in x:
#     print(data)

# x = '1234567890'
# print(x[::2])

# data = [1,2,'A',10.4,2]

# data.append(34)
# data.insert(0,'Python')
# del data[0]

# for x in data:
#     print(x)

# data = {1, 2, 'A', 10.4, 2}
# data.add('AWS')
# for x in data:
#     print(x)

# print(data)

# data = {'Apple': 30, 'Oranges': 90, 'Grapes': 120}

# for x in data.keys():
#     print(x)

# print(data['Apple'])

# for y in data.values():
#     print(y)

# try:
#     data = {'A': 1, 'B': 2}
#    # print(data['C'])
#     print(10/0)
# except KeyError:
#     print('Execption in the code')
# except ZeroDivisionError:
#     print('Zero Division Error')
# finally:
#     print('Finally called ...')

# x = 10
# y = 20

# if x > y: 
#     print('X is greater than Y')
# else:
#     print('Y is greater then X')

# data = 1

# while data <= 10:
#     print(data)
#     data = data + 1

# data = [1,2,0,5,10]

# a = 1

# for x in data:
#     if x == 0: 
#         continue
#     a = a*x
# print('The value of a is {}'.format(a))

# data = [1,2,0,5,10]

# search = 0

# for x in data:
#     if search == x:
#         print('Value is found')
#         break

def add(x=5,y=5):
    result = x+y
    #print('Result of {} and {} is {}'.format(x,y,result))
    return result

result = add(10,20)
print(result)
result = add()
print(result)