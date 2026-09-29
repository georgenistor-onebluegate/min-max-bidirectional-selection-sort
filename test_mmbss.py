import random
from itertools import product

from mmbss import mmbss


def test_basic():
    cases = [[], [1], [2, 1], [1, 2], [3, 2, 1], [1, 2, 3], [7, 3, 9, 1, 5, 8, 2], [5, 4, 3, 2, 1]]
    for original in cases:
        assert mmbss(original.copy()) == sorted(original)


def test_duplicates():
    cases = [[1, 1], [1, 1, 1], [2, 1, 2], [5, 5, 1, 1], [3, 2, 3, 2, 3, 2], [9, 2, 9, 1, 9], [1, 9, 1, 9, 1, 9]]
    for original in cases:
        assert mmbss(original.copy()) == sorted(original)


def test_maximum_at_left_boundary():
    cases = [[9, 2, 5, 1, 7], [10, 1, 2, 3, 4], [100, 5, 4, 3, 2, 1], [9, 1, 9, 2, 3], [50, -10, 20, 0, 40]]
    for original in cases:
        assert mmbss(original.copy()) == sorted(original)


def test_duplicate_maximum_interaction():
    cases = [[9, 2, 5, 1, 9], [9, 9, 5, 1, 2], [9, 2, 9, 1, 9], [10, 1, 10, 2, 10, 3]]
    for original in cases:
        assert mmbss(original.copy()) == sorted(original)


def test_boundary_and_sign_cases():
    cases = [[1, 5, 3, 4, 2], [-1, -2, -3], [3, -1, 2, -5, 0], [0, -1, 1, -2, 2], [7, 7, 7, 7]]
    for original in cases:
        assert mmbss(original.copy()) == sorted(original)


def test_sorted_and_reverse():
    for n in range(101):
        original = list(range(n))
        assert mmbss(original.copy()) == original
        reverse = list(reversed(original))
        assert mmbss(reverse.copy()) == original


def test_random():
    rng = random.Random(20260929)
    for _ in range(100_000):
        n = rng.randint(0, 100)
        original = [rng.randint(-100, 100) for _ in range(n)]
        assert mmbss(original.copy()) == sorted(original)


def test_exhaustive(values, max_length):
    total = 0
    for n in range(max_length + 1):
        for values_tuple in product(values, repeat=n):
            original = list(values_tuple)
            assert mmbss(original.copy()) == sorted(original)
            total += 1
    return total


if __name__ == "__main__":
    print("Running MMBSS verification suite...")
    test_basic()
    test_duplicates()
    test_maximum_at_left_boundary()
    test_duplicate_maximum_interaction()
    test_boundary_and_sign_cases()
    test_sorted_and_reverse()
    test_random()
    count_a = test_exhaustive([0, 1, 2], 8)
    count_b = test_exhaustive([-2, -1, 0, 1, 2], 6)
    print(f"Exhaustive domain A: {count_a} cases")
    print(f"Exhaustive domain B: {count_b} cases")
    print("All MMBSS tests passed.")
