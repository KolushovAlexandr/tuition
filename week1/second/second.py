import itertools

numbers = [1, 2, 2, 3, 5, 2, 6, 77, 77, 89, 77]
for item, group in itertools.groupby(numbers):
    print(f'{item} - {len(list(group))}')