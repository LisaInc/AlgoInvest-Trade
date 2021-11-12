import csv
from os import sys


MAX_PRICE = 500


class Action:
    def __init__(self, id, price, profit):
        self.id = id
        self.price = float(price)
        self.profit_euro = float(price) * (float(profit) / 100)


with open(sys.argv[1], "r") as csv_file:
    actions_csv = csv.reader(csv_file)
    actions = [Action(*action) for action in actions_csv]
    actions_sorted = sorted(
        actions, key=lambda action: action.profit_euro, reverse=True
    )
    remaining_price = MAX_PRICE
    result = []
    profit = 0
    for action in actions_sorted:
        if remaining_price >= action.price:
            result.append(action)
            remaining_price -= action.price
            profit += action.profit_euro

    print(f"{profit:.2f} €")
    for action in result:
        print(action.id)
    print(sum(action.price for action in result))
