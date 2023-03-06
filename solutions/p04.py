times = int(input())
letters_arr = []
for letter in ["O", "E", "A"]:
    letters_arr.append(letter*times)

print(f"{letters_arr[0]}H! Y{letters_arr[1]}{letters_arr[2]}H!")