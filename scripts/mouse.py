def freeze_mouse(duration=10):
    x, y = pyautogui.position()
    start_time = time.time()
    while time.time() - start_time < duration:
        pyautogui.moveTo(x, y)
        time.sleep(0.01)

if __name__ == "__main__":
    freeze_mouse()
