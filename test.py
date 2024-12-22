import yaml
import psutil
import os
from algorithm import *
from utils import *
import time

def run_test_linear_search():
    """
    Function to run and validate test cases for the binary search algorithm.

    This function loads test cases from a YAML file, applies the replacement 
    function to each test case, and compares the result with the expected output.
    """
    print("Testing the algorithm")
    # Load tests from the YAML file
    #tests = load_tests_from_yaml('tests.yml') Not correct dict
    tests = load_tests_from_yaml('dictionary.yml')

    # Iterate through each test case
    for i, test in enumerate(tests['tests'], 1): # Ensure you access the 'tests' key correctly
        #result_linear, time_linear = measure_time(replace_terms_in_text_linear_search, test["text"], test["dictionary"])
        result, execution_time, mem_usage, cpu_percent = measure_resources(
            replace_terms_in_text_linear_search, test["text"], test["dictionary"]
        )
        result = replace_terms_in_text_linear_search(test["text"], test["dictionary"])

        # Display the test details and results
        #print(f"Test {i}:")
        #print(f"Inserted: {test['text']}")
        #print(f"Expected: {test['expected']}")
        #print(f"Result: {result}")
        print(f"Tiempo de ejecución: {execution_time:.4f} segundos")
        print(f"Uso de memoria: {mem_usage / (1024 ** 2):.2f} MB")
        print(f"Uso de CPU: {cpu_percent}%")
        
        if result.strip().lower() != test["expected"].strip().lower():
            print(f"Test {i} failed: {result} != {test['expected']}")
        else:
            print(f"Test {i} passed: {result} == {test['expected']}")

    print("All Linear search tests passed!")

# Ejecutamos los tests
if __name__ == "__main__":
    run_test_linear_search()
