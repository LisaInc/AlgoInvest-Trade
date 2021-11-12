import csv
from os import sys


MAX_PRICE = 500


class Action:
    def __init__(self, id, price, profit):
        self.id = id
        self.price = round(float(price), 2)
        self.profit_euro = self.get_profit_in_euro(round(float(profit), 2))

    def get_profit_in_euro(self, profit_percent):
        return self.price * (profit_percent / 100)


class Cell:
    def __init__(self, profit, actions):
        self.profit = profit
        self.actions = actions

    def get_cost_actions(self):
        return sum(action.price for action in self.actions)

    def merge_with(self, cell):
        self.profit += cell.profit
        for action in cell.actions:
            self.actions.append(action)


def calculate_matrice(actions):
    matrice = [
        [Cell(0, []) for _ in range(MAX_PRICE * 100)] for _ in range(len(actions))
    ]
    for index_row, row in enumerate(matrice):
        for index_column, cell in enumerate(row):
            if actions[index_row].price * 100 <= index_column:
                cell.profit += actions[index_row].profit_euro
                cell.actions.append(actions[index_row])

            if index_row != 0 and cell.get_cost_actions() * 100 < index_column:
                difference = index_column - int(cell.get_cost_actions() * 100)
                cell.merge_with(matrice[index_row - 1][difference])

            if (
                index_row != 0
                and matrice[index_row - 1][index_column].profit > cell.profit
            ):
                cell = matrice[index_row - 1][-1]
    return matrice[-1][-1]


with open(sys.argv[1], "r") as csv_file:
    actions_csv = csv.reader(csv_file)
    actions = [Action(*action) for action in actions_csv]
    result = calculate_matrice(actions)
    print(f"{result.profit:.2f} €")
    for action in result.actions:
        print(action.id)
    print(result.get_cost_actions())
