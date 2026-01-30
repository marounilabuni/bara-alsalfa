from flask import Flask, render_template, request, jsonify, session
import random
import os
from gpt_word_generator import get_gpt_word

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Game words/terms in Arabic (fallback list)
TERMS = [
    "قهوة",
    "سيارة",
    "مدرسة",
    "مطار",
    "مطعم",
    "سينما",
    "بحر",
    "جبل",
    "كتاب",
    "هاتف",
    "كمبيوتر",
    "مستشفى",
    "فندق",
    "حديقة",
    "ملعب",
    "سوق",
    "مكتبة",
    "جامعة",
    "شاطئ",
    "صحراء"
]

def get_term(topic=None, use_gpt=True):
    """
    Get a term for the game.
    
    Args:
        topic (str, optional): Specific topic for the word
        use_gpt (bool): If True, use GPT to generate word. If False, use predefined list
    
    Returns:
        tuple: (word, error_message) - error_message is None if successful
    """
    if use_gpt:
        try:
            word = get_gpt_word(topic)
            return (word, None)
        except Exception as e:
            error_msg = str(e)
            print(f"Error generating word with GPT: {error_msg}")
            # Return error instead of fallback
            return (None, error_msg)
    else:
        return (random.choice(TERMS), None)

def get_word(player_index, total_players, term):
    """
    Get the word for a specific player
    Returns the term or indicates they are 'bara alsalfe'
    """
    bara_index = random.randint(0, total_players - 1)
    
    if player_index == bara_index:
        return None  # This player is "bara alsalfe"
    else:
        return term

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    data = request.json
    num_players = int(data.get('num_players', 3))
    player_names = data.get('player_names', [])
    use_gpt = data.get('use_gpt', True)  # Default to True
    topic = data.get('topic', None)
    
    print('--------------------------------')
    print(f"Topic: {topic}")
    print(f"Use GPT: {use_gpt}")
    print(f"Player Names: {player_names}")
    print(f"Number of Players: {num_players}")
    print('--------------------------------')
    # Generate the term for this game
    term, error = get_term(topic=topic, use_gpt=use_gpt)
    
    # If GPT failed and use_gpt was True, return error
    if term is None and error:
        return jsonify({
            'success': False,
            'error': 'فشل توليد الكلمة باستخدام GPT. الرجاء المحاولة مرة أخرى أو إلغاء تفعيل GPT.',
            'error_details': error
        }), 500
    
    # Randomly select who is "bara alsalfe"
    bara_index = random.randint(0, num_players - 1)
    
    # Store game state in session
    session['term'] = term
    session['bara_index'] = bara_index
    session['player_names'] = player_names
    session['num_players'] = num_players
    session['current_player'] = 0
    
    return jsonify({
        'success': True,
        'message': 'Game started!',
        'current_player': 0,
        'player_name': player_names[0]
    })

@app.route('/get_player_word', methods=['POST'])
def get_player_word():
    # Check if game session exists
    if 'player_names' not in session or not session.get('player_names'):
        return jsonify({
            'error': 'No game session found',
            'redirect': True
        }), 400
    
    data = request.json
    player_index = int(data.get('player_index', 0))
    
    term = session.get('term')
    bara_index = session.get('bara_index')
    player_names = session.get('player_names', [])
    
    # Validate player_index
    if player_index < 0 or player_index >= len(player_names):
        return jsonify({
            'error': 'Invalid player index'
        }), 400
    
    if player_index == bara_index:
        word = None
        is_bara = True
    else:
        word = term
        is_bara = False
    
    return jsonify({
        'word': word,
        'is_bara': is_bara,
        'player_name': player_names[player_index]
    })

@app.route('/next_player', methods=['POST'])
def next_player():
    current = session.get('current_player', 0)
    num_players = session.get('num_players', 0)
    player_names = session.get('player_names', [])
    
    next_index = current + 1
    
    if next_index >= num_players:
        # Game round complete
        return jsonify({
            'complete': True,
            'message': 'All players have seen their words!'
        })
    
    session['current_player'] = next_index
    
    return jsonify({
        'complete': False,
        'current_player': next_index,
        'player_name': player_names[next_index]
    })

@app.route('/get_current_player', methods=['GET'])
def get_current_player():
    """Get current player info without exposing the word"""
    # Check if game session exists
    if 'player_names' not in session or not session.get('player_names'):
        return jsonify({
            'error': 'No game session found',
            'redirect': True
        }), 400
    
    current = session.get('current_player', 0)
    player_names = session.get('player_names', [])
    
    if current < len(player_names):
        return jsonify({
            'player_name': player_names[current],
            'player_index': current
        })
    else:
        return jsonify({
            'player_name': 'لاعب',
            'player_index': 0
        })

@app.route('/game')
def game():
    # Check if game session exists, redirect to home if not
    if 'player_names' not in session or not session.get('player_names'):
        return render_template('error.html', 
                             message='لم يتم إعداد اللعبة. الرجاء البدء من الصفحة الرئيسية.')
    return render_template('game.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
