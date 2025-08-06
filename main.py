import time
import random

# Define logic gate functions
def AND(a, b): return a & b
def OR(a, b): return a | b
def XOR(a, b): return a ^ b
def NAND(a, b): return int(not (a & b))
def NOR(a, b): return int(not (a | b))
def XNOR(a, b): return int(not (a ^ b))

# Define levels
levels = [
    {"gate": "AND", "inputs": (1, 1), "expected": 1},
    {"gate": "OR", "inputs": (0, 0), "expected": 0},
    {"gate": "XOR", "inputs": (1, 0), "expected": 1},
    {"gate": "NAND", "inputs": (1, 1), "expected": 0},
    {"gate": "NOR", "inputs": (0, 0), "expected": 1},
    {"gate": "XNOR", "inputs": (1, 1), "expected": 1},
]
score = 0
history = []

print("🧩 Welcome to Logic Circuit Puzzle Game Simulator!")
print("📜 Previous Score History:")
try:
    with open("score_history.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("No previous history found.\n")

print("Answer the output of the logic gate given the inputs.\n")

for level_num, level in enumerate(levels, start=1):
    gate = level['gate']
    a, b = level['inputs']
    expected = level['expected']
    print(f"\nLevel {level_num}: {gate} Gate - Inputs: {a}, {b}")
    
    start_time = time.time()
    user_input = input("Your Answer (0 or 1): ")
    end_time = time.time()
    
    try:
        user_answer = int(user_input)
    except ValueError:
        print("❌ Invalid input. Skipping level.")
        continue

    correct = user_answer == expected
    time_taken = round(end_time - start_time, 2)

    if correct:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct Answer was {expected}")

    # Save history
    history.append({
        "level": level_num,
        "gate": gate,
        "inputs": (a, b),
        "your_answer": user_answer,
        "correct": correct,
        "time": time_taken
    })

print("\n🎉 Game Over!")
print(f"Your Score: {score} / {len(levels)}")

# Save to score file
with open("score_history.txt", "a") as f:
    f.write(f"\nSession Score: {score} / {len(levels)}\n")
    for h in history:
        f.write(f"Level {h['level']} | Gate: {h['gate']} | Inputs: {h['inputs']} | "
                f"Answer: {h['your_answer']} | Correct: {h['correct']} | Time: {h['time']}s\n")

