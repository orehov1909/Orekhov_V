import itertools

def find_combinations(n, t):
    combinations = []
    for i in range(1, len(n) + 1):
        for combo in itertools.combinations(n, i):
            if sum(combo) == t:
                combinations.append(combo)
    return set(combinations)


numbers = [1, 2, 3, 4, 5]
target_sum = 9
c = find_combinations(numbers, target_sum)
print("Уникальные комбинации чисел", numbers, "с суммой", target_sum, ":", c)