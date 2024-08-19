def calculate_structure_sum(*args):
    total_sum = 0
    total_length = 0

    for item in args:
        if isinstance(item, (int, float)):
            total_sum += item
        elif isinstance(item, str):
            total_length += len(item)
        elif isinstance(item, (list, tuple, set)):
            inner_sum, inner_length = calculate_structure_sum(*item)
            total_sum += inner_sum
            total_length += inner_length
        elif isinstance(item, dict):
            for key, value in item.items():
                if isinstance(key, (int, float)):
                    total_sum += key
                elif isinstance(key, str):
                    total_length += len(key)
                inner_sum, inner_length = calculate_structure_sum(value)
                total_sum += inner_sum
                total_length += inner_length

    return total_sum, total_length  # Возвращаем кортеж (сумма, длина)


data_structure = [
    [1, 2, 3],  # Сумма: 6
    {'a': 4, 'b': 5},  # Сумма: 9
    (6, {'cube': 7, 'drum': 8}),  # Сумма: 21
    "Hello",  # Длина: 5
    ((), [{(2, 'Urban', ('Urban2', 35))}])  # Сумма: 2 + 35 = 37
]

result_sum, result_length = calculate_structure_sum(*data_structure)
total_result = result_sum + result_length
print(total_result)
