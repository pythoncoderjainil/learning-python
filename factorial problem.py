# Question : 1/1% + 2/2%+ 3/3% + ... + n/n%

n = int(input("Enter a number: "))
sum= 0
factorial = 1
for i in range(1, n+1):
    factorial *= i
    sum += i / factorial

print("The sum is:", sum)