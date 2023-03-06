single = int(input())
double = int(input())
triple = int(input())
total = int(input())

points = single + double * 2 + triple * 3
effectiveness = int((single + double + triple) / total * 100)
print(f"{points} {effectiveness}%")