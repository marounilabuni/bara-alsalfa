from flask import Flask, render_template, request, jsonify
import random
import os
from gpt_word_generator import get_gpt_word

app = Flask(__name__)

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/api/generate_word', methods=['POST'])
def generate_word():
    """Generate a word using GPT"""
    data = request.json
    topic = data.get('topic', None)
    
    try:
        word = get_gpt_word(topic)
        return jsonify({
            'success': True,
            'word': word
        })
    except Exception as e:
        error_msg = str(e)
        print(f"Error generating word with GPT: {error_msg}")
        return jsonify({
            'success': False,
            'error': 'فشل توليد الكلمة باستخدام GPT. الرجاء المحاولة مرة أخرى أو إلغاء تفعيل GPT.',
            'error_details': error_msg
        }), 500

@app.route('/api/get_random_word', methods=['GET'])
def get_random_word():
    """Get a random word from predefined list"""
    word = random.choice(TERMS)
    return jsonify({
        'success': True,
        'word': word
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
