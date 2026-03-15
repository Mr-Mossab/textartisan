"""
Core banner generation functionality for TextArtisan
"""

import os
import sys
from typing import List, Optional, Tuple
from .fonts import Fonts
from .effects import Effects
from .utils import Utils

class Banner:
    """Main banner generator class for TextArtisan"""
    
    def __init__(self):
        self.fonts = Fonts()
        self.effects = Effects()
        self.utils = Utils()
        
    def generate(self, 
                 text: str, 
                 font: str = "standard", 
                 color: Optional[str] = None,
                 gradient: Optional[Tuple[str, str]] = None,
                 width: int = 80,
                 border: Optional[str] = None) -> str:
        """
        Generate an ASCII banner
        
        Args:
            text: Text to convert to banner
            font: Font style name
            color: Single color for banner (None for no color)
            gradient: Tuple of (start_color, end_color) for gradient
            width: Maximum width for centering
            border: Character to use for border (None for no border)
            
        Returns:
            ASCII banner as string
        """
        # Validate inputs
        if not text:
            return ""
            
        # Get the ASCII art
        ascii_lines = self.fonts.get_font(text, font)
        
        # Apply colors if requested
        if gradient and len(gradient) == 2:
            ascii_lines = self.effects.apply_gradient(ascii_lines, gradient[0], gradient[1])
        elif color:
            ascii_lines = self.effects.apply_color(ascii_lines, color)
        
        # Center the banner
        ascii_lines = self.utils.center_text(ascii_lines, width)
        
        # Add border if requested
        if border:
            ascii_lines = self.utils.add_border(ascii_lines, border)
        
        return '\n'.join(ascii_lines)
    
    def save(self, text: str, filename: str, **kwargs) -> None:
        """Generate and save banner to file"""
        try:
            banner = self.generate(text, **kwargs)
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(banner)
            print(f"✅ Banner saved to {filename}")
        except Exception as e:
            print(f"❌ Error saving banner: {e}")
    
    def preview(self, text: str, **kwargs) -> None:
        """Preview banner with all available fonts"""
        available_fonts = self.fonts.get_available_fonts()
        
        print("\n" + "=" * 60)
        print("🎨 TextArtisan Font Preview".center(60))
        print("=" * 60 + "\n")
        
        for i, font in enumerate(available_fonts, 1):
            print(f"\n{'─' * 60}")
            print(f"Font {i}: {font.upper()}".center(60))
            print(f"{'─' * 60}\n")
            print(self.generate(text, font=font, **kwargs))
            
            if i < len(available_fonts):
                input("\n⏎ Press Enter to continue...")
        
        print("\n" + "=" * 60)
        print("✨ Preview Complete".center(60))
        print("=" * 60)