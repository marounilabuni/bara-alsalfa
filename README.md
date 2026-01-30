# برا السالفة - Flask Game

A Flask web application for the popular Arabic party game "برا السالفة" (Out of the Loop).

## Features

- **Player Setup**: Enter number of players and their names
- **Random Word Selection**: Automatically selects a random word from a predefined list
- **Secret Role Assignment**: One random player becomes "برا السالفة"
- **Sequential Word Reveal**: Each player views their word/role privately
- **Beautiful Arabic UI**: RTL support with modern gradient design

## How to Use

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment variables (create .env file)
# Add your OpenAI API key:
# OPENAI_API_KEY=your_api_key_here
```

### Running the App

```bash
# Run the Flask application
python app.py
```

The app will be available at `http://localhost:5000`

### Playing the Game

1. **Setup Phase**:
   - Enter the number of players (minimum 3)
   - (Optional) Check "استخدام GPT" to use AI-generated words
   - (Optional) Enter a topic for the word (e.g., طعام, رياضة)
   - Click "إنشاء حقول الأسماء" to generate name fields
   - Enter each player's name
   - Click "ابدأ اللعبة" to start

2. **Word Distribution Phase**:
   - Each player takes turns
   - Current player clicks "عرض الكلمة" to see their word
   - Either they see the secret word OR "أنت برا السالفة"
   - After viewing, click "اللاعب التالي" to pass to next player
   - Continue until all players have seen their words

3. **Game Phase**:
   - Players ask each other questions about the word
   - The goal is to identify who is "برا السالفة"
   - "برا السالفة" tries to blend in and guess the word

## Game Functions

### `get_term(topic=None, use_gpt=False)`
Returns a term for the game.
- If `use_gpt=True`: Uses GPT-4 to generate a fresh word
- If `use_gpt=False`: Returns a random term from the predefined list
- `topic` (optional): Specific topic for the word (e.g., "طعام", "رياضة")

### `get_word(player_index, total_players, term)`
Determines what each player sees:
- Returns `None` if the player is "برا السالفة"
- Returns the actual term for other players

### `get_gpt_word(topic=None)`
Python function that generates words using GPT-4:
- Takes optional `topic` parameter
- Sends message to GPT and gets the word
- Returns ONLY the word/term in Arabic as a string
- No additional text or explanations
- If topic is given, generates word related to that topic
- If no topic, generates any suitable word for the game

## Customization

Add more words to the game by editing the `TERMS` list in `app.py`:

```python
TERMS = [
    "قهوة",
    "سيارة",
    # Add your words here
]
```

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with gradient designs
- **Language Support**: Arabic (RTL)

## Requirements

- Python 3.7+
- Flask 3.0.0
- Werkzeug 3.0.1
- OpenAI API (for GPT word generation - optional)
- python-dotenv 1.0.0

## Testing GPT Word Generation

To test the GPT word generation function independently:

```bash
python test_gpt_word.py
```

This will generate sample words with and without topics to verify the function works correctly.

Enjoy playing برا السالفة! 🎮
