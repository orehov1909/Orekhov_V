import csv
count = int(input("Сколько записей хотите добавить? "))
for i in range(count):
    book = input("Введите название книги: ")
    author = input("Введите имя автора: ")
    year = input("Введите год выпуска: ")
    with open("books.csv", "a", encoding="utf-8-sig", newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow([book, author, year])
s_author = input("Введите автора книги: ")
with open("books.csv", 'r', encoding="utf-8-sig", newline='') as file:
    reader = csv.reader(file, delimiter=";")
    next(reader)
    book = []
    for row in reader:
        if row[1] == s_author:
            book.append(row[0])
if book:
    print("Книга автора", s_author + ":", ",".join(book))
else:
    print("Нет книг автора", s_author)