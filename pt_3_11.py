a = str(input("введите строку: "))
p = {c: a.count(c) for c in a if c in "йцукенгшщзхъфывапролджэячсмитьбю"}
print(p)