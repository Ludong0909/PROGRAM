import numpy as np

def smooth_data(data, window_size):
    """Compute a moving average of a given dataset with a specified window size.

    Args:
        data (list): A list of numbers to be smoothed.
        window_size (int): The number of data points to include in the moving window.

    Returns:
        list: A list of smoothed values, where each value is the average of the `window_size` adjacent values in the original dataset.

    """
    half_window = (window_size - 1) // 2
    smoothed_data = []
    for i in range(len(data)):
        if i < half_window:
            # Not enough data points to compute a full window on the left
            smoothed_data.append(data[i])
        elif i >= len(data) - half_window:
            # Not enough data points to compute a full window on the right
            smoothed_data.append(data[i])
        else:
            # Compute the average of the window
            window_sum = sum(data[i - half_window:i + half_window + 1])
            window_average = window_sum / window_size
            smoothed_data.append(window_average)
    return smoothed_data

# Example usage
data = [1, 3, 2 ,4 ,5 ,7 ,8 ,10]
window_size = 3
smoothed_data = smooth_data(data, window_size)
print(smoothed_data)
