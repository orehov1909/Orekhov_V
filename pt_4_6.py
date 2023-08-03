def rot13(string):
    result = ""
    for char in string:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + 13) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + 13) % 26 + 97)
        else:
            result += char
    return result


s = input("Введите строку для кодирования: ")
encoded_string = rot13(s)
print("Закодированная строка:", encoded_string)