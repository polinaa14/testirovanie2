"""
Единая программа для практической работы №2.
5 участников, 5 модулей, минимум 5 функций в каждом.
"""

import random
import string


# Участник 1: конвертер единиц
def km_to_miles(km): return km * 0.621371
def miles_to_km(miles): return miles / 0.621371
def celsius_to_fahrenheit(c): return c * 9 / 5 + 32
def fahrenheit_to_celsius(f): return (f - 32) * 5 / 9
def kg_to_pounds(kg): return kg * 2.20462


# Участник 2: генератор паролей
def password_alphabet(): return string.ascii_letters + string.digits
def generate_password(length=12):
    if length < 1:
        raise ValueError("Длина пароля должна быть положительной")
    alphabet = password_alphabet()
    return "".join(random.choice(alphabet) for _ in range(length))
def password_has_digit(password): return any(ch.isdigit() for ch in password)
def password_has_uppercase(password): return any(ch.isupper() for ch in password)
def password_strength(password):
    score = sum([
        len(password) >= 8,
        password_has_digit(password),
        password_has_uppercase(password)
    ])
    return "сильный" if score == 3 else "средний" if score == 2 else "слабый"


# Участник 3: анализатор текста
def count_words(text): return len(text.split())
def count_characters(text): return len(text)
def count_vowels(text):
    return sum(ch.lower() in "аеёиоуыэюяaeiou" for ch in text)
def count_sentences(text): return sum(text.count(x) for x in ".!?")
def most_common_word(text):
    words = [w.strip(string.punctuation).lower() for w in text.split()]
    words = [w for w in words if w]
    return max(set(words), key=words.count) if words else None


# Участник 4: матрицы
def matrix_add(a, b):
    if len(a) != len(b) or any(len(x) != len(y) for x, y in zip(a, b)):
        raise ValueError("Размеры матриц не совпадают")
    return [[x + y for x, y in zip(r1, r2)] for r1, r2 in zip(a, b)]
def matrix_transpose(matrix): return [list(row) for row in zip(*matrix)] if matrix else []
def matrix_scalar_multiply(matrix, scalar):
    return [[x * scalar for x in row] for row in matrix]
def matrix_trace(matrix):
    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("Матрица должна быть квадратной")
    return sum(matrix[i][i] for i in range(len(matrix)))
def matrix_determinant_2x2(matrix):
    if len(matrix) != 2 or any(len(row) != 2 for row in matrix):
        raise ValueError("Нужна матрица 2x2")
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


# Участник 5: фильтр чисел
def even_numbers(numbers): return [n for n in numbers if n % 2 == 0]
def odd_numbers(numbers): return [n for n in numbers if n % 2 != 0]
def positive_numbers(numbers): return [n for n in numbers if n > 0]
def negative_numbers(numbers): return [n for n in numbers if n < 0]
def numbers_above(numbers, limit): return [n for n in numbers if n > limit]


def main():
    while True:
        print("\n===== УНИВЕРСАЛЬНЫЙ ПОМОЩНИК =====")
        print("1. Конвертер")
        print("2. Генератор паролей")
        print("3. Анализатор текста")
        print("4. Матрицы")
        print("5. Фильтр чисел")
        print("0. Выход")
        choice = input("Выберите раздел: ")

        try:
            if choice == "1":
                value = float(input("Введите км: "))
                print("Мили:", km_to_miles(value))
            elif choice == "2":
                length = int(input("Длина пароля: "))
                p = generate_password(length)
                print("Пароль:", p)
                print("Сложность:", password_strength(p))
            elif choice == "3":
                text = input("Введите текст: ")
                print("Слов:", count_words(text))
                print("Символов:", count_characters(text))
                print("Гласных:", count_vowels(text))
                print("Предложений:", count_sentences(text))
                print("Частое слово:", most_common_word(text))
            elif choice == "4":
                m = [[1, 2], [3, 4]]
                print("Матрица:", m)
                print("Транспонированная:", matrix_transpose(m))
                print("Умножение на 2:", matrix_scalar_multiply(m, 2))
                print("След:", matrix_trace(m))
                print("Определитель:", matrix_determinant_2x2(m))
            elif choice == "5":
                numbers = list(map(int, input("Числа через пробел: ").split()))
                limit = int(input("Порог: "))
                print("Чётные:", even_numbers(numbers))
                print("Нечётные:", odd_numbers(numbers))
                print("Положительные:", positive_numbers(numbers))
                print("Отрицательные:", negative_numbers(numbers))
                print("Выше порога:", numbers_above(numbers, limit))
            elif choice == "0":
                break
            else:
                print("Неверный пункт.")
        except ValueError as e:
            print("Ошибка:", e)


if __name__ == "__main__":
    main()