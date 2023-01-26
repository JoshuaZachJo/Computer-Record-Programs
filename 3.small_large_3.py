while True:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    z = int(input("Enter the third number: "))
    if x == y == z:
        print("All the three values are {}".format(x))
    elif x > y:
        if x > z:
            print("{} is larger than {} and {}".format(x, y, z))
    elif y > z:
        print("{} is larger than {} and {}".format(y, x, z))
    else:
        print("{} is larger than {} and {}".format(z, x, y))
