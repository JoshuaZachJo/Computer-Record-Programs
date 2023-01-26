while True:
    print("F i n d i n g    H . C . F .     o f    t w o    n u m b e r s ")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    while (x % y) > 0:
        remainder = x % y
        x = y
        y = remainder
    print(y, "is HCF of the numbers given by the user")

    print("F i n d i n g    L . C . M .     o f    t w o    n u m b e r s ")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    if x > y:
        greatest = x
    else:
        greatest = y
    while True:
        if greatest % x == greatest % y == 0:
            lcm = greatest
            break
        greatest += 1
    print(lcm, "is LCM given by the user")
