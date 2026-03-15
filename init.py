"""
TextArtisan - A professional ASCII art and text banner generation library
Create stunning text banners with fonts, colors, gradients, and animations
"""

from .banner import Banner
from .fonts import Fonts
from .effects import Effects
from .utils import Utils

__version__ = "1.0.0"
__all__ = ["Banner", "Fonts", "Effects", "Utils"]

# Convenience function for quick banner creation
def create(text, font="standard", color=None, gradient=None, width=80):
    """Quick banner creation with minimal setup"""
    banner = Banner()
    return banner.generate(text, font=font, color=color, gradient=gradient, width=width)

# CLI entry point
def main():
    """Command-line interface for TextArtisan"""
    import argparse
    import sys
    
    parser = argparse.ArgumentParser(description="TextArtisan - Create beautiful ASCII art banners")
    parser.add_argument("text", help="Text to convert to banner")
    parser.add_argument("-f", "--font", default="standard", help="Font style (default: standard)")
    parser.add_argument("-c", "--color", help="Single color for banner")
    parser.add_argument("-g", "--gradient", nargs=2, metavar=("COLOR1", "COLOR2"), 
                       help="Gradient from color1 to color2")
    parser.add_argument("-a", "--animate", choices=["rainbow", "blink", "typing", "scroll"], 
                       help="Animation effect")
    parser.add_argument("-w", "--width", type=int, default=80, help="Output width (default: 80)")
    parser.add_argument("-o", "--output", help="Save to file instead of printing")
    parser.add_argument("-b", "--border", help="Add border with specified character")
    parser.add_argument("--list-fonts", action="store_true", help="List available fonts")
    
    args = parser.parse_args()
    
    if args.list_fonts:
        fonts = Fonts.get_available_fonts()
        print("\n🎨 TextArtisan - Available Fonts:")
        print("=" * 40)
        for i, font in enumerate(fonts, 1):
            print(f"  {i}. {font}")
        print("=" * 40)
        sys.exit(0)
    
    banner = Banner()
    result = banner.generate(
        args.text,
        font=args.font,
        color=args.color,
        gradient=args.gradient,
        width=args.width
    )
    
    # Add border if requested
    if args.border:
        utils = Utils()
        result_lines = result.split('\n')
        result_lines = utils.add_border(result_lines, args.border)
        result = '\n'.join(result_lines)
    
    if args.animate:
        effects = Effects()
        print("\n" + "=" * 60)
        print(f"✨ TextArtisan Animation: {args.animate}".center(60))
        print("=" * 60 + "\n")
        
        if args.animate == "rainbow":
            effects.rainbow_animation(result)
        elif args.animate == "blink":
            effects.blink_animation(result)
        elif args.animate == "typing":
            effects.typing_animation(result)
        elif args.animate == "scroll":
            effects.scroll_animation(result)
    else:
        if args.output:
            with open(args.output, 'w') as f:
                f.write(result)
            print(f"\n✅ Banner saved to {args.output}")
        else:
            print("\n" + result)

if __name__ == "__main__":
    main()