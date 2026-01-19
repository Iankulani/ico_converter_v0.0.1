from PIL import Image
import os

def simple_ico_converter():
    """Simple ICO converter with prompts"""
    
    print("=== Simple ICO Converter ===\n")
    
    # Get input filename
    while True:
        input_file = input("Enter the image filename to convert (e.g., spider.png): ")
        
        if os.path.exists(input_file):
            break
        else:
            print(f"File '{input_file}' not found. Please try again.\n")
    
    # Get output filename
    base_name = os.path.splitext(input_file)[0]
    output_file = input(f"Enter ICO filename (press Enter for '{base_name}.ico'): ")
    
    if not output_file:
        output_file = f"{base_name}.ico"
    
    # Add .ico extension if not present
    if not output_file.lower().endswith('.ico'):
        output_file += '.ico'
    
    # Convert and save
    try:
        print(f"\nConverting '{input_file}' to '{output_file}'...")
        
        img = Image.open(input_file)
        
        # Handle transparency
        if img.mode in ('RGBA', 'LA'):
            print("Note: Converting image with transparency to RGB format...")
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'RGBA':
                background.paste(img, mask=img.split()[-1])
            else:
                background.paste(img, mask=img.split()[0])
            img = background
        
        # Save as ICO with multiple sizes
        img.save(output_file, format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (32, 32)])
        
        print(f"\n✅ Success! File saved as '{output_file}'")
        print(f"File location: {os.path.abspath(output_file)}")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
    
    input("\nPress Enter to exit...")

# Run the simple converter
if __name__ == "__main__":
    simple_ico_converter()