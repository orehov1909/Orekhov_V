start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

prime_numbers = []


for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime_numbers.append(num)

print("Простые числа в диапазоне от", start, "до", end, ":", prime_numbers)