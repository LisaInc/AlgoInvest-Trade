import os
import csv
import time

import matplotlib.pyplot as plt

actions = [
    "Action-1",
    20,
    5,
    "Action-2",
    30,
    10,
    "Action-3",
    50,
    15,
    "Action-4",
    70,
    20,
    "Action-5",
    60,
    17,
    "Action-6",
    80,
    25,
    "Action-7",
    22,
    7,
    "Action-8",
    26,
    11,
    "Action-9",
    48,
    13,
    "Action-10",
    34,
    27,
    "Action-11",
    42,
    17,
    "Action-12",
    110,
    9,
    "Action-13",
    38,
    23,
    "Action-14",
    14,
    1,
    "Action-15",
    18,
    3,
    "Action-16",
    8,
    8,
    "Action-17",
    4,
    12,
    "Action-18",
    10,
    14,
    "Action-19",
    24,
    21,
    "Action-20",
    114,
    18,
]
times = []
os.system("rm actions_test.csv")
os.system("touch actions_test.csv")
while actions:
    with open("actions_test.csv", "a") as csv_file:
        writer = csv.writer(
            csv_file, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL
        )
        print(actions)
        writer.writerow([actions[0], actions[1], actions[2]])

    start_time = time.time()
    os.system("python3 bruteforce.py actions_test.csv")
    times.append(time.time() - start_time)
    print("--- %s seconds --- get_all_sum_actions" % (time.time() - start_time))
    for _ in range(3):
        actions.pop(0)

nb_actions = [i for i in range(1, 21)]

plt.plot(nb_actions, times)
plt.savefig("foo.png")
