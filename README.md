# Text-Term-Replacer-Optimized

**Text-Term-Replacer-Optimized** is a Python-based text processing tool that replaces specific terms in a string using a predefined dictionary. The code implements **binary search** and **linear search** for finding terms to replace, and also utilizes **QuickSort** for sorting the dictionary entries before the replacement process. The aim is to compare the performance of these search algorithms while using an optimized sorting algorithm.

The tool is designed to be used in contexts such as **text normalization** in machine learning pipelines or **real-time transcription systems** where quick and efficient text replacement is required.

## Main Features:
- **Text replacement**: Replaces terms in a string based on a predefined dictionary of terms and their replacements.
- **Search algorithms**:
  - **Binary Search**: An efficient search algorithm with a time complexity of **O(log n)**, ideal for sorted data.
  - **Linear Search**: A simpler search algorithm with a time complexity of **O(n)**, used in the non-optimized approach.
- **Sorting with QuickSort**: The dictionary entries are sorted using the **QuickSort** algorithm before performing replacements, enabling efficient binary search.

## QuickSort Algorithm:
**QuickSort** is a divide-and-conquer algorithm for sorting. It selects a "pivot" element from the list and partitions the other elements into two sub-arrays: those less than the pivot and those greater than the pivot. The sub-arrays are then recursively sorted.

The primary benefit of QuickSort is its average time complexity of **O(n log n)**, which makes it efficient for sorting large datasets.

### Time Complexity:
- **Best case**: O(n log n) – when the pivot splits the array into equal parts.
- **Average case**: O(n log n) – the pivot typically divides the array into roughly equal halves.
- **Worst case**: O(n^2) – when the pivot is always the smallest or largest element, leading to unbalanced partitions.

In the text-term-replacer tool, **QuickSort** is applied to the dictionary of terms before replacements are made. This ensures the dictionary is sorted, which is crucial for performing efficient binary searches.

## Search Algorithms:
1. **Binary Search**: 
   - Used after the dictionary is sorted with **QuickSort**.
   - With binary search, the time complexity for finding a replacement is reduced to **O(log n)**, which is much faster than linear search for large dictionaries.
  
2. **Linear Search**: 
   - A basic search method where each term is checked one by one.
   - This approach has a time complexity of **O(n)**, meaning it takes longer for larger dictionaries or texts.

## Performance Comparison:
The tool compares the performance of both search approaches and measures the following metrics:
- **Execution time**: How fast the text replacement process is.
- **Memory usage**: The amount of memory used during execution.
- **CPU usage**: The percentage of CPU consumed during the replacement process.

### Results:
- **Binary search** provides a significant performance boost, especially with larger dictionaries or longer texts.
- **Linear search** may be useful for small dictionaries but becomes inefficient as the size of the dictionary or text increases.
- **QuickSort** ensures that the dictionary is sorted, allowing binary search to be used effectively for replacements.

## Example Usage:

```python

replace_terms_in_text_with_quick_sort, test["text"], test["dictionary"]
