import itertools
lst = [1, 2, 3]
permutations = list(itertools.permutations(lst))
print("Перестановки списка", lst, ":")
for perm in permutations:
    print(perm)