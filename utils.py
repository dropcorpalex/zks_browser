# utils.py

def to_hex(number):
    """Convert a number to hexadecimal."""
    return hex(number)

def from_hex(hex_string):
    """Convert a hexadecimal string to a number."""
    return int(hex_string, 16)
