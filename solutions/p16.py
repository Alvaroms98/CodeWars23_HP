original = input()[:-1]
words = original.split(" ")
output = ""
is_acronym = False
before = ""
for word in words:
    first_upper = word[0].isupper()
    if first_upper and not is_acronym:
        is_acronym = True
    elif first_upper and is_acronym:
        output += before[0]
    elif not first_upper and is_acronym:
        output += before[0]
        is_acronym = False
        output += f"{word} "
    else:
        output += f"{word} "
    before = word
output.strip()
output += "."
print(output)
