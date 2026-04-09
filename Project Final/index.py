import subprocess
import threading

from main import main_process # type: ignore


# Step 1: Wrap your assistant logic
def run_voice_assistant():
    main_process()  # This is your assistant loop

# Step 2: Gesture control runner
def run_gesture_script():
    try:
        subprocess.run(["python", "gesture_control.py"])
    except Exception as e:
        print("Error running gesture_control.py:", e)

# Step 3: Start both together
if __name__ == "__main__":
    assistant_thread = threading.Thread(target=run_voice_assistant)
    gesture_thread = threading.Thread(target=run_gesture_script)

    assistant_thread.start()
    gesture_thread.start()

    assistant_thread.join()
    gesture_thread.join()
