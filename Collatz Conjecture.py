#Write a program using a while loop that takes a positive integer n from the user and calculates how many steps it takes to reach 1 following these simple rules:
# If n is even, divide it by 2 (n = n / 2).
# If n is odd, multiply it by 3 and add 1 (n = 3n + 1).
# Repeat this process until n becomes 1.Print the value of n at each step and output the total number of steps taken.

n = int(input("Enter a positive integer: "))
counter=0

while n>1:
    if n%2==0:
      n=n/2
    else:
      n=3*n+1
    counter += 1
    print("STEP NO.", counter, ":", n)
    print("Total no. of steps taken to reach 1 is:", counter)
