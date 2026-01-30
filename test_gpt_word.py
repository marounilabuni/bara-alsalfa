#!/usr/bin/env python3
"""
Test script for GPT word generation function
"""

from gpt_word_generator import get_gpt_word

def main():
    print("=" * 50)
    print("Testing GPT Word Generator for برا السالفة")
    print("=" * 50)
    
    # Test 1: Generate word without topic
    print("\n1. Generating random word (no topic):")
    word1 = get_gpt_word()
    print(f"   Result: {word1}")
    
    # Test 2: Generate word with specific topic
    print("\n2. Generating word with topic 'طعام' (food):")
    word2 = get_gpt_word(topic="طعام")
    print(f"   Result: {word2}")
    
    # Test 3: Generate word with different topic
    print("\n3. Generating word with topic 'رياضة' (sports):")
    word3 = get_gpt_word(topic="رياضة")
    print(f"   Result: {word3}")
    
    # Test 4: Generate word with another topic
    print("\n4. Generating word with topic 'حيوانات' (animals):")
    word4 = get_gpt_word(topic="حيوانات")
    print(f"   Result: {word4}")
    
    # Test 5: Multiple random words
    print("\n5. Generating 3 random words:")
    for i in range(3):
        word = get_gpt_word()
        print(f"   Word {i+1}: {word}")
    
    print("\n" + "=" * 50)
    print("All tests completed successfully!")
    print("=" * 50)

if __name__ == "__main__":
    main()
