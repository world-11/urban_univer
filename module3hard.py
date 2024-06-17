data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = 0

def calculate_structure_sum(list_):
    sum_ = 0
    if isinstance(list_, int):
        sum_ += list_
        return sum_
    for i in list_:
        if isinstance(i, int):
            sum_ += i
        elif isinstance(i, str):
            sum_ += len(i)
        elif isinstance(i, dict):
            for key, value in i.items():
                sum_ += calculate_structure_sum(key) + calculate_structure_sum(value)
        elif isinstance(i, set) or isinstance(i, list) or isinstance(i, tuple):
                sum_ += calculate_structure_sum(i)
    return sum_


result = calculate_structure_sum(data_structure)
print(result)