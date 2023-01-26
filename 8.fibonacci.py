while True:
    n = int(input('Enter a limit: '))
    a = 0
    b = 1
    print(a)
    while b < n:
        print(b)
        temp = a
        a = b
        b = temp + b
