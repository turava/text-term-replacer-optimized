# Text-Term-Replacer-Optimized

**Text-Term-Replacer-Optimized** is a Python-based text processing tool that replaces specific terms in a string using a predefined dictionary. The code implements two types of search to find the words to replace: **binary search** and **linear search**.

The tool is optimized for efficiency, using binary search as an improvement over the traditional linear search. The goal is to demonstrate how different search approaches affect performance in terms of execution time, memory usage, and CPU usage.

## Main Features:
- **Text replacement**: Replaces terms in a string based on a predefined dictionary of terms and their replacements.
- **Binary and linear search**: Implements both search methods to compare performance.
  - **Binary search** is used in the optimized approach, providing more efficient time complexity compared to linear search.
  - **Linear search** is used in the non-optimized approach, iterating through the replacement list sequentially.

## Use Cases:
- **Text normalization** in machine learning pipelines.
- **Real-time transcription systems** that require fast and efficient term replacement.

## Implementation:
The code performs the following key operations:

1. **Dictionary preprocessing**: Creates a sorted list of terms to replace, improving performance during searches.
2. **Term replacement**: A search (binary or linear) is performed for each word in the text, and it is replaced if found in the dictionary.

## Performance Comparison:
The tool's performance was evaluated using both search approaches, and the following metrics were measured:
- **Execution time**: The total time taken for the text replacement process.
- **Memory usage**: The amount of memory used during the execution of the code.
- **CPU usage**: The percentage of CPU consumed while the algorithm is running.

#### Performance Tests:
- **Binary search**: Uses **O(log n)** for searching terms in the dictionary, which results in more efficient performance for large texts or large dictionaries.
- **Linear search**: Uses **O(n)**, which may be slower for large texts due to the need to iterate through the entire dictionary for each word in the text.

#### Results:
- **Binary search** showed an improvement in **execution time** and **memory usage** compared to linear search.
- **Linear search** is useful for small dictionaries, but as the dictionary or text grows in size, the binary search becomes more efficient.

## Example Usage:

```python
from text_term_replacer import replace_terms

# Replacement dictionary
replacements = {
    "Gayá": ["galla", "gallá", "gaya", "gayá"],
    "Deportes+": ["deportesplus", "DeportesPlus", "deportes+"]
}

# Text to process
input_text = "Tenemos a galla en DeportesPlus"

# Replace using binary search (optimized)
output_text = replace_terms(input_text, replacements, use_binary_search=True)
print(output_text)  # "Tenemos a Gayá en Deportes+"
