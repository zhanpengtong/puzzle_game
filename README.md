# 🧩 Puzzle Game  
An interactive image-based puzzle game built using Python and the Turtle graphics library. This project was developed as the final project for **CS5001: Intensive Foundations of Computer Science** at Northeastern University. It features an engaging sliding puzzle interface, real-time interactions, leaderboard functionality, and custom puzzle loading.  

## 🚀 Features  
- 🎮 **Sliding Puzzle Gameplay** – Play using your mouse by clicking on adjacent tiles to swap positions.  
- 🧑 **User Setup** – Enter your player name and choose your move limit before starting.  
- 🗂 **Puzzle Loader** – Load different `.puz` files dynamically to change puzzle layout and images.  
- 🧠 **Win/Lose Detection** – Game automatically recognizes correct tile arrangement.  
- 🏆 **Leaderboard** – Stores top scores in a persistent `leader.txt` file based on moves and win conditions.  
- 🔄 **Buttons** – In-game controls for reset, quit, and loading new puzzles.  
- 🎨 **Turtle Graphics UI** – Cleanly rendered interface with graphical button states and overlays.  
- 📂 **File-based Save/Load** – Modular handling of puzzles and scores using plain text files.  

## 📂 File Structure  
puzzle_game/
├── puzzle_game.py # Main script to launch the game
├── leader.txt # Persistent leaderboard storage
├── Resources/
│ ├── *.gif # Puzzle images, game UI assets (splash, win, lose screens)
│ ├── *.puz # Custom puzzle configuration files (tile layout metadata)
├── README.md # You're reading it!


## ⚙️ How to Run  
### 🐍 Requirements  
- Python 3.x  
- No external dependencies required (uses built-in `turtle`, `os`, `time`)  

### 🧪 Quick Start  
```bash  
git clone https://github.com/zhanpengtong/puzzle_game  
cd puzzle_game  
python puzzle_game.py  
