"""Завдання 2. Поміняти місцями кожні два сусідніх вузли зв'язаного списку.

Значення у вузлах не змінюються — переставляються самі вузли.
[1, 2, 3, 4] -> [2, 1, 4, 3]
[]           -> []
[1]          -> [1]
"""
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    # 0 або 1 вузол — міняти нічого
    if head is None or head.next is None:
        return head
    first = head
    second = head.next
    # спочатку рекурсивно обробляємо хвіст після пари
    first.next = swap_pairs(second.next)
    # другий вузол стає першим
    second.next = first
    return second


# ----- допоміжні функції (теж рекурсивні) -----
def build_list(values: list[int]) -> Optional[ListNode]:
    """Створює зв'язаний список із Python-списку."""
    if not values:
        return None
    return ListNode(values[0], build_list(values[1:]))


def to_list(head: Optional[ListNode]) -> list[int]:
    """Перетворює зв'язаний список у Python-список."""
    if head is None:
        return []
    return [head.val] + to_list(head.next)


if __name__ == "__main__":
    print(to_list(swap_pairs(build_list([1, 2, 3, 4]))))  # [2, 1, 4, 3]
    print(to_list(swap_pairs(build_list([]))))            # []
    print(to_list(swap_pairs(build_list([1]))))           # [1]
