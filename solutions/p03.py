LETTERS = "TRWAGMYFPDXBNJZSQVHLCKE"

def getLetter(dni: int) -> str:
    key = int(dni % 23)
    return LETTERS[key]

dni = int(input())
print(f"Letter: {getLetter(dni)}")