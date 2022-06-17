# Напишите функцию, которая проверяет, является ли
# данная строка палиндромом или нет, и возвращает результат проверки.

def palindrome(text):
    text = text.lower()
    text = text.replace(' ', '')
    if text == text[::-1]:
        return True
    else:
        return False


A = input()

print(palindrome(A))  # Вывод вариант №1

c = palindrome(A)     # Вывод вариант №2
print(c)


