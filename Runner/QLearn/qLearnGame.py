import numpy as np
import pickle, time, pygame
import matplotlib.pyplot as plt
from matplotlib import style
from Resources import config as c
import Resources.Tiles.Player as Cell
from Resources import helpers
from pynput.keyboard import Key, Controller

style.use("ggplot")
keyboard = Controller()
keys = {0: Key.up, 1: Key.right, 2: Key.down, 3: Key.left}

SIZE = c.N
N_OF_EPISODES = 25000
MOVE_PENALTY = 1
GOAL_REWARD = 25
epsilon = 0.9
EPS_DECAY = 0.9998
SHOW_EVERY = 3000
HM_STEPS = 200

Start_qTable = None  # Filename

LEARNING_RATE = 0.1
DISCOUNT = 0.95
steps =[]

# PyGame setup
pygame.init()
screen = pygame.display.set_mode([c.WIDTH,c.HEIGHT])
clock = pygame.time.Clock()

# Setup qTable
if Start_qTable is None:  # make the qTable if it doesn't exist
    qTable = {}
    for x1 in range(-SIZE + 1, SIZE):
        for y1 in range(-SIZE + 1, SIZE):
                qTable[(x1, y1)] = [np.random.uniform(-5, 0) for i in range(4)]

else:  # if a filename is provided, load it
    with open(Start_qTable, "rb") as f:
        qTable = pickle.load(f)
    f.close()


episode_rewards = []
for epi in range(N_OF_EPISODES):
    grid = np.load("/Resources/maze.npy", allow_pickle=True)

    # set tiles
    player = Cell.Player(grid)
    goal = grid[grid.shape[0] - 1, grid.shape[1] - 1]
    goal.color = (255, 255, 0)
    goal.reward = 1

    if epi % SHOW_EVERY == 0:
        print(f"on #{epi}, epsilon is {epsilon}")
        print(f"{SHOW_EVERY} ep mean: {np.mean(episode_rewards[-SHOW_EVERY:])}")
        show = True
    else:
        show = False

    episode_reward = 0
    for i in range(HM_STEPS):
        obs = (player - goal)

        if np.random.random() > epsilon:
            action = np.argmax(qTable[obs])
        else:
            action = np.random.randint(0, 4)

        player.step(action)
        steps.append(action)

        if player.x == goal.x and player.y == goal.y:
            reward = GOAL_REWARD
        else:
            reward = -MOVE_PENALTY

        newObs = (player - goal)
        maxFutureQ = np.max(qTable[newObs])
        currentQ = qTable[obs][action]
        if reward == GOAL_REWARD:
            newQ = GOAL_REWARD
        else:
            newQ = (1 - LEARNING_RATE) * currentQ + LEARNING_RATE * (reward + DISCOUNT * maxFutureQ)

        qTable[obs][action] = newQ

        if show:
            if reward == GOAL_REWARD:
                time.sleep(2)
                break
            else:
                break

        episode_reward += reward
        if reward == GOAL_REWARD:
            break

    episode_rewards.append(episode_reward)
    epsilon *= EPS_DECAY

movingAvg = np.convolve(episode_rewards, np.ones((SHOW_EVERY,))/SHOW_EVERY, mode='valid')
plt.plot([i for i in range(len(movingAvg))], movingAvg)
plt.ylabel(f"Reward {SHOW_EVERY}ma")
plt.xlabel("episode #")
plt.show()

for i in steps:
    print(i)
    keyboard.press(keys[i])
    keyboard.release(keys[i])
    # time.sleep(1)

with open(f"X:\Projects\MazeRunner\Runner\QLearn\qTable-{int(time.time())}.pickle", "wb") as f:
    pickle.dump(qTable, f)
    f.close()

print(steps)
with open ("X:\Projects\MazeRunner\Runner\QLearn\steps.pickle", "wb") as f:
    pickle.dump(steps,f)
    f.close()



