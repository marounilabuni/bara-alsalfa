#!/usr/bin/env python3
"""
Example usage of the get_gpt_word function
"""

from gpt_word_generator import get_gpt_word

# Example 1: Get a random word (any topic)
print("Example 1: Random word")
word = get_gpt_word()
print(f"Generated word: {word}")
print()

# Example 2: Get a word about food
print("Example 2: Word about food")
word = get_gpt_word(topic="طعام")
print(f"Generated word: {word}")
print()

# Example 3: Get a word about sports
print("Example 3: Word about sports")
word = get_gpt_word(topic="رياضة")
print(f"Generated word: {word}")
print()

# Example 4: Get a word about places
print("Example 4: Word about places")
word = get_gpt_word(topic="أماكن")
print(f"Generated word: {word}")
print()

# Example 5: Get multiple random words
print("Example 5: Generate 5 random words")
for i in range(5):
    word = get_gpt_word()
    print(f"{i+1}. {word}")
