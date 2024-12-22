import re
def binary_search(term, variants):
    """
    Perform binary search to find a term in the list of variants.

    :param term: Term to search for.
    :param variants: Alphabetically sorted list of variants.
    :return: True if the term is in the list, False otherwise.
    """
    low, high = 0, len(variants) - 1

    while low <= high:
        mid = (low + high) // 2
        if variants[mid] == term:
            return True
        elif variants[mid] < term:
            low = mid + 1
        else:
            high = mid - 1

    return False


def replace_terms_in_text(text, dictionary):
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