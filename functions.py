"""Utility functions for the Python exercises."""

import math
import re


def is_palindrome(text: str) -> bool:
    """Return whether text reads the same forwards and backwards."""
    normalized = "".join(character for character in text.casefold()
                         if not character.isspace())
    return normalized == normalized[::-1]


def fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number."""
    if n < 0:
        raise ValueError("n must be non-negative")

    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, previous + current
    return previous


def count_vowels(text: str) -> int:
    """Return the number of vowels in text, including Polish vowels."""
    vowels = set("aeiouyąęó")
    return sum(character in vowels for character in text.casefold())


def calculate_discount(price: float, discount: float) -> float:
    """Return price after applying a discount between zero and one."""
    if not 0 <= discount <= 1:
        raise ValueError("discount must be between 0 and 1")
    return price * (1 - discount)


def flatten_list(nested_list: list) -> list:
    """Return a list with all nested lists recursively flattened."""
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened


def word_frequencies(text: str) -> dict:
    """Return case-insensitive word frequencies without punctuation."""
    words = re.findall(r"[^\W_]+(?:['’][^\W_]+)*", text.casefold(),
                       flags=re.UNICODE)
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


def is_prime(n: int) -> bool:
    """Return whether n is a prime number."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for divisor in range(3, math.isqrt(n) + 1, 2):
        if n % divisor == 0:
            return False
    return True
