"""
Min-Max Bidirectional Selection Sort (MMBSS)
Canonical reference implementation, Version 1.0

Author: George Nistor
"""


def mmbss(a):
    """Sort list a in ascending order using the canonical MMBSS algorithm."""
    for i in range(0, int(len(a) / 2)):
        maximum = minimum = a[i]
        index_min = index_max = 0
        swap_min = swap_max = False
        size = len(a) - i

        for j in range(i, size):
            if a[j] <= minimum:
                minimum = a[j]
                index_min = j
                swap_min = True

            if a[j] >= maximum:
                maximum = a[j]
                index_max = j
                swap_max = True

        if swap_min:
            a[index_min], a[i] = a[i], a[index_min]
            if maximum == a[index_min]:
                index_max = index_min

        if swap_max:
            a[index_max], a[size - 1] = a[size - 1], a[index_max]

    return a


if __name__ == "__main__":
    example = [7, 3, 9, 1, 5, 8, 2]
    print("Input: ", example)
    print("Output:", mmbss(example))
