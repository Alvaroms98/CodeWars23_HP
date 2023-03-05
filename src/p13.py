inputt = input()

SHIFT = 64

def to_number(letters: str) -> int:
    pot = len(letters) - 1
    result = 0
    for letter in letters:
        num = ord(letter) - SHIFT
        result += num * (26**pot)
        pot -= 1
    return result

def to_letters(num: int, letters: str) -> str:
    reminder = num % 26
    reminder_letter = chr(reminder+SHIFT)
    letters = reminder_letter + letters
    div = num // 26
    if div <= 26:
        div_letter = chr(div+SHIFT)
        letters = div_letter + letters
        return letters
    else:
        letters = to_letters(div, letters)
    return letters

try:
    inputt = int(inputt)
    output = to_letters(inputt, "")
except Exception as e:
    output = to_number(inputt)

print(output)