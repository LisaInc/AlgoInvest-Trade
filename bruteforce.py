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


def sum_price(actions):
    return sum(action.price for action in actions)


def get_profit(actions):
    return sum(action.get_profit_in_euro() for action in actions)


def get_all_sum_action(actions):
    start_time = time.time()
    all_sum_actions = [[]]
    for action in actions:
        new_all_sum_actions = all_sum_actions.copy()
        for sum_actions in all_sum_actions:
            sum_actions_copy = sum_actions.copy()
            sum_actions_copy.append(action)
            if sum_price(sum_actions_copy) <= MAX_PRICE:
                new_all_sum_actions.append(sum_actions_copy)
        all_sum_actions = new_all_sum_actions.copy()
    all_sum_actions.pop(0)
    print("--- %s seconds --- get_all_sum_actions" % (time.time() - start_time))
    return all_sum_actions


def get_best_actions(all_sum_actions):
    start_time = time.time()
    best_profit = 0
    for sum_actions in all_sum_actions:
        if get_profit(sum_actions) > best_profit:
            best_profit = get_profit(sum_actions)
            best_actions = sum_actions.copy()
    print("--- %s seconds --- get_best_action" % (time.time() - start_time))
    return best_actions, best_profit


with open("actions.csv", "r") as csv_file:
    actions_csv = csv.reader(csv_file)
    actions = [Action(*action) for action in actions_csv]
    best_choice_profit = 0
    all_sum_actions = get_all_sum_action(actions)
    best_actions, best_profit = get_best_actions(all_sum_actions)
    print(f"{best_profit:.2f} €")
    for action in best_actions:
        print(action.id, action.price)

    print(sum(action.price for action in best_actions))
