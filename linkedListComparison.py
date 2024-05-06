import linkedlist
import time
import random
import psutil
import os
import numpy as np

initial_value = 0
max_generated_numbers = 100000
stats_avltree = []
stats = []
worst_case = []

for i in range(0, 10):
    nums = list(range(initial_value, max_generated_numbers))
    random.shuffle(nums)
    for j in range(0, 100):
        initial_mem = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2
        ll = linkedlist.LinkedList()
        for i in nums:
            ll.insertAtBegin(i)
        start_time = time.time()
        found_random = ll.sequentialSearch(random.randint(0, max_generated_numbers))
        end_mem = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2
        end_time = time.time()
        elapsed_time = end_time - start_time
        stats.append({'time_elapsed': elapsed_time, 'mem_used': end_mem - initial_mem, 'comparison_count': found_random[1]})
    for k in range (0, 3):
        initial_mem = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2
        ll = linkedlist.LinkedList()
        for i in nums:
            ll.insertAtBegin(i)
        start_time = time.time()
        found_random = ll.sequentialSearch(1000000000)
        end_mem = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2
        end_time = time.time()
        elapsed_time = end_time - start_time
        worst_case.append({'time_elapsed': elapsed_time, 'mem_used': end_mem - initial_mem, 'comparison_count': found_random[1]})
    
    # Calculando média e desvio padrão para os dados em stats
    time_elapsed_list = [data['time_elapsed'] for data in stats]
    mem_used_list = [data['mem_used'] for data in stats]
    comparison_count_list = [data['comparison_count'] for data in stats]

    time_elapsed_mean = np.mean(time_elapsed_list)
    time_elapsed_std = np.std(time_elapsed_list)

    mem_used_mean = np.mean(mem_used_list)
    mem_used_std = np.std(mem_used_list)

    comparison_count_mean = np.mean(comparison_count_list)
    comparison_count_std = np.std(comparison_count_list)

    print("\nStats Mean and Standard Deviation:")
    print("Time Elapsed - Mean:", time_elapsed_mean, "Std Dev:", time_elapsed_std)
    print("Memory Used - Mean:", mem_used_mean, "Std Dev:", mem_used_std)
    print("Comparison Count - Mean:", comparison_count_mean, "Std Dev:", comparison_count_std)

    # Calculando média e desvio padrão para os dados em worst_case
    time_elapsed_list = [data['time_elapsed'] for data in worst_case]
    mem_used_list = [data['mem_used'] for data in worst_case]
    comparison_count_list = [data['comparison_count'] for data in worst_case]

    time_elapsed_mean = np.mean(time_elapsed_list)
    time_elapsed_std = np.std(time_elapsed_list)

    mem_used_mean = np.mean(mem_used_list)
    mem_used_std = np.std(mem_used_list)

    comparison_count_mean = np.mean(comparison_count_list)
    comparison_count_std = np.std(comparison_count_list)

    print("\nWorst Case Mean and Standard Deviation:")
    print("Time Elapsed - Mean:", time_elapsed_mean, "Std Dev:", time_elapsed_std)
    print("Memory Used - Mean:", mem_used_mean, "Std Dev:", mem_used_std)
    print("Comparison Count - Mean:", comparison_count_mean, "Std Dev:", comparison_count_std)
    max_generated_numbers += 100000