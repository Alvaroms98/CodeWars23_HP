init = int(input())

def collatz(n: int, secuence: list) -> None:
    secuence.append(n)
    if n == 1:
        return
    elif (n % 2) == 0:
        n = int(n / 2)
    else:
        n = int(n * 3 + 1)
    collatz(n, secuence)

sec = []
collatz(init, sec)
output = f"{sec[0]}"
for num in sec[1:]:
    output += " -> "
    output += f"{num}"
output += f" [{len(sec) - 1}]"
print(output)
