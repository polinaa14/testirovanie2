import pytest

from program import (
    km_to_miles, miles_to_km, celsius_to_fahrenheit, fahrenheit_to_celsius,
    kg_to_pounds, generate_password, password_has_digit, password_has_uppercase,
    password_strength, count_words, count_characters, count_vowels,
    count_sentences, most_common_word, matrix_add, matrix_transpose,
    matrix_scalar_multiply, matrix_trace, matrix_determinant_2x2,
    even_numbers, odd_numbers, positive_numbers, negative_numbers,
    numbers_above
)


def test_converter():
    assert km_to_miles(1) == pytest.approx(0.621371)
    assert miles_to_km(1) == pytest.approx(1.609344)
    assert celsius_to_fahrenheit(0) == 32
    assert fahrenheit_to_celsius(32) == 0
    assert kg_to_pounds(1) == pytest.approx(2.20462)


def test_password():
    p = generate_password(10)
    assert len(p) == 10
    assert password_has_digit("abc1")
    assert password_has_uppercase("Abc")
    assert password_strength("Abc12345") == "сильный"


def test_password_error():
    with pytest.raises(ValueError):
        generate_password(0)


def test_text():
    text = "Привет мир. Привет!"
    assert count_words(text) == 4
    assert count_characters(text) == len(text)
    assert count_vowels(text) > 0
    assert count_sentences(text) == 2
    assert most_common_word(text) == "привет"


def test_empty_text():
    assert count_words("") == 0
    assert most_common_word("") is None


def test_matrix():
    assert matrix_add([[1, 2]], [[3, 4]]) == [[4, 6]]
    assert matrix_transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
    assert matrix_scalar_multiply([[1, 2]], 3) == [[3, 6]]
    assert matrix_trace([[1, 2], [3, 4]]) == 5
    assert matrix_determinant_2x2([[1, 2], [3, 4]]) == -2


def test_matrix_error():
    with pytest.raises(ValueError):
        matrix_determinant_2x2([[1, 2, 3]])


def test_filter():
    n = [-3, -2, 0, 1, 2, 5]
    assert even_numbers(n) == [-2, 0, 2]
    assert odd_numbers(n) == [-3, 1, 5]
    assert positive_numbers(n) == [1, 2, 5]
    assert negative_numbers(n) == [-3, -2]
    assert numbers_above(n, 1) == [2, 5]