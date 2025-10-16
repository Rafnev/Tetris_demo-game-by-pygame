# Tetris_demo-game-by-pyga

A classic Tetris game implementation built with Python and Pygame. Features smooth gameplay, scoring system, level progression, and all the standard Tetris mechanics you know and love!

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎯 Features

- **Classic Tetris Gameplay**: All 7 standard tetromino pieces (I, J, L, O, S, T, Z)
- **Smooth Controls**: Responsive keyboard controls for movement and rotation
- **Scoring System**: Official Tetris scoring with combo bonuses
- **Level Progression**: Game speed increases as you clear more lines
- **Next Piece Preview**: See what's coming next to plan your strategy
- **Line Clearing**: Complete rows disappear and award points
- **Game Over Detection**: Game ends when blocks reach the top
- **Visual UI**: Clean interface with score, level, and lines display

## 🎮 How to Play

### Controls

| Key | Action |
|-----|--------|
| ⬅️ **Left Arrow** | Move piece left |
| ➡️ **Right Arrow** | Move piece right |
| ⬇️ **Down Arrow** | Move piece down faster |
| ⬆️ **Up Arrow** | Rotate piece clockwise |

### Objective

- Arrange falling tetromino pieces to create complete horizontal lines
- Completed lines disappear and award points
- Game speeds up as you progress through levels
- Survive as long as possible and achieve the highest score!

## 🚀 Installation
no need
### Prerequisites

- Python 3.7 or higher
- Pygame library

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/tetris-game.git
   cd tetris-game
   ```

2. **Install dependencies**
   ```bash
   pip install pygame
   ```

3. **Run the game**
   ```bash
   python Tetris_remix.py
   ```

## 📊 Scoring System

The game uses the official Tetris scoring system:

| Lines Cleared | Points | Multiplier |
|--------------|--------|------------|
| 1 line | 100 × level | Single |
| 2 lines | 300 × level | Double |
| 3 lines | 500 × level | Triple |
| 4 lines | 800 × level | **Tetris!** |

### Level Progression

- Every **10 lines** cleared increases the level by 1
- Fall speed increases with each level
- Higher levels = more points per line cleared

## 🎨 Game Elements

### Tetromino Pieces

| Piece | Color | Shape |
|-------|-------|-------|
| I | Cyan | ████ |
| J | Blue | ▐██ |
| L | Orange | ██▌ |
| O | Yellow | ██<br>██ |
| S | Green | ▐██<br>██▌ |
| T | Purple | ███<br>▐█▌ |
| Z | Red | ██▌<br>▐██ |

## 🛠️ Technical Details

### Game Configuration

```python
BLOCK_SIZE = 30        # Size of each block in pixels
GRID_WIDTH = 10        # Game grid width (10 blocks)
GRID_HEIGHT = 20       # Game grid height (20 blocks)
SCREEN_WIDTH = 500     # Total window width
SCREEN_HEIGHT = 600    # Total window height
FPS = 60              # Frame rate
```

### Project Structure

```
tetris-game/
├── Tetris_remix.py          # Main game file
├── test1.py                 # Original development file
├── README.md                # This file
└── .github/
    └── copilot-instructions.md  # Development guidelines
```

## 🎯 Game Mechanics

### Piece Movement
- Pieces fall automatically based on the current level speed
- Manual controls allow horizontal movement and rotation
- Collision detection prevents invalid moves

### Line Clearing
- When a horizontal row is completely filled, it's cleared
- All blocks above the cleared line(s) fall down
- Multiple lines can be cleared simultaneously for bonus points

### Game Over
- Game ends when newly spawned pieces overlap with existing blocks
- Final score, level, and lines cleared are displayed

## 🔧 Customization

Want to modify the game? Here are some easy tweaks:

### Change Colors
Edit the `COLORS` list in the code:
```python
COLORS = [
    (0, 255, 255),    # I - Cyan
    (0, 0, 255),      # J - Blue
    # ... modify as desired
]
```

### Adjust Difficulty
Modify the fall speed calculation:
```python
fall_speed = 0.5 - (level - 1) * 0.05  # Adjust multiplier for different difficulty
```

### Change Grid Size
Update the grid dimensions:
```python
GRID_WIDTH = 12   # Wider grid
GRID_HEIGHT = 22  # Taller grid
```

## 🐛 Known Issues

- None currently! If you find any bugs, please open an issue.

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contributions

- Add sound effects and background music
- Implement "hold piece" functionality
- Add ghost piece (shadow showing where piece will land)
- Create a main menu and pause functionality
- Add high score tracking with persistent storage
- Implement wall kicks for better rotation
- Add particle effects for line clears

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Inspired by the classic Tetris game created by Alexey Pajitnov
- Built with [Pygame](https://www.pygame.org/)
- Thanks to the Python and Pygame communities

## 📧 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/tetris-game](https://github.com/yourusername/tetris-game)

---

**Enjoy the game! 🎮 Try to beat your high score!**
