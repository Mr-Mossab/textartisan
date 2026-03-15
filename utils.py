"""
Utility functions for TextArtisan banner manipulation
"""

import os
import sys
import time
from typing import List, Optional, Tuple

class Utils:
    """Helper utilities for TextArtisan banner operations"""
    
    @staticmethod
    def center_text(ascii_lines: List[str], width: int = 80) -> List[str]:
        """Center each line of ASCII art"""
        centered = []
        for line in ascii_lines:
            # Remove ANSI color codes for length calculation
            clean_line = Utils._strip_ansi(line)
            if len(clean_line) < width:
                padding = (width - len(clean_line)) // 2
                centered.append(' ' * padding + line)
            else:
                centered.append(line)
        return centered
    
    @staticmethod
    def add_border(ascii_lines: List[str], border_char: str = '*', 
                   title: Optional[str] = None) -> List[str]:
        """Add a decorative border around the banner"""
        if not ascii_lines:
            return ascii_lines
        
        # Remove ANSI codes for length calculation
        clean_lines = [Utils._strip_ansi(line) for line in ascii_lines]
        max_length = max(len(line) for line in clean_lines)
        
        # Create border
        top_border = border_char * (max_length + 4)
        bottom_border = border_char * (max_length + 4)
        
        bordered = [top_border]
        
        # Add title if provided
        if title:
            title_line = f"{border_char} {title.center(max_length)} {border_char}"
            bordered.append(title_line)
            bordered.append(border_char * (max_length + 4))
        
        # Add content with borders
        for i, line in enumerate(ascii_lines):
            clean_len = len(clean_lines[i])
            padding = max_length - clean_len
            bordered.append(f"{border_char} {line}{' ' * padding} {border_char}")
        
        bordered.append(bottom_border)
        
        return bordered
    
    @staticmethod
    def reverse_colors(ascii_lines: List[str]) -> List[str]:
        """Reverse video effect (swap foreground/background)"""
        return [f"\033[7m{line}\033[0m" for line in ascii_lines]
    
    @staticmethod
    def save_to_file(banner: str, filename: str) -> None:
        """Save banner to file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(banner)
            print(f"✅ Banner saved to {filename}")
        except Exception as e:
            print(f"❌ Error saving banner: {e}")
    
    @staticmethod
    def print_slowly(banner: str, delay: float = 0.01):
        """Print banner character by character"""
        for char in banner:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    @staticmethod
    def get_terminal_size() -> Tuple[int, int]:
        """Get terminal size (width, height)"""
        import shutil
        size = shutil.get_terminal_size()
        return size.columns, size.lines
    
    @staticmethod
    def wrap_text(text: str, width: int = 80) -> str:
        """Wrap text to specified width"""
        words = text.split()
        lines = []
        current_line = []
        current_length = 0
        
        for word in words:
            if current_length + len(word) + 1 <= width:
                current_line.append(word)
                current_length += len(word) + 1
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word)
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return '\n'.join(lines)
    
    @staticmethod
    def preview_fonts(text: str, fonts_dict: Optional[dict] = None) -> None:
        """Preview text in all available fonts"""
        from .fonts import Fonts
        
        available_fonts = Fonts.get_available_fonts()
        
        print("\n" + "=" * 60)
        print("🎨 TextArtisan Font Preview".center(60))
        print("=" * 60 + "\n")
        
        for font_name in available_fonts:
            print(f"\n{'─' * 60}")
            print(f"Font: {font_name.upper()}".center(60))
            print(f"{'─' * 60}\n")
            
            banner = Fonts.get_font(text, font_name)
            print('\n'.join(banner))
            input("\n⏎ Press Enter to continue...")
    
    @staticmethod
    def create_rainbow_text(text: str) -> str:
        """Create rainbow-colored text (each character different color)"""
        rainbow_colors = [
            '\033[91m',  # Red
            '\033[93m',  # Yellow
            '\033[92m',  # Green
            '\033[96m',  # Cyan
            '\033[94m',  # Blue
            '\033[95m',  # Magenta
        ]
        
        result = ''
        for i, char in enumerate(text):
            color = rainbow_colors[i % len(rainbow_colors)]
            result += f"{color}{char}"
        
        return result + '\033[0m'
    
    @staticmethod
    def _strip_ansi(text: str) -> str:
        """Remove ANSI color codes from text"""
        import re
        ansi_pattern = re.compile(r'\x1b\[[0-9;]*m')
        return ansi_pattern.sub('', text)
    
    @staticmethod
    def get_banner_info(banner: str) -> dict:
        """Get information about the banner"""
        lines = banner.split('\n')
        clean_lines = [Utils._strip_ansi(line) for line in lines]
        
        return {
            'height': len(lines),
            'width': max(len(line) for line in clean_lines) if clean_lines else 0,
            'line_count': len(lines),
            'character_count': sum(len(line) for line in clean_lines),
            'has_color': '\033[' in banner
        }