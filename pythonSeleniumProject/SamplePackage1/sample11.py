
# Fibonacci series
def fibonacci_num():
    cycle = int(input("Enter your number: "))
    num1 = 0
    num2 = 1
    print(num1, num2, end = " ")
    for i in range(2, cycle+1):
        num3 = num1 + num2
        print(num3, end = " ")
        num1 = num2
        num2 = num3
    print(" ")

fibonacci_num()





