"""Завдання 3. Числа Фібоначчі: F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2).

Використовується мемоізація (словник уже обчислених значень),
щоб не рахувати одні й ті самі F(k) багато разів.
"""


def fib(n: int, memo: dict | None = None) -> int:
    if memo is None:
        memo = {}
    if n < 2:
        return n          # F(0) = 0, F(1) = 1
    if n in memo:
        return memo[n]
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    print(fib(2))  # 1
    print(fib(3))  # 2
    print(fib(4))  # 3
