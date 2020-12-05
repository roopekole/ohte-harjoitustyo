import time

def show_progress(window, bar):
    steps = 100
    x = 0
    while (x < steps):
        time.sleep(0.01)
        bar["value"] += 1
        x += 1
        window.update_idletasks()