# 🎤 Munch Assistant

**Terminal-based animated ASCII art featuring Ice Spice with rotating verified quotes AND AUDIO!**

![Terminal Animation](https://img.shields.io/badge/Terminal-Animation-yellow?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.6+-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Unix%20%7C%20Linux%20%7C%20Mac%20%7C%20Windows-green?style=for-the-badge)
![Audio](https://img.shields.io/badge/Audio-Enabled-red?style=for-the-badge)

## 👑 BOW DOWN TO THE SPICE QUEEN 👑

This is not your average terminal app. Ice Spice demands RESPECT and SCREEN SPACE!

## ✨ Features

- **🎨 MASSIVE ASCII Art** - Full-size artwork that commands your attention
- **🎵 AUDIO PLAYBACK** - Looping music/beats while you vibe
- **💬 Verified Quotes** - Real Ice Spice quotes from 2024 interviews (Rolling Stone, Complex, Billboard)
- **⚡ Auto-Rotation** - Quotes change automatically every 5 seconds
- **🎯 Centered Display** - Always perfectly centered, no scrolling
- **🌈 Colorful** - Vibrant terminal colors with bold styling
- **⌨️ Interactive** - Press 'n' for next quote, 'q' to quit
- **💅 DEMANDS RESPECT** - Requires 90×50 terminal or the Queen won't show!

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

### 2. Install Dependencies (REQUIRED for audio!)

```bash
pip install pygame
```

Or install all requirements:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
chmod +x run.sh
./run.sh
```

Or directly:

```bash
python3 munch.py
```

### Windows Users

Install both pygame and windows-curses:

```bash
pip install pygame windows-curses
python munch.py
```

## 🎮 Controls

| Key | Action |
|-----|--------|
| `q` or `Q` | Quit the application |
| `n` or `N` or `Space` | Next quote |
| `ESC` | Exit |

## 📐 Terminal Requirements

### 👑 THE QUEEN'S DEMANDS 👑

- **REQUIRED SIZE**: **90 columns × 50 rows MINIMUM**
- **Color Support**: Absolutely required
- **Audio**: pygame installed for the full experience

**If your terminal is too small, you'll see this message:**
> 👑 BOW DOWN TO THE SPICE QUEEN 👑
>
> Your terminal is TOO SMALL!
>
> RESIZE YOUR TERMINAL OR BUY A BIGGER MONITOR! 💅

The app will NOT run until you resize. Ice Spice demands respect!

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
├── munch.wav         # Audio file (21MB) - Plays on loop
├── run.sh            # Quick run script (Unix/Linux/Mac)
├── requirements.txt  # Dependencies
├── README.md         # This file
├── index.html        # Web version (legacy)
├── styles.css        # Web version (legacy)
└── script.js         # Web version (legacy)
```

## 🎵 Audio

The app includes a `munch.wav` file that loops continuously while you vibe. The audio starts automatically when you run the app (if pygame is installed).

**No audio?** Make sure pygame is installed:
```bash
pip install pygame
```

## 🐛 Troubleshooting

### "Terminal too small!" message

THE QUEEN HAS SPOKEN! Resize your terminal to at least **90×50** characters. No compromises!

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
