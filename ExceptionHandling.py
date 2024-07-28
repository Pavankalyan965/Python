def division():
    while True:
        try:
            a = int(input("Enter a numerator"))
            b = int(input("Enter a denominator"))
            print(a/b)
        except ZeroDivisionError:
            print("Zero division error")
division()


