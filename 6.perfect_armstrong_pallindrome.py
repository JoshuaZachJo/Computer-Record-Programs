while True:
    sel = input("Welcome! Select a program to run:\n[1] Palindrome \n[2] Armstrong number \n[3] Perfect number \n ")
    if sel == "1":
        n = int(input("Enter a number:"))
        temp = n
        rever = 0
        while n > 0:
            digit = n % 10
            rever = rever * 10 + digit
            n = n // 10
        if temp == rever:
            print(temp, "The number is a palindrome")
        else:
            print(temp, "The number isn't a palindrome")

    elif sel == "2":
        n = int(input("Enter a number:"))
        count = 0
        temp = n
        while temp > 0:
            digit = temp % 10
            count += digit ** 3
            temp //= 10
        if n == count:
            print(n, "is an Armstrong number")
        else:
            print(n, "is not an Armstrong number")

    elif sel == "3":
        n = int(input("Enter a number:"))
        count = 0
        for i in range(1, n):
            if n % i == 0:
                count = count + i
        if count == n:
            print(n, "The number is a perfect number")
        else:
            print(n, "The number is not a perfect number")
