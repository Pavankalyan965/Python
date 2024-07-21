num1 =0
num2 =1

limit = int(input("Enter your number to which Fibonacci series is to be printed: "))
print(num1)
print(num2)
while(num2<=limit):
    next_num = num1 + num2
    print(next_num)
    num1 = num2
    num2 = next_num

