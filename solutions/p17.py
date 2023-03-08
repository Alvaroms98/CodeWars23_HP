sentence = input()

positions = []
while True:
    curr = input()
    if curr == "#":
        break
    positions.append(int(curr))

final_dot = False
if sentence[-1] == ".":
    sentence = sentence[:-1]
    final_dot = True

words = sentence.split(" ")
for i in positions:
    word = words[i-1]
    aux = ""
    for j in range(len(word)-1, -1, -1):
        aux += word[j]
    words[i-1] = aux

output = " ".join(words)
if final_dot:
    output += "."

print(output)