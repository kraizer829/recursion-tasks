"""Тести для всіх п'яти завдань. Запуск: python -m unittest test_tasks.py"""
import io
import unittest
from contextlib import redirect_stdout

from task1_reverse_string import print_reversed, reverse_string
from task2_swap_pairs import build_list, swap_pairs, to_list
from task3_fibonacci import fib
from task4_climb_stairs import climb_stairs
from task5_pow import my_pow


class TestRecursion(unittest.TestCase):
    def test_print_reversed(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            print_reversed("tiger")
        self.assertEqual(buf.getvalue(), "regit\n")

    def test_reverse_string(self):
        self.assertEqual(reverse_string("tiger"), "regit")
        self.assertEqual(reverse_string(""), "")

    def test_swap_pairs(self):
        self.assertEqual(to_list(swap_pairs(build_list([1, 2, 3, 4]))), [2, 1, 4, 3])
        self.assertEqual(to_list(swap_pairs(build_list([]))), [])
        self.assertEqual(to_list(swap_pairs(build_list([1]))), [1])
        self.assertEqual(to_list(swap_pairs(build_list([1, 2, 3]))), [2, 1, 3])

    def test_swap_pairs_moves_nodes_not_values(self):
        head = build_list([1, 2])
        first, second = head, head.next
        new_head = swap_pairs(head)
        self.assertIs(new_head, second)
        self.assertIs(new_head.next, first)

    def test_fib(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(30), 832040)

    def test_climb_stairs(self):
        self.assertEqual(climb_stairs(1), 1)
        self.assertEqual(climb_stairs(2), 2)
        self.assertEqual(climb_stairs(3), 3)
        self.assertEqual(climb_stairs(45), 1836311903)

    def test_pow(self):
        self.assertAlmostEqual(my_pow(2.0, 10), 1024.0)
        self.assertAlmostEqual(my_pow(2.1, 3), 9.261, places=5)
        self.assertAlmostEqual(my_pow(2.0, -2), 0.25)
        self.assertAlmostEqual(my_pow(1.0, 2**31 - 1), 1.0)
        self.assertAlmostEqual(my_pow(2.0, -2**31), 0.0)


if __name__ == "__main__":
    unittest.main()
