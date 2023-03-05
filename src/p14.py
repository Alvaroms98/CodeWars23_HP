cities = []
while True:
    curr = input()
    if curr == "#":
        break
    cities.append(curr)
shift = int(cities.pop())

length = len(cities)
for i in range(length):
    index = (i + shift)%length
    print(cities[index])
