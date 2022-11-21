num = []
n = int(input("Enter the amount of numbers to sort : "))

for _ in range(0, n):
    numbers = int(input('Give me a number: '))
    num.append(numbers)
num.sort()

print(num)
