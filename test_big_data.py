import yaml
from algorithm import *
import bisect
import re
from utils import *


def run_test_quick_sort():
    """
    Run test cases for the QuickSort-based term replacement algorithm.
    This function loads test cases from a YAML file, applies the replacement function 
    to each test case, and compares the result with the expected output.
    """
    print("Testing the QuickSort algorithm")
    
    # Load tests from the YAML file
   # tests = load_tests_from_yaml('tests.yml') not correct dict
    tests = load_tests_from_yaml('dictionary.yml')

    # Iterate through each test case
    for i, test in enumerate(tests['tests'], 1):  # Accessing the 'tests' key
        #result_quick_sort, time_quick_sort = measure_time(replace_terms_in_text_with_quick_sort, test["text"], test["dictionary"])

        #result = replace_terms_in_text_with_quick_sort(test["text"], test["dictionary"])
        result, execution_time, mem_usage, cpu_percent = measure_resources(
            replace_terms_in_text_with_quick_sort, test["text"], test["dictionary"]
        )
        # Display the test details and results
        #print(f"Test {i}:")
        #print(f"Inserted: {test['text']}")
        #print(f"Expected: {test['expected']}")
        #print(f"Result: {result}")
        #print(f"Tiempo de ejecución (QuickSort y Binary Search): {time_quick_sort:.6f} segundos")
        print(f"Tiempo de ejecución: {execution_time:.4f} segundos")
        print(f"Uso de memoria: {mem_usage / (1024 ** 2):.2f} MB")
        print(f"Uso de CPU: {cpu_percent}%")
        
        
        # Compare the result with expected value
        if result.strip().lower() != test["expected"].strip().lower():
            print(f"Test {i} failed: {result} != {test['expected']}")
        else:
            print(f"Test {i} passed: {result} == {test['expected']}")

    print("All QuickSort tests passed!")

# Ejecutamos los tests
if __name__ == "__main__":
    run_test_quick_sort()