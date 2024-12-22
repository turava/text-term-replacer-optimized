import re
import bisect

def quicksort(arr):
    """
    Replace terms in the given text using QuickSort for sorting replacement words 
    and binary search to find words to replace.
    Args:
        text (str): The input text where replacements need to be made.
        dictionary (dict): A dictionary with replacement terms as keys and lists of terms to be replaced as values.
    Returns:
        str: The modified text after replacements.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    return quicksort(left) + middle + quicksort(right)


def binary_search(word_list, word):
    """
    Perform binary search on a sorted list of words.
    
    Args:
        word_list (list): The sorted list of words to search through.
        word (str): The word to search for.
    
    Returns:
        bool: True if the word is found, False otherwise.
    """
    index = bisect.bisect_left(word_list, word)
    if index < len(word_list) and word_list[index] == word:
        return True
    return False

# Búsqueda binaria
#def binary_search(word_list, word):
    index = bisect.bisect_left(word_list, word)
    if index < len(word_list) and word_list[index] == word:
        return True
    return False

def replace_terms_in_text_with_quick_sort(text, dictionary):
    """
    Replace terms in the given text using QuickSort for sorting replacement words 
    and binary search to find words to replace.
    
    Args:
        text (str): The input text where replacements need to be made.
        dictionary (dict): A dictionary with replacement terms as keys and lists of terms to be replaced as values.
    
    Returns:
        str: The modified text after replacements.
    """
    words_to_replace = []
    for values in dictionary.values():
        words_to_replace.extend(values)
    
    # Sorting the words using the imported quicksort function
    words_to_replace = quicksort(words_to_replace)

    words = text.split()
    for i, word in enumerate(words):
        word_clean = re.sub(r'\W', '', word).lower()  # Clean word
        if binary_search(words_to_replace, word_clean):
            for key, values in dictionary.items():
                if word_clean in [v.lower() for v in values]:
                    words[i] = key
                    break

    return ' '.join(words)


def replace_terms_in_text_linear_search(text, dictionary):
    """
    Linear Search implementation
    Function to replace terms in a text using binary search logic.
    Args:
        text (str): The input text where replacements need to be made.
        dictionary (dict): A dictionary with keys as replacement terms 
                           and values as lists of terms to be replaced.
    Returns:
        str: The modified text after replacements.
    """
    for key, values in dictionary.items():
        # Iterate through all alternative words for each key in the dictionary
        for value in values:
            print(f"Replacing '{value}' with '{key}' in the text")
            # Use a regular expression to replace the exact word
            # 'r'\b' and '\b' ensure that only whole words are replaced
            # The re.IGNORECASE flag is used to make the search case-insensitive
            text = re.sub(r'\b' + re.escape(value) + r'\b', key, text, flags=re.IGNORECASE)
    return text

#if __name__ == "__main__":