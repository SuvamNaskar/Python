    # TODO: Fibonacci Series Generator

a = 0
b = 1
n = int(input("Enter number of terms: "))

print(str(a) + " " + str(b) + " ")
for i in range(3, n + 1):
    c = a + b
    print(str(c) + " ")
    a = b
    b = c