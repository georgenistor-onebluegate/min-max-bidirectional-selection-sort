# Min-Max Bidirectional Selection Sort (MMBSS)

**Author:** George Nistor  
**Version:** 1.0

Min-Max Bidirectional Selection Sort (MMBSS) is an in-place, comparison-based, bidirectional selection sort. During one traversal of the active unsorted region, it identifies both the minimum and maximum values, places the minimum at the left boundary and the maximum at the right boundary, and then shrinks the active region from both sides.

## Core properties

- In-place
- Comparison-based
- Bidirectional
- Selects minimum and maximum in one traversal
- Supports duplicate values
- Time complexity: `O(n²)`
- Auxiliary space: `O(1)`
- Not stable

## Reference implementation

The original experimental implementation is preserved in `main.py`. The canonical function implementation is in `mmbss.py`.

## Verification

`test_mmbss.py` includes basic, adversarial, randomized, and exhaustive tests. The exhaustive tests cover every array up to length 8 over `{0,1,2}` and every array up to length 6 over `{-2,-1,0,1,2}`.

## Attribution

This repository documents and attributes the algorithm described here as:

**Min-Max Bidirectional Selection Sort (MMBSS) — George Nistor**

The repository provides a public technical record of the algorithm, its reference implementation, and its verification methodology.
