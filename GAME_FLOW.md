# Game Flow Documentation

## Overview
This document explains how the "برا السالفة" game flow works and ensures that `get_player_word` is only called after player names are selected.

## Game Flow

### 1. Setup Phase (index.html)
```
User enters:
  ├─ Number of players
  ├─ (Optional) Enable GPT word generation
  ├─ (Optional) Topic for word
  └─ Player names for each player

↓ Click "ابدأ اللعبة"

POST to /start_game with:
  ├─ num_players
  ├─ player_names (array)
  ├─ use_gpt (boolean)
  └─ topic (string or null)
```

### 2. Game Initialization (/start_game endpoint)
```
Backend processes:
  ├─ Generates word using get_term(topic, use_gpt)
  ├─ Randomly selects "bara_index" (who is برا السالفة)
  ├─ Stores in session:
  │    ├─ term (the secret word)
  │    ├─ bara_index (index of player who is برا السالفة)
  │    ├─ player_names (list of all names)
  │    ├─ num_players (total count)
  │    └─ current_player (starts at 0)
  └─ Returns success response

↓ Redirect to /game
```

### 3. Game Page Load (game.html)
```
Page loads:
  ├─ Does NOT call get_player_word yet
  ├─ Calls GET /get_current_player
  └─ Displays first player's name only

User sees:
  ├─ Player name: "لاعب 1" (or their actual name)
  └─ Button: "عرض الكلمة"
```

### 4. Word Reveal (First time get_player_word is called)
```
User clicks "عرض الكلمة":
  ↓
  POST to /get_player_word with player_index
  ↓
Backend checks:
  ├─ Is player_index == bara_index?
  │    ├─ YES: Return { word: null, is_bara: true }
  │    └─ NO: Return { word: term, is_bara: false }
  └─ Include player_name in response

Frontend displays:
  ├─ If is_bara: "🎭 أنت برا السالفة!"
  ├─ Else: Shows the actual word
  └─ Shows "اللاعب التالي" button
```

### 5. Next Player
```
User clicks "اللاعب التالي":
  ↓
  POST to /next_player
  ↓
Backend:
  ├─ Increments current_player
  ├─ Checks if all players done
  │    ├─ YES: Return { complete: true }
  │    └─ NO: Return { complete: false, current_player: X, player_name: "..." }

Frontend:
  ├─ If complete: Show "Game Complete" screen
  └─ Else: Reset to step 4 for next player
```

## Security & Privacy

### ✅ What's Protected
- `get_player_word` is ONLY called when user clicks "عرض الكلمة"
- Word/term is never exposed until player explicitly views it
- Each player only sees their own word when they click the button

### ✅ Endpoints
1. **GET /get_current_player** - Returns ONLY player name and index (no word)
2. **POST /get_player_word** - Returns word/bara status (only when explicitly requested)
3. **POST /next_player** - Advances to next player (no word exposed)

## Key Improvements

### Before
❌ `window.onload` called `get_player_word` immediately
❌ First player's word could be exposed in network logs
❌ API called before user was ready

### After
✅ `window.onload` only calls `get_current_player` (no word)
✅ `get_player_word` only called when user clicks "عرض الكلمة"
✅ Complete control over when word is revealed
✅ Better privacy and game flow

## Testing Checklist

- [ ] Enter player names on setup page
- [ ] Click "ابدأ اللعبة"
- [ ] Game page loads showing first player's name
- [ ] Network tab shows NO call to `get_player_word` on page load
- [ ] Click "عرض الكلمة" - NOW `get_player_word` is called
- [ ] Word/bara status is displayed correctly
- [ ] Click "اللاعب التالي" - advances to next player
- [ ] Repeat until all players have seen their words
- [ ] Game completion screen appears
