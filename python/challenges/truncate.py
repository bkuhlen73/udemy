'''
truncate("Super cool", 2) # "Truncation must be at least 3 characters."
truncate("Super cool", 1) # "Truncation must be at least 3 characters."
truncate("Super cool", 0) # "Truncation must be at least 3 characters."
truncate("Hello World", 6) # "Hel..."
truncate("Problem solving is the best!", 10) # "Problem..."
truncate("Another test", 12) # "Another t..."
truncate("Woah", 4) # "W..."
truncate("Woah", 3) # "..."
truncate("Yo",100) # "Yo"
truncate("Holy guacamole!", 152) # "Holy guacamole!"
'''


def truncate(string, n):
    if (n < 3):
        return "Truncation must be at least 3 characters."
    if (n > len(string) + 2):
        return string

    return string[:n - 3] + "..."


print(truncate("Super cool", 2))  # "Truncation must be at least 3 characters."
print(truncate("Super cool", 1))  # "Truncation must be at least 3 characters."
print(truncate("Super cool", 0))  # "Truncation must be at least 3 characters."
print(truncate("Hello World", 6))  # "Hel..."
print(truncate("Problem solving is the best!", 10))  # "Problem..."
print(truncate("Another test", 12))  # "Another t..."
print(truncate("Woah", 4))  # "W..."
print(truncate("Woah", 3))  # "..."
print(truncate("Yo", 100))  # "Yo"
print(truncate("Holy guacamole!", 152))  # "Holy guacamole!"
