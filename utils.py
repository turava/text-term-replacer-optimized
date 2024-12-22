import yaml
import os
import time
import psutil

# Función para medir el tiempo de ejecución
def measure_time(func, *args, **kwargs):
    start_time = time.time()  # Capturamos el tiempo de inicio
    result = func(*args, **kwargs)  # Ejecutamos la función
    end_time = time.time()  # Capturamos el tiempo de finalización
    
    elapsed_time = end_time - start_time  # Calculamos el tiempo transcurrido
    return result, elapsed_time  # Devolvemos el resultado y el tiempo
def measure_resources(func, *args, **kwargs):
    # Medir el tiempo de ejecución
    start_time = time.time()

    # Medir uso de memoria y CPU
    process = psutil.Process(os.getpid())
    
    # Iniciar monitoreo de memoria
    mem_before = process.memory_info().rss  # Memoria antes de la ejecución

    # Ejecutar la función
    result = func(*args, **kwargs)

    # Medir uso de memoria después de la ejecución
    mem_after = process.memory_info().rss  # Memoria después de la ejecución
    mem_usage = mem_after - mem_before

    # Medir el tiempo de ejecución
    end_time = time.time()
    execution_time = end_time - start_time

    # Medir el uso de CPU
    cpu_percent = psutil.cpu_percent(interval=1)

    # Retornar los resultados
    return result, execution_time, mem_usage, cpu_percent
    
def load_tests_from_yaml(file_path):
    """ Function to load tests from a YAML file.
    Args:
        file_path (str): Path to the YAML file containing the tests.
    Returns:
        dict: A dictionary with the loaded test cases.
    """
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)  # Use safe_load to load data safely
