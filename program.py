# Калькулятор

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def power(a, b):
    return a ** b


# Анализатор текста

def count_words(text):
    return len(text.split())


def count_characters(text):
    return len(text)


def count_vowels(text):
    return sum(1 for ch in text.lower() if ch in "аеёиоуыэюя")


def reverse_text(text):
    return text[::-1]


def to_upper(text):
    return text.upper()


# Конвертер единиц

def kilometers_to_meters(km):
    return km * 1000


def meters_to_kilometers(m):
    return m / 1000


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def kilograms_to_grams(kg):
    return kg * 1000
