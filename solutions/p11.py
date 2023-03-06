known_letters = input()
num_words = int(input())

can_be_read = []
for i in range(num_words):
    word = input().lower()
    curr = "Yes"
    for letter in word:
        if letter not in known_letters:
            curr = "No"
            break
    can_be_read.append(curr)

for case in can_be_read:
    print(case)
    