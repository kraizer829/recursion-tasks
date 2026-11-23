"""Завдання 5. Власна функція піднесення до степеня pow(x, n).

Швидке піднесення до степеня: x^n = (x^(n/2))^2, тому глибина рекурсії
лише ~log2(n) (близько 31 навіть для n = 2^31 - 1).
Для від'ємного n: x^(-n) = 1 / x^n.
"""


def my_pow(x: float, n: int) -> float:
    if n < 0:
        return 1 / my_pow(x, -n)
    if n == 0:
        return 1.0
    half = my_pow(x, n // 2)
    if n % 2 == 0:
        return half * half
    return half * half * x


if __name__ == "__main__":
    print(f"{my_pow(2.0, 10):.5f}")  # 1024.00000
    print(f"{my_pow(2.1, 3):.5f}")   # 9.26100
    print(f"{my_pow(2.0, -2):.5f}")  # 0.25000
