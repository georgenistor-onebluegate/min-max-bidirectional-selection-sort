# Attribution and prior-art record

## Algorithm / project

**Min-Max Bidirectional Selection Sort (MMBSS)**

## Author attribution

This repository documents and attributes the **MMBSS implementation, terminology, experiments, and reference code** to **George Nistor**.

This attribution should not be read as a claim that the general idea of selecting both a minimum and maximum during a pass and placing them at opposite ends of an array originated with this repository.

## Prior art identified in the initial literature search

The initial search identified earlier work describing substantially the same core sorting strategy:

1. **Wang Min (2010), “Design and analysis on bidirectional selection sort algorithm.”** The paper describes bidirectional selection-sort designs in which minimum and maximum elements are selected from the unsorted region and placed at opposite ends. DOI: 10.1109/ICETC.2010.5529660.

2. **Mahesh Goyani, Mohammad Chharchhodawala, and Bhargav Mendapara (2013), “Min-Max Selection Sort Algorithm – Improved Version of Selection Sort.”** The paper describes simultaneous minimum/maximum selection and placement at the respective ends, reducing the number of outer passes. The paper was subsequently listed by the journal site in Volume 4, Issue 10 (October 2014).

3. **Double Selection Sort / Bidirectional Selection Sort references.** Later educational and technical references use names such as Double Selection Sort, Bidirectional Selection Sort, and Min-Max Selection Sort for the same general family of algorithms: select both extrema in the active region, place them at opposite boundaries, and shrink the region from both ends.

## Comparison with MMBSS

| Feature | Earlier bidirectional / min-max selection variants | MMBSS repository |
|---|---|---|
| Select minimum and maximum in one active-region scan | Yes | Yes |
| Place minimum toward left boundary | Yes | Yes |
| Place maximum toward right boundary | Yes | Yes |
| Shrink active region from both sides | Yes | Yes |
| In-place comparison sorting | Yes | Yes |
| `O(n²)` time / `O(1)` auxiliary space | Yes | Yes |
| Name “Min-Max Bidirectional Selection Sort (MMBSS)” | Not established as unique by this search | Used by this repository |
| George Nistor reference implementation and project documentation | Not applicable | Yes |

## Important implementation note

The reference implementation in `mmbss.py` performs the minimum placement before the maximum placement and includes an explicit correction of `index_max` when the maximum value has been moved by the minimum swap. This is an implementation detail of the repository's reference code; the initial prior-art search also found closely related index-adjustment logic in descriptions of double-selection sort.

## Conclusion of the initial search

The initial search does **not** support a claim that the general min/max bidirectional selection-sort technique was invented by George Nistor. Earlier published descriptions clearly predate this repository.

The defensible attribution for this repository is that **George Nistor is the author of the MMBSS project as documented here: its chosen terminology, reference implementation, experiments, tests, and documentation.**

This is an initial literature search, not an exhaustive patent or scholarly prior-art investigation. Absence of a result in this document should not be interpreted as proof that no other related work exists.

## Public record

Repository: https://github.com/georgenistor-onebluegate/min-max-sort-v3

The repository preserves the specification, reference implementation, verification suite, citation metadata, attribution record, and Git development history.
