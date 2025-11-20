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
from textwrap import wrap

# Try to import pygame for audio
try:
    import pygame
    AUDIO_AVAILABLE = True
except ImportError:
    AUDIO_AVAILABLE = False

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
ASCII_ART = r"""
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
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:
"""

# Required terminal size for THE QUEEN
REQUIRED_WIDTH = 90
REQUIRED_HEIGHT = 50

def init_audio():
    """Initialize audio playback"""
    if not AUDIO_AVAILABLE:
        return False

    try:
        pygame.mixer.init()
        audio_file = os.path.join(os.path.dirname(__file__), "munch.wav")
        if os.path.exists(audio_file):
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play(-1)  # Loop forever
            return True
    except Exception as e:
        return False
    return False

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

def draw_ascii_art(stdscr, start_y, color_pair=1):
    """Draw ASCII art centered"""
    lines = ASCII_ART.strip().split('\n')
    height, width = stdscr.getmaxyx()

    for i, line in enumerate(lines):
        if start_y + i < height:
            x = max(0, (width - len(line)) // 2)
            if x < width:
                try:
                    stdscr.addstr(start_y + i, x, line[:width-1],
                                curses.color_pair(color_pair) | curses.A_BOLD)
                except curses.error:
                    pass
    return len(lines)

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
    stdscr.timeout(100) # 100ms timeout

    # Initialize colors
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_YELLOW, -1)    # Gold for ASCII art
    curses.init_pair(2, curses.COLOR_CYAN, -1)      # Cyan for quotes
    curses.init_pair(3, curses.COLOR_MAGENTA, -1)   # Magenta accent
    curses.init_pair(4, curses.COLOR_RED, -1)       # Red for warnings

    current_quote = 0
    glow_state = 0
    last_quote_change = time.time()
    quote_interval = 5  # Change quote every 5 seconds

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # CHECK IF TERMINAL IS WORTHY OF THE QUEEN
        if height < REQUIRED_HEIGHT or width < REQUIRED_WIDTH:
            show_resize_demand(stdscr)
            time.sleep(0.1)

            # Check for quit
            key = stdscr.getch()
            if key in [ord('q'), ord('Q'), 27]:  # q, Q, or ESC
                break
            continue

        # Calculate positions
        art_lines = ASCII_ART.strip().count('\n') + 1
        total_height = art_lines + 10  # Art + spacing + quote
        start_y = max(0, (height - total_height) // 2)

        # Draw header with glow effect
        glow_char = ['✦', '✧', '✨', '✧'][glow_state % 4]
        header = f"{glow_char} MUNCH ASSISTANT {glow_char}"
        draw_centered_text(stdscr, start_y, header, 3, bold=True)

        # Draw ASCII art
        art_end_y = draw_ascii_art(stdscr, start_y + 2, 1)

        # Draw quote
        quote_y = start_y + 2 + art_end_y + 2
        draw_quote(stdscr, quote_y, QUOTES[current_quote], 2)

        # Draw footer
        footer_y = height - 2
        audio_status = "🎵 AUDIO ON" if AUDIO_AVAILABLE else "🔇 Install pygame for audio"
        draw_centered_text(stdscr, footer_y - 1, audio_status, 3)
        draw_centered_text(stdscr, footer_y, "Press 'q' to quit • Press 'n' for next quote", 3)

        stdscr.refresh()

        # Update animation
        glow_state += 1

        # Auto-change quote
        if time.time() - last_quote_change > quote_interval:
            current_quote = (current_quote + 1) % len(QUOTES)
            last_quote_change = time.time()

        # Handle input
        key = stdscr.getch()
        if key in [ord('q'), ord('Q'), 27]:  # q, Q, or ESC
            break
        elif key in [ord('n'), ord('N'), ord(' ')]:  # n, N, or Space
            current_quote = (current_quote + 1) % len(QUOTES)
            last_quote_change = time.time()

        time.sleep(0.1)

def run():
    """Run the application"""
    # Initialize audio first
    audio_started = init_audio()

    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass
    finally:
        # Stop audio
        if AUDIO_AVAILABLE:
            try:
                pygame.mixer.music.stop()
                pygame.mixer.quit()
            except:
                pass

    print("\n👑 Thanks for vibing with Ice Spice! You're a MUNCH! 🎤✨")

if __name__ == "__main__":
    if not AUDIO_AVAILABLE:
        print("⚠️  Warning: pygame not installed. Running without audio.")
        print("   Install with: pip install pygame")
        print()
    run()
