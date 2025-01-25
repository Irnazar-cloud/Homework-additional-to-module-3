def calculate_structure_sum(*args):
    sum_ = 0
    first = args[0]
    args = args[1:]
    if isinstance(first, list) or isinstance(first, tuple) or isinstance(first, set):
        args = list(args)
        for i in first:
            args.append(i)
    elif isinstance(first, dict):
        args = list(args)
        for j, k in first.items():
            args.extend([j, k])
    elif isinstance(first, str):
        sum_ =+ len(first)
    elif isinstance(first, int):
        sum_ =+ first
    if len(args) == 0:
        return sum_
    return sum_ + calculate_structure_sum(*args)
data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(data_structure)
print(result)
