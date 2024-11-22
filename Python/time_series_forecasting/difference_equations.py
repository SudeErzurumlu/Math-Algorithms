import numpy as np
import matplotlib.pyplot as plt

# Function for first-order difference equation prediction
def predict_next(values, coefficients):
    """
    Predict the next value in a time series using a first-order difference equation.
    
    Parameters:
        values (list): The past values in the time series
        coefficients (list): Coefficients of the difference equation
    
    Returns:
        float: Predicted next value
    """
    return sum(c * v for c, v in zip(coefficients, values))

# Example usage
if __name__ == "__main__":
    time_series = [100, 105, 110, 120]  # Example data
    coeffs = [0.8, 0.2]  # Example coefficients
    
    predicted = predict_next(time_series[-2:], coeffs)
    print("Predicted Next Value:", predicted)
