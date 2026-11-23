"""Завдання 1. Надрукувати строку у зворотному порядку (рекурсивно, без циклів).

"tiger" -> "regit"
"""


def print_reversed(s: str) -> None:
    """Друкує строку у зворотному порядку."""
    if s == "":
        print()  # кінець рядка
        return
    print(s[-1], end="")      # останній символ
    print_reversed(s[:-1])    # решта строки без останнього символу


def reverse_string(s: str) -> str:
    """Повертає перевернуту строку (зручно для тестів)."""
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])


if __name__ == "__main__":
    print_reversed("tiger")  # regit
