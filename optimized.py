import csv
import time
from os import sys


MAX_PRICE = 5


class Action:
    def __init__(self, id, price, profit):
        self.id = id
        self.price = int(price)
        self.profit_percent = int(profit)

    def get_profit_in_euro(self):
        return self.price * (self.profit_percent / 100)


def create_matrice(actions):
    matrice = {}
    sublist = [0 for _ in range(MAX_PRICE + 1)]
    for i in enumerate(actions):
        matrice.append(sublist)
    return matrice


def calculate_matrice(matrice):
    previous_action = None
    for action in range(len(matrice)):
        for price_max in range(len(matrice[action])):
            if action.price <= price_max:
                matrice[action][price_max] += action.profit_percent
            if previous_action:
                if (price_max - action.price) != 0:
                    previous_action_row = matrice[previous_action][
                        price_max - action.price
                    ]
                    print(previous_action_row)
                    matrice[action][price_max] += previous_action_row
                if matrice[previous_action][price_max] > matrice[action][price_max]:
                    matrice[action][price_max] = matrice[previous_action][price_max]
                print(
                    action.id,
                    matrice[previous_action],
                    matrice[action],
                )
        previous_action = action


with open(sys.argv[1], "r") as csv_file:
    actions_csv = csv.reader(csv_file)
    actions = [Action(*action) for action in actions_csv]

    matrice = create_matrice(actions)
    calculate_matrice(matrice)
