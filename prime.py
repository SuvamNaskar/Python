    # TODO: Check if a number is prime or not

n = int(input("Enter a Number: "))
flag = 0

for i in range(2, n):
    if(n % i == 0):
        flag = 1

if(flag == 1):
    print("Number is NOT-PRIME")
else:
    print("Number is PRIME")