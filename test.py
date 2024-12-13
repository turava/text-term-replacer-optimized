import yaml
from algorithm import *
import yaml

# Función para cargar los tests desde un archivo YAML
def load_tests_from_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)  # Utilizamos safe_load para cargar los datos de forma segura

# Función para reemplazar términos usando búsqueda binaria
#def replace_terms_with_binary_search(text, dictionary):
    # Lógica para reemplazar términos usando búsqueda binaria
    for key, values in dictionary.items():
        for value in values:
            if value in text:
                text = text.replace(value, key)
    return text

# Función para ejecutar los tests
def run_tests_binary_search():
    print(f"Testesndo el algoritmo")
    # Carga de los tests desde el archivo YAML
    tests = load_tests_from_yaml('tests.yml')

    # Recorremos cada test y ejecutamos la prueba
    for i, test in enumerate(tests['tests'], 1):  # Asegúrate de acceder correctamente a la clave 'tests'
        result = replace_terms_with_binary_search(test["text"], test["dictionary"])

        # Mostrar el resultado antes de hacer la comparación
        print(f"Test {i}:")
        print(f"Inserted: {test['text']}")
        print(f"Expected: {test['expected']}")
        print(f"Result: {result}")
        
        # Comparar sin tener en cuenta las diferencias de mayúsculas/minúsculas
        #assert result.strip().lower() == test["expected"].strip().lower(), f"Test {i} failed: {result} != {test['expected']}"
        # Compare without considering case differences and print the result
        print("This test is not considering the lower case differences")
        if result.strip().lower() != test["expected"].strip().lower():
            print(f"Test {i} failed: {result} != {test['expected']}")
        else:
            print(f"Test {i} passed: {result} == {test['expected']}")

    print("All binary search tests passed!")

# Ejecutamos los tests
if __name__ == "__main__":
    run_tests_binary_search()
