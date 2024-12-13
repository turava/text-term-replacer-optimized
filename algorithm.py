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


def replace_terms_with_binary_search(text, dictionary):
    # Usamos un bucle para recorrer el diccionario y reemplazar las palabras en el texto
    for key, values in dictionary.items():
        # Recorremos todas las palabras alternativas para cada clave en el diccionario
        for value in values:
            print(f"Replacing '{value}' with '{key}' in the text")
            # Usamos una expresión regular para reemplazar la palabra exacta
            # 'r'\b' y '\b' aseguran que solo se reemplacen palabras completas
            # La flag re.IGNORECASE se usa para hacer la búsqueda insensible a mayúsculas/minúsculas
            text = re.sub(r'\b' + re.escape(value) + r'\b', key, text, flags=re.IGNORECASE)
    return text

#if __name__ == "__main__":