digit = int(input('Enter a digit of numbers: '))

num1 = digit//10000
num2 = (digit%10000)//1000
num3 = (digit%1000)//100
num4 = (digit%100)//10
num5 = digit%10

print(num1, num2, num3, num4, num5)