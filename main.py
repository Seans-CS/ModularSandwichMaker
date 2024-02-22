import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():

    print("Welcome to the sandwhich shop")

    while True:

        size = input("What size of sandwich would you like? (small, medium, large): ").lower()

        if size in ["small", "medium", "large"]:

            if sandwich_maker_instance.make_sandwich(size):
                print("Sandwich made successfully.")

                cost = data.recipes[size]['cost']

                if cashier_instance.transaction_result(coins=cashier_instance.process_coins(), cost=cost):
                    print("Transaction successful. Enjoy your sandwich!")
                    break
                else:
                    print("Transaction failed, not enough coins.")
            else:
                print("Failed to make the sandwich. Please try again.")
        else:
            print("Invalid sandwich size. Please choose from small, medium, or large.")


if __name__=="__main__":
    main()
