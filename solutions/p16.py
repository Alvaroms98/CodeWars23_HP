original = input()[:-1]

words = original.split(" ")

output = ""
memory = []
last = (len(words) - 1)
for i in range(len(words)):
    word = words[i]
    is_upper = word[0].isupper()
    if is_upper and i < last:
        memory.append(word)
    else:
        if i == last:
            memory.append(word)
            word = ""
        if len(memory) > 1:
            for acronym in memory:
                output += acronym[0]
            output += " "
            memory = []
        elif len(memory) == 1:
            output += f"{memory.pop()} "
        output += f"{word} "

output = output.strip()
output += "."
print(output)
