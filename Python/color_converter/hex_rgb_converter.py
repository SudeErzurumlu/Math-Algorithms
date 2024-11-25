# Function to convert HEX color to RGB
def hex_to_rgb(hex_color):
    """
    Convert a HEX color code to RGB format.
    
    Parameters:
        hex_color (str): The HEX color code (e.g., "#FFFFFF")
    
    Returns:
        tuple: RGB representation as (R, G, B)
    """
    hex_color = hex_color.lstrip('#')
    if len(hex_color) != 6:
        raise ValueError("Invalid HEX color format")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Function to convert RGB color to HEX
def rgb_to_hex(r, g, b):
    """
    Convert an RGB color to HEX format.
    
    Parameters:
        r (int): Red value (0-255)
        g (int): Green value (0-255)
        b (int): Blue value (0-255)
    
    Returns:
        str: HEX color code (e.g., "#FFFFFF")
    """
    if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
        raise ValueError("RGB values must be in the range 0-255")
    return f"#{r:02X}{g:02X}{b:02X}"

# Example usage
if __name__ == "__main__":
    hex_color = "#1E90FF"
    rgb_color = hex_to_rgb(hex_color)
    print(f"HEX {hex_color} to RGB:", rgb_color)

    rgb_color = (30, 144, 255)
    hex_color = rgb_to_hex(*rgb_color)
    print(f"RGB {rgb_color} to HEX:", hex_color)
