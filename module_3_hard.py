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

    return total_sum, total_length


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hi",
    ((), [{(2, 'Name', ('Zero', 35))}])
]

result = calculate_structure_sum(*data_structure)
print(result)
