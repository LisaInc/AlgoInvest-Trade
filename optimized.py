import csv
import time


MAX_PRICE = 500


class Action:
    def __init__(self, id, price, profit):
        self.id = id
        self.price = int(price)
        self.profit_percent = int(profit)

    def get_profit_in_euro(self):
        return self.price * (self.profit_percent / 100)


def create_matrice(actions):
    matrice = {}
    sublist = [0 for _ in range(MAX_PRICE * 100)]
    for i, action in enumerate(actions):
        matrice[action] = sublist
    return matrice


def calculate_matrice(matrice, actions):
    for action in matrice.keys():
        for price_max, price in enumerate(matrice[action]):
            if action.price * 100 <= price_max:
                print("rentre")


with open("actions.csv", "r") as csv_file:
    actions_csv = csv.reader(csv_file)
    actions = [Action(*action) for action in actions_csv]

    matrice = create_matrice(actions)
    calculate_matrice(matrice, actions)
