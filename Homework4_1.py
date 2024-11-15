import random
import timeit
import heapq
# Алгоритм сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Алгоритм сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Timsort (використовуємо вбудований sorted)
def timsort(arr):
    return sorted(arr)

# Генерація наборів даних
def generate_data(size, case="random"):
    if case == "random":
        return [random.randint(1, 10000) for _ in range(size)]
    elif case == "sorted":
        return list(range(size))
    elif case == "reversed":
        return list(range(size, 0, -1))
    elif case == "nearly_sorted":
        arr = list(range(size))
        for _ in range(size // 10):  # 10% елементів перемішано
            i, j = random.sample(range(size), 2)
            arr[i], arr[j] = arr[j], arr[i]
        return arr

# Вимірювання часу виконання
def measure_time(func, arr):
    return timeit.timeit(lambda: func(arr.copy()), number=1)

# Об'єднання k відсортованих списків
def merge_k_lists(lists):
    return list(heapq.merge(*lists))

# Набори даних для тестування
sizes = [100, 1000, 5000, 10000]
cases = ["random", "sorted", "reversed", "nearly_sorted"]
results = {}

# Тестування алгоритмів на різних наборах даних
for case in cases:
    results[case] = {"insertion_sort": [], "merge_sort": [], "timsort": []}
    for size in sizes:
        data = generate_data(size, case)
        results[case]["insertion_sort"].append(measure_time(insertion_sort, data))
        results[case]["merge_sort"].append(measure_time(merge_sort, data))
        results[case]["timsort"].append(measure_time(timsort, data))

results

print(results.items())

# Тест об'єднання k відсортованих списків
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print(merged_list)

# Збереження результатів у файл
results_path = "/Users/jurek/Desktop/goit-algo-hw-04/results/results.txt"

with open(results_path, "w") as file:
    for case, case_results in results.items():
        file.write(f"Case: {case}\n")
        for algo, times in case_results.items():
            file.write(f"  {algo}: {times}\n")
        file.write("\n")

results_path