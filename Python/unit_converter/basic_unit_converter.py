# Function for unit conversion
def convert_units(value, from_unit, to_unit):
    """
    Convert a value from one unit to another.
    
    Parameters:
        value (float): The value to convert
        from_unit (str): The unit to convert from
        to_unit (str): The unit to convert to
    
    Returns:
        float: The converted value
    """
    conversion_factors = {
        'km_to_miles': 0.621371,
        'miles_to_km': 1.60934,
        'kg_to_pounds': 2.20462,
        'pounds_to_kg': 0.453592
    }
    
    key = f"{from_unit}_to_{to_unit}"
    if key not in conversion_factors:
        raise ValueError("Conversion not supported.")
    return value * conversion_factors[key]

# Example usage
if __name__ == "__main__":
    print("10 kilometers in miles:", convert_units(10, 'km', 'miles'))
    print("50 pounds in kilograms:", convert_units(50, 'pounds', 'kg'))
