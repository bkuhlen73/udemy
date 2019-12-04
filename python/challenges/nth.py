def nth(arr, idx):
    if idx >= 0:
        return arr[idx]
    return arr[idx + len(arr)]


print(nth(['a', 'b', 'c', 'd'], 1))  # 'b'
print(nth(['a', 'b', 'c', 'd'], -2))  # 'c'
print(nth(['a', 'b', 'c', 'd'], 0))  # 'a'
print(nth(['a', 'b', 'c', 'd'], -4))  # 'a'
print(nth(['a', 'b', 'c', 'd'], -1))  # 'd'
print(nth(['a', 'b', 'c', 'd'], 3))  # 'd'
