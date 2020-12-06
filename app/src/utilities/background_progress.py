import time

def show_progress(window, progress_bar):
    """

    Args:
        window: TKinter root frame
        progress_bar: progressbar object

    Returns: updates the progressbar value attribute
    and updates the window (no return value)

    """
    steps = 100
    counter = 0
    while counter < steps:
        time.sleep(0.01)
        progress_bar["value"] += 1
        counter += 1
        window.update_idletasks()
