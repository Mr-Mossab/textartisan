from textartisan import Banner

def basic_examples():
    print("=" * 60)
    print("TEXTARTISAN - BASIC EXAMPLES".center(60))
    print("=" * 60)
    
    # Create banner instance
    banner = Banner()
    
    # Example 1: Simple banner
    print("\n1️⃣ SIMPLE BANNER:")
    print("-" * 40)
    result = banner.generate("Hello", font="standard")
    print(result)