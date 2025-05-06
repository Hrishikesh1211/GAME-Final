Project Report – The Mansion
Student Name: Hrishikesh Rajaputra
 Course: Game 441
 Date: 5/6/2025

1. Base System Functionality (30 pts)
Overview:
 The Mansion is a single-player, AI-driven text-based horror game set in a haunted house. The player navigates through eerie rooms, manages their sanity, avoids possession, and collects clues to solve the mystery and escape.
Handled Scenarios:
Room exploration and descriptions


Dice-based action resolution


Sanity management system


Random events and environmental reactions


Locked door progression with roll-based access


Clue discovery


Encountering cursed items


Audio-driven immersion


Replay option with summary


Core Features Implemented:
explore command to enter rooms


roll for actions (e.g., open door, escape, sanity)


Sanity loss and recovery mechanics


Inventory system with cursed items and clues


Win and loss conditions with multiple endings


Visual HUD (sanity bar, progress bar, clues bar)



2. Prompt Engineering & Model Parameter Choice (10 pts)
While the system does not use a live LLM in real-time gameplay, prompts and structured narrative templates were used during development to generate:
Dynamic room descriptions


In-game events


Clue hints and object details


Model Design Influences:
Controlled generation style to keep horror tone


Balanced output length to avoid delays


Prompts written with context awareness, e.g., "You enter a dim hallway. A mirror seems to breathe."


Parameters like temperature (0.7–0.9) were used during design testing to ensure unpredictability while keeping coherence.

3. Tools Usage (15 pts)
Integrated Tools:
pygame – for sound effect playback and ambient looping


colorama – for dynamic terminal coloring (sanity warnings)


random – for simulating dice rolls and room events


os – to manage prompt suppression and directory settings


All tools are part of the Python ecosystem and demonstrate AI-adjacent utilities, especially around player feedback and immersion.

4. Planning & Reasoning (15 pts)
Multi-Step Planning Examples:
Room generation calls internally update game state


Roll outcomes trigger conditional branches (e.g., roll result, cursed status, sanity threshold)


Clues and cursed item logic affect endgame reasoning


Chain-of-thought logic is embedded in:
Endings, which evaluate multiple conditions


Replay loop, allowing players to start over with a fresh state


Sound triggers tied to specific emotional or gameplay thresholds (e.g., sanity loss)



5. Retrieval-Augmented Generation (10 pts)
While no database or external vector search was used, a lightweight form of in-memory context tracking functions as RAG:
Clues are stored per room and never repeated


Found clues affect final narrative and outcome


Previously triggered states (e.g., danger, curse, door status) influence future decisions


This simulates memory retrieval and response adaptation across playthroughs.

6. Additional Tools / Innovation (10 pts)
Innovations Added:
Audio system (optional toggle):


Thunder intro


Door creaks


Heartbeat when sanity is at risk


Mind snap on sanity loss


Ambient loop option


Visual HUD:


Sanity bar with color tiers


Room progress tracker


Clue tracker


Game summary at the end with dynamic flavor text


Multiple endings based on clue count, sanity level, and cursed item status


Help menu to toggle audio in real-time



7. Code Quality & Modular Design (10 pts)
Structure:
main.py handles gameplay loop and user interaction


game_state.py manages the player's state (sanity, clues, progress)


scenes.py generates new room descriptions


dice.py encapsulates roll logic


sounds/ is ignored in Git but included in release ZIP


Modular imports, clean functions, and inline documentation included


Version control was maintained through GitHub:
Repository: https://github.com/Hrishikesh1211/GAME-Final 
Sound files provided through GitHub Releases 

Conclusion
The Mansion demonstrates a robust use of fundamental AI principles in a game system. It blends modular logic, narrative-driven decision trees, and player state tracking to deliver a cohesive and immersive horror experience. With layered endings, user-configurable audio, and progressive mechanics.

