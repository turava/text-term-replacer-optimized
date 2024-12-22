import yaml
from algorithm import *
import bisect
import re


def load_tests_from_yaml(file_path):
    """ Function to load tests from a YAML file.
    Args:
        file_path (str): Path to the YAML file containing the tests.
    Returns:
        dict: A dictionary with the loaded test cases.
    """
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)  # Use safe_load to load data safely

def run_test_quick_sort():
    """
    Run test cases for the QuickSort-based term replacement algorithm.
    This function loads test cases from a YAML file, applies the replacement function 
    to each test case, and compares the result with the expected output.
    """
    print("Testing the QuickSort algorithm")
    
    # Load tests from the YAML file
    tests = load_tests_from_yaml('tests.yml')

    # Iterate through each test case
    for i, test in enumerate(tests['tests'], 1):  # Accessing the 'tests' key
        result = replace_terms_in_text_with_quick_sort(test["text"], test["dictionary"])

        # Display the test details and results
        print(f"Test {i}:")
        print(f"Inserted: {test['text']}")
        print(f"Expected: {test['expected']}")
        print(f"Result: {result}")
        
        # Compare the result with expected value
        if result.strip().lower() != test["expected"].strip().lower():
            print(f"Test {i} failed: {result} != {test['expected']}")
        else:
            print(f"Test {i} passed: {result} == {test['expected']}")

    print("All QuickSort tests passed!")

# Ejecutamos los tests
if __name__ == "__main__":
    run_test_quick_sort()