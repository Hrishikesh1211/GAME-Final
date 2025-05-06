import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
from game_state import GameState
from scenes import generate_room
from dice import roll_dice
from colorama import init, Fore, Style

init(autoreset=True)

# Initialize sound system
pygame.mixer.init()

sound_effects_enabled = True
ambient_enabled = False

def play_sound(filename):
    if sound_effects_enabled:
        try:
            pygame.mixer.Sound(f"sounds/{filename}").play()
        except Exception as e:
            print(f"[Sound error] {e}")

def start_ambient_loop():
    try:
        pygame.mixer.music.load("sounds/ambient_loop.mp3")
        pygame.mixer.music.play(-1)
    except Exception as e:
        print(f"[Ambient loop error] {e}")

def stop_ambient_loop():
    pygame.mixer.music.stop()

def lose_sanity(state, amount):
    state.sanity = max(0, state.sanity - amount)

def show_help_menu():
    global ambient_enabled, sound_effects_enabled
    print("\n--- Audio Settings ---")
    print(f"1. Ambient Sound: {'ON' if ambient_enabled else 'OFF'}")
    print(f"2. Sound Effects: {'ON' if sound_effects_enabled else 'OFF'}")
    print("Type '1' to toggle ambient sound.")
    print("Type '2' to toggle sound effects.")
    print("Type 'back' to return to the game.")

    while True:
        choice = input("Option > ").strip().lower()
        if choice == "1":
            if ambient_enabled:
                stop_ambient_loop()
                ambient_enabled = False
                print("Ambient sound disabled.")
            else:
                start_ambient_loop()
                ambient_enabled = True
                print("Ambient sound enabled.")
        elif choice == "2":
            sound_effects_enabled = not sound_effects_enabled
            print(f"Sound effects {'enabled' if sound_effects_enabled else 'disabled'}.")
        elif choice == "back":
            break
        else:
            print("Invalid option. Type 1, 2, or back.")

def show_progress(state):
    explored = "🟥" * state.room_count
    remaining = "⬜" * (10 - state.room_count)
    print(f"{'Progress:':<10} {explored}{remaining} ({state.room_count}/10)")

def show_sanity_bar(state):
    blocks = state.sanity // 10
    bar = ""
    for i in range(10):
        if i < blocks:
            if state.sanity > 70:
                bar += "🟩"
            elif state.sanity > 40:
                bar += "🟨"
            else:
                bar += "🟥"
        else:
            bar += "⬛"
    print(f"{'Sanity:':<10} {bar} ({state.sanity}/100)")

    if state.sanity <= 20:
        print(Fore.RED + "!!! WARNING: Your sanity is low !!!" + Style.RESET_ALL)

def show_clue_bar(state):
    found = min(state.found_clues, 5)
    clues = "🧩" * found
    remaining = "⬜" * (5 - found)
    print(f"{'Clues:':<10} {clues}{remaining} ({state.found_clues}/5)")

def play_game():
    global sound_effects_enabled, ambient_enabled

    state = GameState()

    ambient_input = input("Enable ambient background sound? (yes/no): ").strip().lower()
    if ambient_input == "yes":
        ambient_enabled = True
        start_ambient_loop()

    effects_input = input("Enable sound effects? (yes/no): ").strip().lower()
    if effects_input == "no":
        sound_effects_enabled = False

    play_sound("thunder.wav")
    print("================================================\n")
    print("Welcome to The Mansion...\n")
    print("Thunder cracks. You awaken on a cold stone floor. The air is damp. A door creaks open in the dark...\n")

    while not state.game_over:
        show_sanity_bar(state)
        show_progress(state)
        show_clue_bar(state)
        print("What would you like to do? (explore / roll / help / quit)")
        user_input = input("> ").strip().lower()

        if not user_input:
            print("Please type a command.")
            continue

        if "explore" in user_input:
            room_description = generate_room(state)
            print(room_description)

            if state.room_count >= 10 and state.sanity > 0:
                if state.cursed_item:
                    print("\nYou find the exit... but the cursed object pulses in your hand.")
                    print("Your body escapes, but your soul is bound to the house forever.")
                    state.ending = "Possession"
                elif state.found_clues >= 5 and state.sanity > 30:
                    print("\nYou piece together the story of the house as you flee.")
                    print("You understand what happened here. You solved the mystery.")
                    state.ending = "Solved Escape"
                elif state.sanity > 30:
                    print("\nYou find a hidden exit and flee into the night.")
                    print("You survived the house. You win.")
                    state.ending = "Escape"
                else:
                    print("\nYou stumble out of the house, barely conscious. You don’t know what was real.")
                    state.ending = "Unsolved Escape"
                state.game_over = True

        elif "roll" in user_input:
            action = input("What are you rolling for? (e.g., escape, sanity, open door) > ").strip().lower()
            result = roll_dice()
            print(f"You rolled a {result} for {action}.")

            if action == "escape":
                if not state.in_danger:
                    print("There's nothing to escape from.")
                elif result >= 10:
                    print("You successfully escape the unseen danger.")
                    state.in_danger = False
                else:
                    play_sound("heartbeat.wav")
                    print("You stumble in fear… it's still coming.")
                    state.in_danger = False
                    lose_sanity(state, 10)
                    print("(You lose 10 sanity.)")

            elif action == "sanity":
                if result >= 12:
                    print("You regain your composure slightly. +5 sanity.")
                    state.sanity = min(100, state.sanity + 5)
                else:
                    print("Your mind reels in fear. You gain nothing.")

            elif action == "open door":
                if not state.locked_door_found:
                    print("There is no locked door to open.")
                elif result >= 10:
                    print("You force the heavy door open. A cold draft spills out from the darkness beyond.")
                    play_sound("door_creak.wav")
                    state.room_count += 1
                    state.locked_door_found = False
                    room_description = generate_room(state)
                    print(room_description)

                    if state.room_count >= 10 and state.sanity > 0:
                        if state.cursed_item:
                            print("\nYou find the exit... but the cursed object pulses in your hand.")
                            print("Your body escapes, but your soul is bound to the house forever.")
                            state.ending = "Possession"
                        elif state.found_clues >= 5 and state.sanity > 30:
                            print("\nYou piece together the story of the house as you flee.")
                            print("You understand what happened here. You solved the mystery.")
                            state.ending = "Solved Escape"
                        elif state.sanity > 30:
                            print("\nYou find a hidden exit and flee into the night.")
                            print("You survived the house. You win.")
                            state.ending = "Escape"
                        else:
                            print("\nYou stumble out of the house, barely conscious. You don’t know what was real.")
                            state.ending = "Unsolved Escape"
                        state.game_over = True
                else:
                    play_sound("heartbeat.wav")
                    print("The door won't budge. Something resists from the other side.")
                    lose_sanity(state, 5)
                    state.locked_door_found = False
                    print("(You lose 5 sanity.)")

            else:
                print("You feel the dice decide nothing this time...")

        elif "help" in user_input:
            show_help_menu()

        elif "quit" in user_input:
            print("You feel the cold darkness claim you...")
            state.ending = "Quit"
            state.game_over = True

        if state.sanity <= 0:
            play_sound("heartbeat.wav")
            print("\nYour mind fractures. You collapse into madness.")
            print("Game over.")
            state.ending = "Insanity"
            state.game_over = True

    if ambient_enabled:
        pygame.mixer.music.fadeout(2000)

    print("\n--- Game Summary ---")
    print(f"Ending: {state.ending}")
    print(f"Rooms Explored: {state.room_count}")
    print(f"Sanity Remaining: {state.sanity}")
    print(f"Clues Found: {state.found_clues}")
    if state.cursed_item:
        print("You carried a cursed item.")

    if state.ending == "Solved Escape":
        print("The nightmares fade. The truth of the house is yours alone now.")
    elif state.ending == "Escape":
        print("You vanish into the fog, heart racing. But you are free.")
    elif state.ending == "Unsolved Escape":
        print("You escaped, but the horror clings to your mind. What did you leave behind?")
    elif state.ending == "Possession":
        print("You got out... but part of you is still trapped in that house.")
    elif state.ending == "Insanity":
        print("They found your body days later. Your eyes... still wide open.")
    elif state.ending == "Quit":
        print("The house remains, and you’ll never know what you left unfinished.")

    print("\nThanks for playing!")

    replay = input("\nWould you like to play again? (yes/no): ").strip().lower()
    if replay == "yes":
        play_game()

if __name__ == "__main__":
    play_game()
