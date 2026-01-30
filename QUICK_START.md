# Quick Start Guide - برا السالفة 🎮

## 🚀 Run the App Locally

```bash
# Navigate to project directory
cd "/Users/maroun/my local files/games/bara"

# Install dependencies (first time only)
pip install -r requirements.txt

# Run the app
python app.py
```

Open your browser to: **http://localhost:5001**

---

## 🎮 How to Play

### 1. Setup Phase
1. Enter **number of players** (minimum 3)
2. **GPT is enabled by default** ✅ (generates unique words)
3. (Optional) Enter a **topic** (e.g., طعام، رياضة، حيوانات)
4. Click **"إنشاء حقول الأسماء"**
5. Enter each player's **name**
6. Click **"ابدأ اللعبة"**

### 2. Word Distribution
1. Each player takes a turn
2. Current player clicks **"عرض الكلمة"**
3. Player sees either:
   - The secret word, OR
   - "🎭 أنت برا السالفة!"
4. Click **"اللاعب التالي"** to pass device
5. Repeat until all players have seen their words

### 3. Game Phase
- Players ask each other questions about the word
- Try to identify who is "برا السالفة"
- "برا السالفة" tries to blend in and guess the word

---

## ⚙️ Settings

### GPT Word Generation (Default: ON)
- ✅ **Enabled**: Generates fresh, unique words using AI
- ❌ **Disabled**: Uses predefined Arabic word list

### Topic (Optional)
- Guide word generation to specific category
- Examples: طعام، رياضة، حيوانات، أماكن، مهن

---

## 🐛 Troubleshooting

### GPT Not Working?
**Error Modal Appears:**
- Click **"استخدام كلمة محفوظة"** to auto-switch to predefined words
- OR uncheck GPT manually and retry

**Common Causes:**
- Missing/invalid OPENAI_API_KEY in `.env`
- No internet connection
- API rate limit reached

**Quick Fix:**
```bash
# Check .env file has your API key
cat .env | grep OPENAI_API_KEY
```

### Port Already in Use?
```bash
# Change port in app.py (line 205)
app.run(debug=True, host='0.0.0.0', port=5002)  # Use different port
```

### Game State Lost?
```bash
# Clear localStorage in browser console
localStorage.removeItem('baraGameState');
# Then start a new game
```

---

## 🌐 Deploy Online

### Option 1: Vercel (Recommended)
```bash
# Install Vercel CLI
npm install -g vercel

# Login
vercel login

# Deploy
vercel

# Add OPENAI_API_KEY in Vercel dashboard
```

### Option 2: Render
1. Push code to GitHub
2. Go to https://render.com
3. Create new "Web Service"
4. Connect your repo
5. Add environment variable: `OPENAI_API_KEY`
6. Deploy!

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

---

## 📁 Project Structure

```
bara/
├── app.py                 # Flask backend (no sessions!)
├── gpt_word_generator.py  # GPT integration
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (local)
├── vercel.json           # Vercel config
├── templates/
│   ├── index.html        # Setup page
│   └── game.html         # Game page
└── docs/
    ├── DEPLOYMENT.md     # Deployment guide
    ├── ERROR_HANDLING.md # Error handling docs
    └── QUICK_START.md    # This file
```

---

## 🎨 Features

✅ **AI-Powered** - GPT generates unique words  
✅ **Topic-Based** - Choose word categories  
✅ **Beautiful UI** - Modern gradient design  
✅ **Error Handling** - Professional modals with auto-recovery  
✅ **Mobile Ready** - Responsive design  
✅ **Arabic RTL** - Proper right-to-left support  
✅ **No Sessions** - Works on serverless platforms  
✅ **Fast** - Frontend state management  

---

## 🔑 Environment Variables

### Local Development (.env)
```bash
OPENAI_API_KEY=sk-proj-...your-key-here...
```

### Production (Vercel/Render)
Add in platform dashboard:
- Key: `OPENAI_API_KEY`
- Value: Your OpenAI API key

---

## 📝 Notes

- **Game state** stored in browser localStorage
- **No database** needed - fully stateless
- **GPT calls** only happen once per game (at setup)
- **All navigation** happens client-side after setup
- **Works offline** after word is generated

---

## 🎯 Tips

1. **Larger Groups**: More fun with 5-8 players
2. **Custom Topics**: Try specific topics for themed games
3. **Mobile Friendly**: Pass one phone around
4. **No Peeking**: Players should close eyes when passing device
5. **Time Limit**: Add your own timer for more challenge

---

## 🆘 Get Help

### Check Logs
```bash
# Terminal shows all requests and errors
# Look for error messages in console
```

### Test GPT
```bash
python test_gpt_word.py
```

### Test Error Handling
```bash
python test_gpt_error_handling.py
```

---

## 🎉 You're Ready!

Everything is set up and working. Just run:

```bash
python app.py
```

And visit: **http://localhost:5001**

Have fun playing برا السالفة! 🎮✨
