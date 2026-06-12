# Higher-Lower Game 🎮

A fun, text-based Python game inspired by the popular web game "The Higher Lower Game". Challenge yourself to guess who has more Instagram followers between two public figures or brands!

## 📋 Table of Contents
- [Features](#features)
- [Rules of the Game](#rules-of-the-game)
- [Prerequisites](#prerequisites)
- [How to Run](#how-to-run)
- [File Structure](#file-structure)

---

## ✨ Features
- **Dynamic Matchups:** Shuffles and selects data entries at random to ensure every game feels fresh.
- **Continuous Streak:** If you guess correctly, the current opponent moves to the hot seat, and a brand new contender appears.
- **Score Tracking:** Keeps track of your current win streak in real-time.
- **Clean Console UI:** Automatically clears the terminal screen after each turn to keep the interface tidy.

---

## 🕹️ Rules of the Game
1. You will be presented with two choices: **Option A** and **Option B**.
2. Compare the two options and guess who has a higher follower count on Instagram.
3. Type **'A'** or **'B'** to lock in your guess.
4. **Scoring:**
   - If your guess is **correct**, you gain `1 point`. **Option B** becomes your new **Option A**, a new challenger is picked for **Option B**, and the game continues!
   - If your guess is **incorrect**, the game ends immediately and displays your final score.

---

## 🛠️ Prerequisites
To run this game, make sure you have **Python 3.x** installed on your machine. No extra third-party libraries are required, as it runs entirely using Python's built-in modules.

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Neha-reddy-c/Higher-Lower.git](https://github.com/Neha-reddy-c/Higher-Lower.git)

2. **Navigate to the project directory:**
   ```bash
   cd Higher-Lower
   
3. **Run the game:**
   ```bash
   python main.py
