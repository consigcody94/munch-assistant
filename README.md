# 🎤 Munch Assistant

**Terminal-based animated ASCII art featuring Ice Spice with rotating verified quotes!**

![Terminal Animation](https://img.shields.io/badge/Terminal-Animation-yellow?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.6+-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Unix%20%7C%20Linux%20%7C%20Mac%20%7C%20Windows-green?style=for-the-badge)

## ✨ Features

- **🎨 Animated ASCII Art** - Beautiful terminal-based artwork with glow effects
- **💬 Verified Quotes** - Real Ice Spice quotes from 2024 interviews (Rolling Stone, Complex, Billboard)
- **⚡ Auto-Rotation** - Quotes change automatically every 5 seconds
- **🎯 Centered Display** - Always perfectly centered, no scrolling
- **🌈 Colorful** - Vibrant terminal colors with bold styling
- **⌨️ Interactive** - Press 'n' for next quote, 'q' to quit

## 🚀 Quick Start

### One-Line Run

```bash
./run.sh
```

Or directly with Python:

```bash
python3 munch.py
```

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/consigcody94/munch-assistant.git
cd munch-assistant
```

### 2. Run the Application

```bash
chmod +x run.sh
./run.sh
```

That's it! No dependencies to install on Unix/Linux/Mac.

### Windows Users

If you're on Windows, install the curses library:

```bash
pip install windows-curses
python munch.py
```

## 🎮 Controls

| Key | Action |
|-----|--------|
| `q` or `Q` | Quit the application |
| `n` or `N` or `Space` | Next quote |
| `ESC` | Exit |

## 📐 Terminal Requirements

- **Minimum Size**: 50 columns × 25 rows
- **Recommended**: 80 columns × 30+ rows for best experience
- **Color Support**: Terminal with color support recommended

## 🎨 Screenshots

The app displays:
1. **Header**: "✦ MUNCH ASSISTANT ✦" with animated glow
2. **ASCII Art**: Ice Spice logo/name in stylized ASCII
3. **Quote**: Rotating verified quotes from interviews
4. **Footer**: Control hints

## 💬 Featured Quotes

All quotes are verified from actual 2024 interviews:
- Rolling Stone cover story (July 2024)
- Complex interviews
- Billboard Women in Music 2024
- Grammy red carpet interviews

Sample quotes:
> "I won, bro. I win at life." - Rolling Stone

> "I'm constantly evolving while still staying true to myself." - Interview 2024

> "When I was in the studio with Taylor, I'll never forget that." - Billboard

## 🛠️ Customization

### Add Your Own Quotes

Edit `munch.py` and modify the `QUOTES` list:

```python
QUOTES = [
    "Your custom quote here",
    "Add as many as you want",
]
```

### Change Colors

Modify the color pairs in `munch.py`:

```python
curses.init_pair(1, curses.COLOR_YELLOW, -1)   # ASCII art color
curses.init_pair(2, curses.COLOR_CYAN, -1)     # Quote color
curses.init_pair(3, curses.COLOR_MAGENTA, -1)  # Accent color
```

Available colors:
- `COLOR_BLACK`, `COLOR_RED`, `COLOR_GREEN`, `COLOR_YELLOW`
- `COLOR_BLUE`, `COLOR_MAGENTA`, `COLOR_CYAN`, `COLOR_WHITE`

### Adjust Quote Rotation Speed

Change the interval in `munch.py`:

```python
quote_interval = 5  # Change to desired seconds
```

## 📁 Project Structure

```
munch-assistant/
├── munch.py          # Main Python application
├── run.sh            # Quick run script (Unix/Linux/Mac)
├── requirements.txt  # Dependencies (Windows only)
├── README.md         # This file
├── index.html        # Web version (legacy)
├── styles.css        # Web version (legacy)
└── script.js         # Web version (legacy)
```

## 🐛 Troubleshooting

### "Terminal too small!" message

Resize your terminal window to at least 50×25 characters.

### Colors not showing

Make sure you're using a terminal that supports colors:
- **Mac**: Terminal.app or iTerm2
- **Linux**: GNOME Terminal, Konsole, or xterm
- **Windows**: Windows Terminal (recommended), not CMD

### curses module not found (Windows)

Install the Windows curses library:

```bash
pip install windows-curses
```

## 🎓 Technical Details

- **Language**: Python 3.6+
- **Library**: `curses` (standard library on Unix/Linux/Mac)
- **Animation**: Custom glow effects with timed updates
- **Input**: Non-blocking keyboard input
- **Layout**: Dynamic centering based on terminal size

## 🌟 Why Terminal?

Terminal applications are:
- ⚡ **Fast** - No browser overhead
- 🎨 **Retro** - Classic ASCII art aesthetic
- 🔧 **Lightweight** - No dependencies (except Windows)
- 😎 **Cool** - Runs anywhere you have a terminal

## 📝 License

This project is open source and free to use for any purpose.

## 🎵 Credits

- **Quotes**: All quotes verified from Ice Spice's 2024 interviews
- **Created with**: Python, curses, and ❤️ for Ice Spice fans!

## ⚠️ Note

This project contains verified interview quotes from public sources, not copyrighted song lyrics. All quotes are properly attributed to Ice Spice from her interviews with Rolling Stone, Complex, Billboard, and other verified sources.

---

**Made with 🎤 by fans, for fans**

Enjoy the vibes! Press `q` when you're done.
