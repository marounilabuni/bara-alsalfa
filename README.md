# برا السالفة - Flask Game

A Flask web application for the popular Arabic party game "برا السالفة" (Out of the Loop).

**🎉 Now Vercel-Ready!** This app uses frontend state management (no sessions), making it compatible with serverless platforms like Vercel, Netlify, Render, Railway, and more!

## Features

- **Player Setup**: Enter number of players and their names
- **AI Word Generation**: GPT-4 generates fresh, unique words (enabled by default)
- **Topic Selection**: Optional topic to guide word generation
- **Fallback System**: Uses predefined words if GPT fails or is disabled
- **Error Handling**: Clear error messages if word generation fails
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
   - **GPT is enabled by default** - generates fresh, unique words
   - (Optional) Enter a topic for the word (e.g., طعام, رياضة, حيوانات)
   - Uncheck GPT if you want to use predefined words instead
   - Click "إنشاء حقول الأسماء" to generate name fields
   - Enter each player's name
   - Click "ابدأ اللعبة" to start
   - If GPT fails, you'll see an error message - try again or disable GPT

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

### `get_term(topic=None, use_gpt=True)`
Returns a term for the game with error handling.
- **Default**: `use_gpt=True` - GPT is enabled by default
- If `use_gpt=True`: Uses GPT-4 to generate a fresh word
- If `use_gpt=False`: Returns a random term from the predefined list
- `topic` (optional): Specific topic for the word (e.g., "طعام", "رياضة")
- **Returns**: `(word, error)` tuple - word is None if error occurred

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

- **Backend**: Flask (Python) - Stateless API
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **State Management**: localStorage (no sessions!)
- **Styling**: Custom CSS with gradient designs
- **Language Support**: Arabic (RTL)
- **Deployment**: Vercel-ready (also works on Render, Railway, etc.)

## Requirements

- Python 3.7+
- Flask 3.0.0
- Werkzeug 3.0.1
- OpenAI API (for GPT word generation - optional)
- python-dotenv 1.0.0
- gunicorn 21.2.0 (for production deployment)

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for complete deployment instructions to:
- ✅ Vercel (serverless)
- ✅ Render (container)
- ✅ Railway (container)
- ✅ Fly.io (container)

**Quick Deploy to Vercel:**
```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel

# Add your OPENAI_API_KEY in Vercel dashboard
```

## Testing GPT Word Generation

### Basic Testing
To test the GPT word generation function independently:

```bash
python test_gpt_word.py
```

This will generate sample words with and without topics to verify the function works correctly.

### Error Handling Testing
To test error handling and edge cases:

```bash
python test_gpt_error_handling.py
```

This comprehensive test checks:
- Normal word generation
- Generation with topics
- Missing API key handling
- App-level error handling

## Error Handling

The app has robust error handling:

1. **GPT Generation Fails**: 
   - User sees a clear Arabic error message
   - Button returns to normal state
   - User can try again or disable GPT

2. **Missing API Key**:
   - Error message explains the issue
   - User is prompted to add API key or disable GPT

3. **Network Issues**:
   - Timeout after 10 seconds
   - User-friendly error message
   - Can retry immediately

4. **Loading States**:
   - Button shows "جاري توليد الكلمة..." while waiting
   - Button is disabled during generation
   - Prevents double-submission

Enjoy playing برا السالفة! 🎮
