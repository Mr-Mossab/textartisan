"""
Color, gradient, and animation effects for TextArtisan
"""

import time
import sys
from typing import List, Optional, Tuple

class Colors:
    """ANSI color codes for TextArtisan"""
    # Standard colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'
    
    # Bright colors
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    # Styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    STRIKE = '\033[9m'

class Effects:
    """Visual effects for TextArtisan banners"""
    
    def __init__(self):
        self.color_map = {
            'black': Colors.BLACK,
            'red': Colors.RED,
            'green': Colors.GREEN,
            'yellow': Colors.YELLOW,
            'blue': Colors.BLUE,
            'magenta': Colors.MAGENTA,
            'cyan': Colors.CYAN,
            'white': Colors.WHITE,
            'bright_red': Colors.BRIGHT_RED,
            'bright_green': Colors.BRIGHT_GREEN,
            'bright_yellow': Colors.BRIGHT_YELLOW,
            'bright_blue': Colors.BRIGHT_BLUE,
            'bright_magenta': Colors.BRIGHT_MAGENTA,
            'bright_cyan': Colors.BRIGHT_CYAN,
            'bright_white': Colors.BRIGHT_WHITE,
        }
    
    def apply_color(self, ascii_lines: List[str], color: str) -> List[str]:
        """Apply a single color to all lines"""
        color_code = self.color_map.get(color.lower(), Colors.RESET)
        return [f"{color_code}{line}{Colors.RESET}" for line in ascii_lines]
    
    def apply_gradient(self, ascii_lines: List[str], 
                       start_color: str, end_color: str) -> List[str]:
        """Apply gradient across the banner"""
        start_rgb = self._hex_to_rgb(start_color) if start_color.startswith('#') else None
        end_rgb = self._hex_to_rgb(end_color) if end_color.startswith('#') else None
        
        if not start_rgb or not end_rgb:
            return ascii_lines
        
        colored_lines = []
        num_lines = len(ascii_lines)
        
        for i, line in enumerate(ascii_lines):
            # Calculate color for this line
            ratio = i / (num_lines - 1) if num_lines > 1 else 0
            r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * ratio)
            g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * ratio)
            b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * ratio)
            
            # Convert RGB to ANSI 256 color
            color_code = self._rgb_to_ansi(r, g, b)
            colored_lines.append(f"\033[38;5;{color_code}m{line}{Colors.RESET}")
        
        return colored_lines
    
    def rainbow_animation(self, banner: str, delay: float = 0.1, iterations: int = 0):
        """Animate banner with rainbow colors"""
        rainbow_colors = [
            Colors.RED, Colors.YELLOW, Colors.GREEN, 
            Colors.CYAN, Colors.BLUE, Colors.MAGENTA
        ]
        
        try:
            count = 0
            while iterations == 0 or count < iterations:
                for color in rainbow_colors:
                    sys.stdout.write('\033[2J\033[H')  # Clear screen
                    sys.stdout.write(f"{color}{banner}{Colors.RESET}")
                    sys.stdout.flush()
                    time.sleep(delay)
                    count += 1
                    if iterations > 0 and count >= iterations:
                        break
        except KeyboardInterrupt:
            sys.stdout.write(Colors.RESET)
            print("\n\n✨ Animation stopped by user")
    
    def blink_animation(self, banner: str, delay: float = 0.5, iterations: int = 10):
        """Make banner blink"""
        try:
            for i in range(iterations):
                sys.stdout.write('\033[2J\033[H')
                sys.stdout.write(banner)
                sys.stdout.flush()
                time.sleep(delay)
                sys.stdout.write('\033[2J\033[H')
                sys.stdout.flush()
                time.sleep(delay)
        except KeyboardInterrupt:
            print("\n\n✨ Animation stopped by user")
    
    def typing_animation(self, banner: str, delay: float = 0.03):
        """Simulate typing effect"""
        sys.stdout.write('\033[2J\033[H')
        sys.stdout.write(f"{Colors.BRIGHT_GREEN}")  # Green text for typing
        
        for char in banner:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        
        sys.stdout.write(Colors.RESET)
        print()
    
    def scroll_animation(self, banner: str, delay: float = 0.1, direction: str = 'up'):
        """Scroll banner vertically"""
        lines = banner.split('\n')
        terminal_height = self._get_terminal_height()
        
        try:
            while True:
                for i in range(len(lines)):
                    sys.stdout.write('\033[2J\033[H')
                    visible_lines = lines[i:i+terminal_height]
                    sys.stdout.write('\n'.join(visible_lines))
                    sys.stdout.flush()
                    time.sleep(delay)
        except KeyboardInterrupt:
            print("\n\n✨ Animation stopped by user")
    
    def pulse_animation(self, banner: str, delay: float = 0.1):
        """Pulse effect (brightness variation)"""
        try:
            while True:
                for intensity in range(0, 100, 10):
                    sys.stdout.write('\033[2J\033[H')
                    sys.stdout.write(f"\033[38;5;{intensity}m{banner}{Colors.RESET}")
                    sys.stdout.flush()
                    time.sleep(delay)
                for intensity in range(100, 0, -10):
                    sys.stdout.write('\033[2J\033[H')
                    sys.stdout.write(f"\033[38;5;{intensity}m{banner}{Colors.RESET}")
                    sys.stdout.flush()
                    time.sleep(delay)
        except KeyboardInterrupt:
            print("\n\n✨ Animation stopped by user")
    
    def _hex_to_rgb(self, hex_color: str) -> Tuple[int, int, int]:
        """Convert hex color to RGB tuple"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def _rgb_to_ansi(self, r: int, g: int, b: int) -> int:
        """Convert RGB to ANSI 256 color code"""
        # Simplified conversion
        return 16 + (36 * (r // 51)) + (6 * (g // 51)) + (b // 51)
    
    def _get_terminal_height(self) -> int:
        """Get terminal height in lines"""
        import shutil
        return shutil.get_terminal_size().lines