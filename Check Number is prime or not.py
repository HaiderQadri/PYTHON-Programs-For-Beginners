num = int(input("Enter the number: "))
if num <= 1:
    print(f"{num} is not prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not prime number")
            break
    else:
         print(f"{num} is prime number")