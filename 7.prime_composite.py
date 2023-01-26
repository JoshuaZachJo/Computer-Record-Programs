while True:
    num = int(input("Enter a number: "))
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    if prime:
        print(num, "is a prime number")
    else:
        print(num, "is a composite number")