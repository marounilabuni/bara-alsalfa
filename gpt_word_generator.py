import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_gpt_word(topic=None):
    """
    Generate a word/term for برا السالفة game using GPT.
    
    Args:
        topic (str, optional): Specific topic for the word. If None, generates any suitable word.
    
    Returns:
        str: A single word/term in Arabic suitable for the game
    
    Raises:
        Exception: If API call fails or API key is missing
    """
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        raise Exception("OPENAI_API_KEY not found in environment variables")
    
    try:
        client = OpenAI(api_key=api_key)
        
        if topic:
            prompt = f"""Generate ONE single word or short term in Arabic (2-3 words max) for the game "برا السالفة" on the topic: {topic}

The word should be:
- Common and familiar to most people
- Not too easy or too hard to describe without saying it
- Suitable for a guessing game

Return ONLY the word/term in Arabic, nothing else. No explanations, no punctuation, no additional text."""
        else:
            prompt = """Generate ONE single word or short term in Arabic (2-3 words max) for the game "برا السالفة"

The word should be:
- Common and familiar to most people
- Not too easy or too hard to describe without saying it
- Suitable for a guessing game
- Can be from any category (places, objects, activities, professions, food, etc.)

Return ONLY the word/term in Arabic, nothing else. No explanations, no punctuation, no additional text."""
        
        prompt += "\n\nThe word should be in Arabic. not too describing"
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a word generator for Arabic party games. Return ONLY the requested word with no additional text."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.9,
            max_tokens=20,
            timeout=10
        )
        
        word = response.choices[0].message.content.strip()
        
        if not word:
            raise Exception("GPT returned empty response")
        
        return word
        
    except Exception as e:
        # Re-raise with more context
        raise Exception(f"Failed to generate word with GPT: {str(e)}")


if __name__ == "__main__":
    # Test the function
    print("Testing word generation:")
    print(f"Random word: {get_gpt_word()}")
    print(f"Food topic: {get_gpt_word('طعام')}")
    print(f"Sports topic: {get_gpt_word('رياضة')}")
