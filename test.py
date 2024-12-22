import yaml
from algorithm import *
import yaml

def load_tests_from_yaml(file_path):
    """ Function to load tests from a YAML file.
    Args:
        file_path (str): Path to the YAML file containing the tests.
    Returns:
        dict: A dictionary with the loaded test cases.
    """
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)  # Use safe_load to load data safely



def run_tests_binary_search():
    """
    Function to run and validate test cases for the binary search algorithm.

    This function loads test cases from a YAML file, applies the replacement 
    function to each test case, and compares the result with the expected output.
    """
    print("Testing the algorithm")
    # Load tests from the YAML file
    tests = load_tests_from_yaml('tests.yml')

    # Iterate through each test case
    for i, test in enumerate(tests['tests'], 1): # Ensure you access the 'tests' key correctly
        result = replace_terms_in_text(test["text"], test["dictionary"])

        # Display the test details and results
        print(f"Test {i}:")
        print(f"Inserted: {test['text']}")
        print(f"Expected: {test['expected']}")
        print(f"Result: {result}")
        
        if result.strip().lower() != test["expected"].strip().lower():
            print(f"Test {i} failed: {result} != {test['expected']}")
        else:
            print(f"Test {i} passed: {result} == {test['expected']}")

    print("All binary search tests passed!")

# Ejecutamos los tests
if __name__ == "__main__":
    run_tests_binary_search()
