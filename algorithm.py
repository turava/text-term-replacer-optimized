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

    def replace_word(word):
        """Replaces the word based on the dictionary."""
        word_clean = re.sub(r'\W', '', word).lower()  # Clean word for comparison
        if binary_search(words_to_replace, word_clean):
            for key, values in dictionary.items():
                if word_clean in [v.lower() for v in values]:
                    return key  # Return the replacement term
        return word  # If no replacement, return the original word

    # Use regular expression to match words, punctuation, and spaces separately
    words_and_symbols = re.findall(r'\w+|[^\w\s]+|\s+', text)  # Matches words, punctuation, and spaces separately

    # Replace words where applicable
    replaced_words = []
    for word in words_and_symbols:
        if word.strip() and not word.isspace():  # Only replace if it's a word
            replaced_words.append(replace_word(word))
        else:
            replaced_words.append(word)  # Keep spaces and punctuation unchanged

    # Reassemble the text with spaces and punctuation
    return ''.join(replaced_words)



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
            #print(f"Replacing '{value}' with '{key}' in the text")
            # Use a regular expression to replace the exact word
            # 'r'\b' and '\b' ensure that only whole words are replaced
            # The re.IGNORECASE flag is used to make the search case-insensitive
            text = re.sub(r'\b' + re.escape(value) + r'\b', key, text, flags=re.IGNORECASE)
    return text

#if __name__ == "__main__":