VOWELS = "aeiouAEIOU"
sentence = input()
new_sentence = ""
for letter in sentence:
    if letter in VOWELS:
        new_sentence+="*"
    else:
        new_sentence+=letter

print(new_sentence)