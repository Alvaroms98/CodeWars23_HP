
numbers = []
while True:
    new = input()
    if new == "#":
        break
    numbers.append(int(new))

length = len(numbers)
sums = ""
products = ""
for i in range(length):
    sum = 0
    product = 1
    for j in range(length):
        if i != j:
            sum += numbers[j]
            product *= numbers[j]
    sums += f"{sum} "
    products += f"{product} "

print(sums.strip())
print(products.strip())
