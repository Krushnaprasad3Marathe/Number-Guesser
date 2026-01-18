# 🎯 Number Guessing Game (Python)

This is a simple **Number Guessing Game** written in **Python**.  
The player has to guess a randomly generated number within limited lives.

---

## 🚀 Features

- Two difficulty levels:
  - **EASY** → 5 lives → number between **1 to 9**
  - **HARD** → 3 lives → number between **10 to 19**
- Random number generation using `random` module
- Loop-based guessing system
- Simple and beginner-friendly logic

---

## 🧠 How the Game Works

1. Program asks the user to select difficulty: **EASY** or **HARD**
2. A random number is generated based on difficulty
3. User enters a guess
4. If the guess is:
   - ✅ Correct → Game ends
   - ❌ Wrong → Life decreases and user tries again
5. Game continues until:
   - Correct guess OR
   - All lives are finished

---

## 🧾 Rules

| Difficulty | Number Range | Lives |
|-----------|--------------|-------|
| EASY      | 1 – 9        | 5     |
| HARD      | 10 – 19      | 3     |

---

## 🛠️ Technologies Used

- Python 3
- `random` module

---

## ▶️ How to Run the Program

1. Make sure Python is installed
2. Clone the repository:
   ```bash
   git clone https://github.com/Krushnaprasad3Marathe/Number-Guesser.git
