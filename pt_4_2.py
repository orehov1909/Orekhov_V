string = input("Введите строку: ")
palindromes = []
for i in range(len(string)):
    for j in range(i + 1, len(string) + 1):
        substring = string[i:j]
        if substring == substring[:: - 1]:
            palindromes.append(substring)
            
print("Подстроки-палиндромы:", palindromes)