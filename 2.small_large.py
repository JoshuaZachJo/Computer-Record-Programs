while True:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    if x > y:
        print("{} is largest and {} is smallest".format(x,y))
    elif x < y:
        print("{} is largest and {} is smallest".format(y, x))
    else:
        print("Both {} and {} are equal".format(x,y))