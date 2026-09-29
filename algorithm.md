# Min-Max Bidirectional Selection Sort (MMBSS)
## Canonical Algorithm Specification — Version 1.0

**Author:** George Nistor

## Abstract

Min-Max Bidirectional Selection Sort (MMBSS) is an in-place comparison-based sorting algorithm that selects the minimum and maximum values of the current unsorted region during a single traversal.

At the end of each traversal, the selected minimum is placed at the left boundary of the unsorted region and the selected maximum is placed at the right boundary. The sorted portion therefore grows simultaneously from both ends.

## Definition

For an array `A` of length `n`, iteration `i` operates on the active region `A[i : n-i]`. The minimum of that region is placed at `A[i]`, and the maximum is placed at `A[n-i-1]`. The active region then contracts by two positions.

## Reference pseudocode

    MMBSS(A):
        n <- length(A)
        for i <- 0 to floor(n / 2) - 1:
            minimum <- A[i]
            maximum <- A[i]
            index_min <- 0
            index_max <- 0
            swap_min <- false
            swap_max <- false
            size <- n - i

            for j <- i to size - 1:
                if A[j] <= minimum:
                    minimum <- A[j]
                    index_min <- j
                    swap_min <- true
                if A[j] >= maximum:
                    maximum <- A[j]
                    index_max <- j
                    swap_max <- true

            if swap_min:
                swap A[index_min], A[i]
                if maximum = A[index_min]:
                    index_max <- index_min

            if swap_max:
                swap A[index_max], A[size - 1]
        return A

## Outer-loop invariant

At the beginning of iteration `i`, `A[0:i]` contains the `i` smallest elements in nondecreasing order, `A[n-i:n]` contains the `i` largest elements in nondecreasing order, and `A[i:n-i]` contains the remaining elements.

## Maximum-index correction

The minimum swap occurs before the maximum swap. If the original left-boundary value is the maximum, moving the minimum away from that boundary also moves that maximum to `index_min`. The reference implementation detects this with:

    if maximum == A[index_min]:
        index_max = index_min

If multiple equal maximum values exist, selecting another occurrence is equivalent with respect to sorted output.

## Correctness argument

Each pass examines every element in the active region, identifies an occurrence of its minimum and maximum, and places those extrema at the two boundaries. Those two elements are then in their final positions, so the active region can shrink by two. Repetition terminates when zero or one element remains in the active region, which is already sorted.

## Complexity

- Time: `O(n²)`
- Auxiliary space: `O(1)`
- Stable: No

## Canonical one-sentence definition

> Min-Max Bidirectional Selection Sort (MMBSS), authored by George Nistor, is an in-place selection sort that identifies the minimum and maximum elements of the active unsorted region during a single traversal, places them toward opposite boundaries, and progressively shrinks the unsorted region from both sides.

## Attribution

**Algorithm:** Min-Max Bidirectional Selection Sort (MMBSS)  
**Author:** George Nistor  
**Version:** 1.0
