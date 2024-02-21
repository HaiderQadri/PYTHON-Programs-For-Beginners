def counting(string):
    upper = 0
    lower = 0
    for letter in string:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1
    return upper, lower


input_string = input("Enter the string: ")
upper, lower = counting(input_string)
print("Number of uppercase letter:", upper)
print("Number of lowercase letter:", lower)
