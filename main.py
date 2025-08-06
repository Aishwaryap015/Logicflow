import time

# File to save scores
SCORE_FILE = "scores.txt"

# Logic puzzles by level
LEVELS = [
    {
        "question": "Level 1: What is the output of 1 AND 0?",
        "answer": "0"
    },
    {
        "question": "Level 2: What is the output of 1 OR 0?",
        "answer": "1"
    },
    {
        "question": "Level 3: What is the output of NOT 1?",
        "answer": "0"
    },
    {
        "question": "Level 4: What is the output of (1 XOR 1)?",
        "answer": "0"
    },
    {
        "question": "Level 5: What is the output of (1 AND (NOT 0))?",
        "answer": "1"
    }
]

def save_score(name, score, total_time):
    with open(SCORE_FILE, "a") as f:
        f.write(f"{name}: {score} points in {total_time:.2f} seconds\n")

def view_scores():
    try:
        with open(SCORE_FILE, "r") as f:
            print("\n📜 Score History:")
            print(f.read())
    except FileNotFoundError:
        print("\nNo scores recorded yet.")

def play_game():
    name = input("Enter your name: ")
    print(f"\n🎮 Welcome, {name}! Let's start the logic circuit puzzle game.\n")

    score = 0
    start_time = time.time()

    for level in LEVELS:
        print(level["question"])
        answer = input("Your answer: ").strip()
        if answer == level["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer was {level['answer']}\n")

    end_time = time.time()
    total_time = end_time - start_time

    print(f"🏁 Game Over! You scored {score}/{len(LEVELS)} in {total_time:.2f} seconds.")
    save_score(name, score, total_time)

def main():
    while True:
        print("\n🧩 Logicflow: Logic Circuit Puzzle Game Simulator")
        print("1. Play Game")
        print("2. View Score History")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            play_game()
        elif choice == "2":
            view_scores()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

