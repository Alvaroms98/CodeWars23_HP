def formula(n: int) -> int:
    return int((n * (3*n - 1)) / 2)

n = int(input())
print(formula(n))