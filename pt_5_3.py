import csv
z = ["Книга", "Автор", "Год выпуска"]
books = [
    ["Робинзок Крузо", "Даниэль Дефо", "1719"],
    ["Капитанская дочка", "А.С. Пушкин", "1836"],
    ["Герой нашего времени", "М.Ю.Лермонтов", "1840"],
    ["Судьба Человека", "М.Шолохов", "1956"],
    ["Мцыри", "М.Ю.Лермонтов", "1840"],
]
with open("books.csv", "w", encoding="utf-8-sig", newline='') as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(z)
for book in books:
    with open("books.csv", "a", encoding="utf-8-sig", newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(
            book
        )