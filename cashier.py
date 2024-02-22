class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""

        total_amount = 0

        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickels = int(input("how many nickels?: "))
        pennies = int(input("how many pennies?: "))

        total_amount += quarters * 0.25
        total_amount += dimes * 0.10
        total_amount += nickels * 0.05
        total_amount += pennies * 0.01

        return total_amount

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            return True
        else:
            return False
