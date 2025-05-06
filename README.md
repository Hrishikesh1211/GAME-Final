# The Mansion – Final Project Report

**Student:** Hrishikesh Rajaputra  
**Course:** Game AI  
**Date:** 5/6/2025

---

## 1. Base System Functionality (30 pts)

**Overview:**  
_The Mansion_ is a text-based, AI-inspired horror game where the player explores 10 haunted rooms, manages their sanity, avoids a cursed item, collects clues, and attempts to escape. The system tracks progress and decisions dynamically to support multiple endings.

### Scenarios Handled:
- Dynamic room generation and environmental descriptions
- Dice-based skill resolution (e.g., open door, regain sanity, escape danger)
- Sanity tracking and depletion with consequences
- Clue collection and cursed item logic
- Conditional branching for various endings
- Replay loop with full game summary
- Visual progress and sanity/clue bars in the terminal
- Optional immersive audio system

---

## 2. Prompt Engineering & Model Parameter Choice (10 pts)

While no real-time language model is used during gameplay, prompt engineering principles were applied in designing narrative templates and response logic.

### Design Considerations:
- Room descriptions were structured using reusable horror-themed templates
- Prompts modeled to keep tone consistent and concise
- Inspired by LLM temperature control principles to ensure variety while avoiding incoherence
- Player instructions and help prompts were carefully worded to guide user actions and improve immersion

---

## 3. Tools Usage (15 pts)

The game integrates multiple tools and Python libraries:

- `pygame` – audio playback for ambient sounds and effects
- `colorama` – dynamic terminal color coding (e.g., sanity bar)
- `random` – handles all game chance logic (dice, events, clue discovery)
- `os` – for environmental control and suppressing sound module prompts

The `sounds/` folder is excluded from GitHub via `.gitignore` and made available separately via GitHub Releases for clean distribution.

---

## 4. Planning & Reasoning (15 pts)

Multi-step reasoning is at the core of this game's logic:

- Exploration triggers a sequence of decisions: update state → check progress → check for clues → generate event
- Endings are decided by multiple conditions: room count, sanity level, clues found, cursed item status
- Sound effects are tied to event types and emotional thresholds (e.g., mind snap when sanity drops)

Replay logic resets the game and encourages alternate paths and endings based on new decisions.

---

## 5. Retrieval-Augmented Generation (10 pts)

Clue tracking, cursed item status, and danger states simulate memory and context-based behavior across rooms.

### In-Game Retrieval System:
- Clues are stored and not repeated
- Sanity loss is cumulative and persistent
- Room events are generated based on evolving game state
- Endings reflect multiple past conditions, similar to RAG-based summarization

---

## 6. Additional Tools / Innovation (10 pts)

### Features Added:
- **Audio System**: Configurable ambient loop and situational effects (heartbeat, door creak, thunder)
- **Visual Meters**:
  - Sanity bar with color-coded thresholds
  - Room progress bar showing total rooms explored
  - Clue bar with live tracking
- **In-Game Help System**: Real-time toggling of sound settings
- **Narrative-Driven Endings**: Each tied to cumulative gameplay variables
- **Multiple replay paths** with randomly distributed clue locations and cursed item events

---

## 7. Code Quality & Modular Design (10 pts)

### Structure:
- `main.py` – gameplay loop and I/O
- `game_state.py` – tracks player state and handles updates
- `scenes.py` – handles room description generation and clue distribution
- `dice.py` – encapsulates all roll logic
- `sounds/` – holds audio assets (external via release)
- `.gitignore` – excludes audio from version control

The system is cleanly modular, well-commented, and structured for maintainability. GitHub repo uses semantic commits and organized asset distribution.

---

## Repository

Code and game logic:  
[https://github.com/Hrishikesh1211/GAME-Final](https://github.com/Hrishikesh1211/GAME-Final)

Download full game with sound:  
[https://github.com/Hrishikesh1211/GAME-Final/releases](https://github.com/Hrishikesh1211/GAME-Final/releases)

---

## Conclusion

_The Mansion_ applies core AI game development techniques — procedural generation, player state management, conditional logic, and sound-driven immersion — in a coherent and replayable horror experience. It meets the rubric's goals across all learning outcomes while remaining user-friendly and fun to play.

