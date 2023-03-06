num = int(input())

piramids = {}
for i in range(num):
    info = input()
    splitted = info.split(' ')
    piramid = splitted.pop(0)
    north = []
    south = []
    from_south = False
    for item in splitted:
        if item == "#":
            from_south = True
        else:
            if from_south:
                south.append(int(item))
            else:
                north.append(int(item))
    south.reverse()
    if north == south:
        piramids[piramid] = True
    else:
        piramids[piramid] = False

for key, value in piramids.items():
    if value:
        print(f"{key} has same number of steps for both faces")
    else:
        print(f"{key} has NOT same number of steps for both faces")
