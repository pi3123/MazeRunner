import pickle, time
from pynput.keyboard import Key, Controller

path = "X:\Projects\MazeRunner\Runner\QLearn\steps.pickle"

with open(path, "rb") as f:
    steps = pickle.load(f)
    f.close()
keyboard = Controller()
keys = {0: Key.up, 1: Key.right, 2: Key.down, 3: Key.left}

print(steps)
time.sleep(5)

for i in steps:
    print(i)
    keyboard.press(keys[i])
    keyboard.release(keys[i])
    time.sleep(1)

