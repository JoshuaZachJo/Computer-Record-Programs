while True:
    x = int(input("Enter the number: "))
    n = int(input("Enter the exponent: "))
    pow = 1
    i = 0
    while i < n:
        pow *= x
        i += 1
    print(pow)