# Практическая работа №2 — Модульное и мутационное тестирование



## О работе

3 модуля на Python, каждый тестировал чужой модуль (независимо). В каждый модуль намеренно внесена ошибка. **24 теста** (pytest). Все ошибки найдены и исправлены. Мутационное тестирование: эффективность **85,7 % → 100 %**.

---

## Модули и ошибки

| Модуль | Функции | Ошибка |
|--------|---------|--------|
| Калькулятор | add, subtract, multiply, divide, power | `multiply` — сложение вместо умножения |
| Анализатор текста | count_words, count_characters, count_vowels, reverse_text, to_upper | `split(" ")` вместо `split()` |
| Конвертер единиц | km↔m, °C↔°F, kg→g | коэффициент 100 вместо 1000 |

---

## Код

```python
# Калькулятор
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0: raise ZeroDivisionError("division by zero")
    return a / b
def power(a, b): return a ** b

# Анализатор текста
def count_words(text): return len(text.split())
def count_characters(text): return len(text)
def count_vowels(text): return sum(1 for ch in text.lower() if ch in "aeiouyаоуыэеёиюя")
def reverse_text(text): return text[::-1]
def to_upper(text): return text.upper()

# Конвертер единиц
def kilometers_to_meters(km): return km * 1000
def meters_to_kilometers(m): return m / 1000
def celsius_to_fahrenheit(c): return c * 9 / 5 + 32
def fahrenheit_to_celsius(f): return (f - 32) * 5 / 9
def kilograms_to_grams(kg): return kg * 1000
```

```python
# Пример тестов
def test_add(): assert add(2, 3) == 5
def test_multiply(): assert multiply(6, 7) == 42
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError): divide(5, 0)
def test_negative_numbers():
    assert add(-2, -3) == -5
    assert multiply(-2, 4) == -8
```

---

## Итоги

| Показатель | Значение |
|------------|----------|
| Модулей / функций / тестов | 3 / 15 / 24 |
| Найдено дефектов | 3 |
| Покрытие функций | 100 % |
| Мутантов уничтожено | 6/7 → **7/7** |
| Эффективность | 85,7 % → **100 %** |

**Вывод:** мутационное тестирование выявило пробел (нет теста на отрицательные значения) — после добавления все мутанты уничтожены.

**GitHub:** https://github.com/polinaa14/testirovanie2
