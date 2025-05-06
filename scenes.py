import random
from prompts import room_prompt
from ai_engine import generate_ai_response
from dice import roll_dice

def generate_room(state):
    prompt = room_prompt(state)
    description = generate_ai_response(prompt)

    # Sanity-related hallucinations
    if state.sanity < 70:  # trigger earlier:
        print("You feel reality slipping...")
        result = roll_dice()
        if result < 10:
            print("The walls bleed. You scream, but no one hears.")
            state.sanity = max(0, state.sanity - 5)
        else:
            print("You shake off the vision. Just barely.")

    # Random sanity decrease
    if random.random() < 0.8:  # more frequent sanity loss
        loss = random.randint(10, 25)  # higher loss range
        state.sanity = max(0, state.sanity - loss)
        description += f"\n(Your sanity slips by {loss} points...)"

    # Chance to discover a hidden feature
    hidden_roll = random.randint(1, 20)
    if hidden_roll == 20:
        description += "\nYou notice a glint behind the fireplace... is that a hidden compartment?"
    
    # Random chance to encounter a locked door
    if random.random() < 0.4:  # 40% of rooms have a locked door
        description += "\nThere’s a locked door here. Maybe you can force it open?"
        state.locked_door_found = True
    else:
        state.locked_door_found = False

    # Chance to find a clue
    if random.random() < 0.3:
        description += "\nYou notice something scratched into the wall... a clue."
        state.found_clues += 1
        description += f"\n(Clue found. Total clues: {state.found_clues})"

# Rare chance to find cursed item
    if not state.cursed_item and random.random() < 0.1:
        description += "\nYou pick up a small doll. It’s cold, and your hands tremble as you hold it."
        state.cursed_item = True

# 30% chance of an encounter after exploring
    if random.random() < 0.3:
        description += "\nSomething stirs in the shadows... You sense immediate danger!"
        state.in_danger = True
    else:
        state.in_danger = False


    return description
