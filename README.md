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

## Attribution and prior art

This repository documents **Min-Max Bidirectional Selection Sort (MMBSS)** as George Nistor's implementation and documentation of a bidirectional/min-max selection sorting approach. Related algorithms have been described previously under names including Bidirectional Selection Sort, Double Selection Sort, and Min-Max Selection Sort. The repository's attribution and provenance discussion records this prior art and distinguishes it from the specific implementation and documentation maintained here.

## Citation

**Nistor, G. (2026). _Min-Max Bidirectional Selection Sort (MMBSS), Version 1.0.0_. Zenodo.**

DOI: https://doi.org/10.5281/zenodo.23033516

For citation metadata, see [`CITATION.cff`](CITATION.cff).

## Public archive

The versioned v1.0.0 release is archived through Zenodo and identified by DOI **10.5281/zenodo.23033516**.

## Repository

GitHub: https://github.com/georgenistor-onebluegate/min-max-sort-v3
