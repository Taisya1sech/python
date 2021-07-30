
def gen_factorial(n):
    cur = 1
    for i in range(1, n + 1):
        cur *= i
        yield cur


n = 12
for ind, el in inenumerate(gen_factorial(n)):
    print(f"#{ind + 1} {el}")
