#!/usr/bin/env python3
"""
Munch Assistant - Ice Spice Terminal Art
Animated ASCII art with rotating quotes and AUDIO in your terminal
BOW DOWN TO THE SPICE QUEEN 👑
"""

import curses
import time
import os
import sys
import subprocess
import shutil
import importlib
from textwrap import wrap

# Try to import pygame for audio
try:
    import pygame
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False

AUDIO_METHOD = None
AUDIO_PROC = None
AUDIO_PLAYING = False

# Ice Spice verified quotes from interviews (2024)
QUOTES = [
    "I won, bro. I win at life.",
    "I'm constantly evolving while still staying true to myself.",
    "I like to record alone. I like to focus in to get the song done.",
    "I'm at a point in my career now where I'm more confident in my own decision-making.",
    "People only love you when nobody else does. But then once other people start to love you, people have to hate to balance it out.",
    "Which is so rude to me, because why would she not want to be my friend?",
    "I would say Lana Del Rey. I'm obsessed with her.",
    "When I was in the studio with Taylor, I'll never forget that.",
    "It's definitely an adjustment, but I have been adjusting to things. I'm not going to complain.",
    "I realized virality is really based on the person. When you're a viral type of person, you're gonna always go viral.",
]

# FULL ASCII ART - THE QUEEN DEMANDS YOUR SCREEN SPACE
DEFAULT_ASCII_ART = r"""
                                    .:--::.
                               .-=+++++++++==-:.
                            :=+++++++++++++++++++-.
                          :+++++++++++++++++++++++++=:
                        :++++++++++++++++++++++++++++++:
                      .=+++++++++++++++++++++++++++++++++-.
                     -++++++++++++++++++++++++++++++++++++++:
                   .++++++++++++++++++++++++++++++++++++++++++:
                  :+++++++++++++++++++++++++++++++++++++++++++++-
                 -+++++++++++++++++++++++++++++++++++++++++++++++=
                =+++++++++++++++++++++++++++++++++++++++++++++++++=
              .=+++++++++++++++++++++++++++++++++++++++++++++++++++=
             .++++++++++++++++++++++++++++++++++++++++++++++++++++++=
            :+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
           -++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:
          =++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
         =++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=
        =+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=
       =+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=
      -+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
     :+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
    .+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    =++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   =+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  .++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:
  =+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 :++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:
 =+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.
 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:
:++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:
=++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:
"""


def load_ascii_art():
    """Load ASCII art from ascii_art.txt if present, else fallback to default art."""
    art_path = os.path.join(os.path.dirname(__file__), "ascii_art.txt")
    if os.path.exists(art_path):
        try:
            with open(art_path, "r", encoding="utf-8", errors="replace") as f:
                art = f.read()
                # Avoid empty file edge case
                if art.strip("\n"):
                    return art
        except Exception:
            pass
    return DEFAULT_ASCII_ART


ASCII_ART = load_ascii_art()

# Pre-calc art dimensions so we can size the terminal to fit everything
ASCII_LINES = ASCII_ART.lstrip("\n").splitlines()
ART_HEIGHT = len(ASCII_LINES)
ART_WIDTH = max(len(line) for line in ASCII_LINES) if ASCII_LINES else 0

# Required terminal size for THE QUEEN (art + header/footer/quotes padding)
REQUIRED_WIDTH = ART_WIDTH + 10
REQUIRED_HEIGHT = ART_HEIGHT + 14


def auto_resize_terminal(rows: int, cols: int):
    """Ask the terminal to resize itself (xterm-compatible escape)."""
    try:
        sys.stdout.write(f"\x1b[8;{rows};{cols}t")
        sys.stdout.flush()
        time.sleep(0.05)
    except Exception:
        # If the terminal refuses the resize, fall back to resize prompt
        pass


def ensure_pygame_installed():
    """Offer to install pygame; prefer a local .venv when not already in one."""
    global PYGAME_AVAILABLE, pygame

    # In frozen/packaged builds (PyInstaller), skip install attempts
    if getattr(sys, "frozen", False):
        return False

    if PYGAME_AVAILABLE:
        return True

    print("pygame is not installed. Needed for in-app audio.")
    choice = input("Install pygame now? [Y/n]: ").strip().lower()
    if choice not in ("", "y", "yes"):
        return False

    try:
        base_python = sys.executable
        in_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
        venv_path = os.path.join(os.path.dirname(__file__), ".venv")
        python_cmd = base_python

        # If not already in a venv, create/use .venv to avoid polluting system
        if not in_venv:
            if not os.path.exists(venv_path):
                print("Creating .venv for pygame…")
                subprocess.run([base_python, "-m", "venv", venv_path], check=True)
            python_cmd = os.path.join(venv_path, "bin", "python3")
            if not os.path.exists(python_cmd):
                python_cmd = os.path.join(venv_path, "Scripts", "python.exe")

        print("Installing pygame…")
        subprocess.run([python_cmd, "-m", "pip", "install", "--upgrade", "pip"], check=False)
        subprocess.run([python_cmd, "-m", "pip", "install", "pygame"], check=True)

        # If we installed into a new venv, restart the script from that interpreter
        if python_cmd != sys.executable:
            print("Restarting app from .venv with pygame available…")
            os.execv(python_cmd, [python_cmd, __file__])

        # Otherwise reload in the same process
        importlib.invalidate_caches()
        pygame = importlib.import_module("pygame")
        PYGAME_AVAILABLE = True
        return True
    except Exception as e:
        print(f"Failed to install pygame automatically: {e}")
        return False

def start_external_audio(audio_file):
    """Play audio using common CLI players (ffplay/afplay/aplay/mpg123/paplay)."""
    global AUDIO_PROC, AUDIO_METHOD, AUDIO_PLAYING

    players = [
        ["ffplay", "-nodisp", "-autoexit", "-loop", "0", audio_file],
        ["afplay", audio_file],
        ["aplay", "--loop=0", audio_file],
        ["mpg123", "--loop", "-1", audio_file],
        ["paplay", audio_file],
    ]

    for cmd in players:
        if shutil.which(cmd[0]):
            try:
                AUDIO_PROC = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                AUDIO_METHOD = cmd[0]
                AUDIO_PLAYING = True
                return True
            except Exception:
                continue
    return False


def init_audio():
    """Initialize audio playback with pygame, otherwise try external players."""
    global AUDIO_PLAYING, AUDIO_METHOD

    audio_file = os.path.join(os.path.dirname(__file__), "munch.wav")
    if not os.path.exists(audio_file):
        return False

    if PYGAME_AVAILABLE:
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play(-1)  # Loop forever
            AUDIO_METHOD = "pygame"
            AUDIO_PLAYING = True
            return True
        except Exception:
            AUDIO_PLAYING = False

    return start_external_audio(audio_file)


def stop_audio():
    """Stop whichever audio backend we started."""
    global AUDIO_PROC, AUDIO_PLAYING, AUDIO_METHOD

    if AUDIO_METHOD == "pygame" and PYGAME_AVAILABLE:
        try:
            pygame.mixer.music.stop()
            pygame.mixer.quit()
        except Exception:
            pass
    elif AUDIO_PROC:
        try:
            AUDIO_PROC.terminate()
        except Exception:
            pass

    AUDIO_PROC = None
    AUDIO_PLAYING = False
    AUDIO_METHOD = None

def draw_centered_text(stdscr, y, text, color_pair=0, bold=False):
    """Draw text centered on screen"""
    height, width = stdscr.getmaxyx()
    x = max(0, (width - len(text)) // 2)
    if 0 <= y < height and x < width:
        try:
            attr = curses.color_pair(color_pair)
            if bold:
                attr |= curses.A_BOLD
            stdscr.addstr(y, x, text[:width-1], attr)
        except curses.error:
            pass

def draw_ascii_art(stdscr, start_y, color_pair=0, x_offset=0):
    """Draw ASCII art centered; optional horizontal sway via x_offset."""
    height, width = stdscr.getmaxyx()

    for i, line in enumerate(ASCII_LINES):
        if start_y + i < height:
            x = max(0, ((width - len(line)) // 2) + x_offset)
            if x < width:
                try:
                    attr = 0
                    if color_pair:
                        attr |= curses.color_pair(color_pair)
                    stdscr.addstr(start_y + i, x, line[:width-1], attr)
                except curses.error:
                    pass
    return len(ASCII_LINES)

def draw_quote(stdscr, start_y, quote, color_pair=2):
    """Draw quote wrapped and centered"""
    height, width = stdscr.getmaxyx()
    max_width = min(70, width - 4)
    wrapped_lines = wrap(f'"{quote}"', max_width)

    for i, line in enumerate(wrapped_lines):
        if start_y + i < height:
            draw_centered_text(stdscr, start_y + i, line, color_pair, bold=True)

    # Add attribution
    if start_y + len(wrapped_lines) + 1 < height:
        draw_centered_text(stdscr, start_y + len(wrapped_lines) + 1, "- Ice Spice", color_pair)

def show_resize_demand(stdscr):
    """Show the demand to resize terminal - THE QUEEN REQUIRES SPACE"""
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    messages = [
        "👑 BOW DOWN TO THE SPICE QUEEN 👑",
        "",
        "Your terminal is TOO SMALL!",
        "",
        f"REQUIRED: {REQUIRED_WIDTH} columns × {REQUIRED_HEIGHT} rows",
        f"YOU HAVE: {width} columns × {height} rows",
        "",
        "RESIZE YOUR TERMINAL OR BUY A BIGGER MONITOR! 💅",
        "",
        "Press 'q' to quit (if you're not ready for this energy)",
    ]

    start_y = max(0, (height - len(messages)) // 2)

    for i, msg in enumerate(messages):
        if start_y + i < height:
            color = 3 if i in [0, 7] else 1
            draw_centered_text(stdscr, start_y + i, msg, color, bold=True)

    stdscr.refresh()

def main(stdscr):
    """Main application loop"""
    # Setup
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)   # Non-blocking input
    stdscr.timeout(100) # refresh rate

    sway_offset = 0
    sway_direction = 1
    last_sway_change = time.time()
    sway_interval = 0.3  # adjust for slower sway

    while True:
        stdscr.erase()
        height, width = stdscr.getmaxyx()

        # CHECK IF TERMINAL IS WORTHY OF THE QUEEN
        if height < REQUIRED_HEIGHT or width < REQUIRED_WIDTH:
            # Try to auto-resize before we warn the user
            auto_resize_terminal(REQUIRED_HEIGHT, REQUIRED_WIDTH)
            height, width = stdscr.getmaxyx()

            if height < REQUIRED_HEIGHT or width < REQUIRED_WIDTH:
                show_resize_demand(stdscr)
                time.sleep(0.1)

                # Check for quit
                key = stdscr.getch()
                if key in [ord('q'), ord('Q'), 27]:  # q, Q, or ESC
                    break
                continue

        # Calculate positions for art only
        art_lines = ART_HEIGHT
        start_y = max(0, (height - art_lines) // 2)

        # Draw ASCII art only with gentle sway
        draw_ascii_art(stdscr, start_y, 0, sway_offset)

        stdscr.refresh()

        # Update sway
        now = time.time()
        if now - last_sway_change > sway_interval:
            sway_offset += sway_direction
            if sway_offset >= 2:
                sway_direction = -1
            elif sway_offset <= -2:
                sway_direction = 1
            last_sway_change = now

        # Handle input (only quit)
        key = stdscr.getch()
        if key in [ord('q'), ord('Q'), 27]:  # q, Q, or ESC
            break
        time.sleep(0.05)

def run():
    """Run the application"""
    # Initialize audio first
    audio_started = init_audio()

    # Auto-grow the terminal to fit the full ASCII art and UI
    auto_resize_terminal(REQUIRED_HEIGHT, REQUIRED_WIDTH)

    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass
    finally:
        stop_audio()

    print("\n👑 Thanks for vibing with Ice Spice! You're a MUNCH! 🎤✨")


if __name__ == "__main__":
    if not PYGAME_AVAILABLE:
        ensure_pygame_installed()
    run()
