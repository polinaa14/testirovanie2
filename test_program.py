import pytest

from program import (
    add,
    subtract,
    multiply,
    divide,
    power,
    count_words,
    count_characters,
    count_vowels,
    reverse_text,
    to_upper,
    kilometers_to_meters,
    meters_to_kilometers,
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    kilograms_to_grams
)


# Тесты калькулятора

def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(6, 7) == 42


def test_divide():
    assert divide(12, 3) == 4


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)


def test_power():
    assert power(2, 5) == 32


def test_negative_numbers():
    assert add(-2, -3) == -5
    assert multiply(-2, 4) == -8


def test_float_values():
    assert divide(7.5, 2.5) == 3


# Тесты анализатора текста

def test_count_words():
    assert count_words("один два три") == 3


def test_count_words_multiple_spaces():
    assert count_words("один   два") == 2


def test_count_characters():
    assert count_characters("abc") == 3


def test_count_vowels():
    assert count_vowels("Привет") == 2


def test_reverse_text():
    assert reverse_text("abc") == "cba"


def test_empty_text():
    assert count_words("") == 0
    assert count_characters("") == 0
    assert reverse_text("") == ""


def test_uppercase():
    assert to_upper("Привет") == "ПРИВЕТ"


def test_punctuation():
    assert count_words("Привет, мир!") == 2


# Тесты конвертера единиц

def test_km_to_m():
    assert kilometers_to_meters(2) == 2000


def test_m_to_km():
    assert meters_to_kilometers(3000) == 3


def test_c_to_f():
    assert celsius_to_fahrenheit(0) == 32


def test_f_to_c():
    assert fahrenheit_to_celsius(32) == 0


def test_kg_to_g():
    assert kilograms_to_grams(2.5) == 2500


def test_zero_values():
    assert kilometers_to_meters(0) == 0
    assert meters_to_kilometers(0) == 0


def test_negative_values():
    assert kilometers_to_meters(-1) == -1000
    assert kilograms_to_grams(-2) == -2000


def test_round_trip():
    assert meters_to_kilometers(kilometers_to_meters(3)) == 3
