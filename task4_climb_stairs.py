"""Завдання 4. Скількома способами можна піднятися на n сходинок кроками по 1 або 2.

На останню сходинку можна потрапити або з (n-1), або з (n-2), тому
ways(n) = ways(n-1) + ways(n-2), ways(1) = 1, ways(2) = 2.
Мемоізація потрібна, бо n може бути до 45 (без неї — мільярди викликів).
"""


def climb_stairs(n: int, memo: dict | None = None) -> int:
    if memo is None:
        memo = {}
    if n <= 2:
        return n          # 1 -> 1 спосіб, 2 -> 2 способи
    if n in memo:
        return memo[n]
    memo[n] = climb_stairs(n - 1, memo) + climb_stairs(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    print(climb_stairs(2))   # 2
    print(climb_stairs(3))   # 3
    print(climb_stairs(45))  # 1836311903
