"""
ASCII font definitions and management for TextArtisan
"""

from typing import Dict, List, Optional

class Fonts:
    """Collection of ASCII fonts for TextArtisan"""
    
    # Standard ASCII font
    STANDARD = {
        'A': ['  █████  ',
              ' ██   ██ ',
              ' ███████ ',
              ' ██   ██ ',
              ' ██   ██ '],
        'B': [' ██████  ',
              ' ██   ██ ',
              ' ██████  ',
              ' ██   ██ ',
              ' ██████  '],
        'C': ['  ██████ ',
              ' ██      ',
              ' ██      ',
              ' ██      ',
              '  ██████ '],
        'D': [' ██████  ',
              ' ██   ██ ',
              ' ██   ██ ',
              ' ██   ██ ',
              ' ██████  '],
        'E': [' ███████ ',
              ' ██      ',
              ' █████   ',
              ' ██      ',
              ' ███████ '],
        'F': [' ███████ ',
              ' ██      ',
              ' █████   ',
              ' ██      ',
              ' ██      '],
        'G': ['  ██████ ',
              ' ██      ',
              ' ██  ███ ',
              ' ██   ██ ',
              '  ██████ '],
        'H': [' ██   ██ ',
              ' ██   ██ ',
              ' ███████ ',
              ' ██   ██ ',
              ' ██   ██ '],
        'I': [' ███████ ',
              '   ██    ',
              '   ██    ',
              '   ██    ',
              ' ███████ '],
        'J': [' ███████ ',
              '    ██   ',
              '    ██   ',
              ' ██ ██   ',
              '  ███    '],
        'K': [' ██   ██ ',
              ' ██  ██  ',
              ' █████   ',
              ' ██  ██  ',
              ' ██   ██ '],
        'L': [' ██      ',
              ' ██      ',
              ' ██      ',
              ' ██      ',
              ' ███████ '],
        'M': [' ██    ██ ',
              ' ███  ███ ',
              ' ██ ██ ██ ',
              ' ██    ██ ',
              ' ██    ██ '],
        'N': [' ██    ██ ',
              ' ███   ██ ',
              ' ██ █  ██ ',
              ' ██  █ ██ ',
              ' ██   ███ '],
        'O': ['  █████  ',
              ' ██   ██ ',
              ' ██   ██ ',
              ' ██   ██ ',
              '  █████  '],
        'P': [' ██████  ',
              ' ██   ██ ',
              ' ██████  ',
              ' ██      ',
              ' ██      '],
        'Q': ['  █████  ',
              ' ██   ██ ',
              ' ██   ██ ',
              ' ██   ██ ',
              '  ██████ '],
        'R': [' ██████  ',
              ' ██   ██ ',
              ' ██████  ',
              ' ██  ██  ',
              ' ██   ██ '],
        'S': ['  ██████ ',
              ' ██      ',
              '  █████  ',
              '     ██  ',
              ' ██████  '],
        'T': [' ███████ ',
              '   ██    ',
              '   ██    ',
              '   ██    ',
              '   ██    '],
        'U': [' ██   ██ ',
              ' ██   ██ ',
              ' ██   ██ ',
              ' ██   ██ ',
              '  █████  '],
        'V': [' ██   ██ ',
              ' ██   ██ ',
              ' ██   ██ ',
              '  ██ ██  ',
              '   ███   '],
        'W': [' ██     ██ ',
              ' ██     ██ ',
              ' ██  █  ██ ',
              ' ██ ███ ██ ',
              '  ███ ███  '],
        'X': [' ██   ██ ',
              '  ██ ██  ',
              '   ███   ',
              '  ██ ██  ',
              ' ██   ██ '],
        'Y': [' ██   ██ ',
              '  ██ ██  ',
              '   ███   ',
              '   ██    ',
              '   ██    '],
        'Z': [' ███████ ',
              '    ██   ',
              '   ██    ',
              '  ██     ',
              ' ███████ '],
        ' ': ['      ',
              '      ',
              '      ',
              '      ',
              '      '],
        '!': ['   ██   ',
              '   ██   ',
              '   ██   ',
              '        ',
              '   ██   '],
        '?': ['  ████  ',
              ' ██  ██ ',
              '   ██   ',
              '        ',
              '   ██   '],
    }
    
    # Block font (simple but bold)
    BLOCK = {
        'A': [' ▄▄▄ ',
              '█   █',
              '█▄▄▄█',
              '█   █',
              '█   █'],
        'B': [' ▄▄▄ ',
              '█   █',
              '█▄▄▄ ',
              '█   █',
              '█▄▄▄ '],
        'C': [' ▄▄▄ ',
              '█   ',
              '█   ',
              '█   ',
              ' ▄▄▄ '],
        # Add more block letters as needed
    }
    
    # Slant font (italic style)
    SLANT = {
        'A': ['   ▄▄  ',
              '  █  █ ',
              ' █▄▄▄█ ',
              '█     █',
              '█     █'],
        # Add more slant letters
    }
    
    # Digital font (LED style)
    DIGITAL = {
        'A': [' ╔══╗ ',
              ' ║  ║ ',
              ' ╠══╣ ',
              ' ║  ║ ',
              ' ║  ║ '],
        # Add more digital letters
    }
    
    # Fancy font (ornamental)
    FANCY = {
        'A': ['╔════╗',
              '║    ║',
              '╠════╣',
              '║    ║',
              '╚════╝'],
        # Add more fancy letters
    }
    
    # Retro font
    RETRO = {
        'A': ['  ▲▲▲  ',
              ' ██ ██ ',
              ' █████ ',
              ' ██ ██ ',
              ' ██ ██ '],
        # Add more retro letters
    }
    
    FONTS = {
        'standard': STANDARD,
        'block': BLOCK,
        'slant': SLANT,
        'digital': DIGITAL,
        'fancy': FANCY,
        'retro': RETRO
    }
    
    @classmethod
    def get_font(cls, text: str, font_name: str = 'standard') -> List[str]:
        """
        Convert text to ASCII art using specified font
        
        Args:
            text: Input text
            font_name: Name of font to use
            
        Returns:
            List of strings representing ASCII art lines
        """
        font = cls.FONTS.get(font_name.lower(), cls.STANDARD)
        text = text.upper()
        
        # Initialize lines
        result = [''] * 5  # All fonts use 5 lines
        
        # Build each character
        for char in text:
            if char in font:
                char_lines = font[char]
                for i in range(5):
                    result[i] += char_lines[i] + ' '
            else:
                # Handle spaces and unknown characters
                for i in range(5):
                    result[i] += '      '  # 5 spaces + 1 for separator
        
        return result
    
    @classmethod
    def get_available_fonts(cls) -> List[str]:
        """Return list of available font names"""
        return list(cls.FONTS.keys())
    
    @classmethod
    def add_custom_font(cls, name: str, font_dict: Dict) -> bool:
        """Add a custom font to the collection"""
        if name and font_dict and len(next(iter(font_dict.values()))) == 5:
            cls.FONTS[name.lower()] = font_dict
            return True
        return False