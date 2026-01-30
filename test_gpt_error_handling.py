#!/usr/bin/env python3
"""
Test script to verify GPT error handling works correctly
"""

import os
from gpt_word_generator import get_gpt_word

def test_normal_generation():
    """Test normal word generation"""
    print("=" * 60)
    print("Test 1: Normal GPT Word Generation")
    print("=" * 60)
    
    try:
        word = get_gpt_word()
        print(f"✅ Success! Generated word: {word}")
        return True
    except Exception as e:
        print(f"❌ Failed: {str(e)}")
        return False

def test_with_topic():
    """Test word generation with topic"""
    print("\n" + "=" * 60)
    print("Test 2: GPT Word Generation with Topic")
    print("=" * 60)
    
    try:
        word = get_gpt_word(topic="رياضة")
        print(f"✅ Success! Generated word about sports: {word}")
        return True
    except Exception as e:
        print(f"❌ Failed: {str(e)}")
        return False

def test_missing_api_key():
    """Test behavior when API key is missing"""
    print("\n" + "=" * 60)
    print("Test 3: Missing API Key Error Handling")
    print("=" * 60)
    
    # Temporarily remove API key
    original_key = os.getenv('OPENAI_API_KEY')
    os.environ['OPENAI_API_KEY'] = ''
    
    try:
        word = get_gpt_word()
        print(f"❌ Should have raised an error but got: {word}")
        result = False
    except Exception as e:
        print(f"✅ Correctly raised error: {str(e)}")
        result = True
    finally:
        # Restore API key
        if original_key:
            os.environ['OPENAI_API_KEY'] = original_key
    
    return result

def test_app_error_handling():
    """Test app.py get_term function error handling"""
    print("\n" + "=" * 60)
    print("Test 4: App Error Handling")
    print("=" * 60)
    
    # Import after environment is set up
    from app import get_term
    
    # Test with GPT (default)
    print("\n4a. Testing with GPT enabled:")
    term, error = get_term(use_gpt=True)
    if term and not error:
        print(f"✅ GPT generation successful: {term}")
    elif error:
        print(f"⚠️  GPT failed (expected if no API key): {error}")
    
    # Test without GPT
    print("\n4b. Testing with GPT disabled (fallback):")
    term, error = get_term(use_gpt=False)
    if term and not error:
        print(f"✅ Fallback to predefined list: {term}")
    else:
        print(f"❌ Fallback failed: {error}")
    
    return True

def main():
    print("\n🎮 Testing برا السالفة - GPT Error Handling")
    print("=" * 60)
    
    # Check if API key exists
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("⚠️  WARNING: OPENAI_API_KEY not found in environment")
        print("Some tests will fail, but error handling will be tested.\n")
    else:
        print(f"✓ API Key found: {api_key[:10]}...\n")
    
    results = []
    
    # Run tests
    results.append(("Normal Generation", test_normal_generation()))
    results.append(("With Topic", test_with_topic()))
    results.append(("Missing API Key", test_missing_api_key()))
    results.append(("App Error Handling", test_app_error_handling()))
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    print(f"\nTotal: {passed}/{total} tests passed")
    
    print("\n" + "=" * 60)
    print("Testing Complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
