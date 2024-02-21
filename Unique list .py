def unique_list(list):
    x = []
    for element in list:
        if element not in x:
            x.append(element)
    return x


input_list = input("Enter the list: ")
print("Unique list: ",unique_list(input_list))


