import random  # Import the random module to use for fluctuating asset prices

class Asset:
    def __init__(self, name, initial_price): # a special method name in Python that indicates this method is a constructor.
        # Constructor for the Asset class, initializes the asset with a name and an initial price

        #self is a reference to the current instance of the class. 
        #It allows the method to access the attributes and methods of the class.
        
        self.name = name  # Store the name of the asset
        self.price = initial_price  # Store the initial price of the asset


    def fluctuate(self):
        # Method to randomly change the price of the asset
        change_percent = random.uniform(-0.1, 0.1)  # Generate a random percentage change between -10% and +10%
        self.price *= (1 + change_percent)  # Adjust the price based on the percentage change
        self.price = round(self.price, 2)  # Round the price to two decimal places for simplicity


class Portfolio:
    def __init__(self):
        # Constructor for the Portfolio class, initializes with starting cash and an empty holdings dictionary
        self.cash = 1000  # Set starting cash to $1000
        self.holdings = {}  # Initialize an empty dictionary to hold the assets and their quantities


    def buy(self, asset, amount):
        # Method to buy a specified amount of an asset
        total_cost = asset.price * amount  # Calculate the total cost of the purchase
        if total_cost <= self.cash:  # Check if there is enough cash to complete the purchase
            self.cash -= total_cost  # Deduct the total cost from the available cash
            if asset.name in self.holdings:  # Check if the asset is already in the holdings
                self.holdings[asset.name] += amount  # Increase the quantity of the asset in the holdings
            else:
                self.holdings[asset.name] = amount  # Add the asset to the holdings with the specified quantity
            print(f"Bought {amount} of {asset.name}")  # Print a message confirming the purchase
        else:
            print("Not enough cash to complete the purchase")  # Print a message if there isn't enough cash


    def sell(self, asset, amount):
        # Method to sell a specified amount of an asset
        if asset.name in self.holdings and self.holdings[asset.name] >= amount:
            # Check if the asset is in the holdings and if there is enough quantity to sell
            self.cash += asset.price * amount  # Increase the cash by the total value of the sold assets
            self.holdings[asset.name] -= amount  # Decrease the quantity of the asset in the holdings
            if self.holdings[asset.name] == 0: # If all units of the asset have been sold
                del self.holdings[asset.name]  # Remove the asset from the holdings
            print(f"Sold {amount} of {asset.name}")  # Print a message confirming the sale
        else:
            print("Not enough holdings to complete the sale")  # Print a message if there isn't enough quantity


    def view_portfolio(self, assets):
        # Method to view the current portfolio including cash and assets
        print("\nYour Portfolio:")  # Print the portfolio header
        print(f"Cash: ${self.cash:.2f}")  # Print the available cash, formatted to two decimal places
        total_value = self.cash  # Initialize the total value of the portfolio with the available cash
        for asset_name, amount in self.holdings.items():  # Loop through each asset in the holdings
            asset_value = amount * assets[asset_name].price  # Calculate the total value of the current asset
            total_value += asset_value  # Add the asset's total value to the portfolio's total value
            print(f"{asset_name}: {amount} units at ${assets[asset_name].price:.2f} each (Total: ${asset_value:.2f})")
            # Print the details of the current asset, including its name, quantity, price, and total value
        print(f"Total Portfolio Value: ${total_value:.2f}\n")  # Print the total value of the portfolio


def main():
    # Main function to run the simulation game
    stock = Asset("Stock", 100)  # Create a stock asset with an initial price of $100
    crypto = Asset("Crypto", 50)  # Create a crypto asset with an initial price of $50
    assets = {"Stock": stock, "Crypto": crypto}  # Store the assets in a dictionary for easy access


    portfolio = Portfolio()  # Create a new portfolio


    while True:
        # Infinite loop to continuously run the game until the user chooses to exit
        for asset in assets.values():  # Loop through each asset in the dictionary
            asset.fluctuate()  # Randomly fluctuate the price of each asset


        # Display the current prices of the assets
        print(f"\nCurrent Prices:")
        for asset in assets.values():  # Loop through each asset again
            print(f"{asset.name}: ${asset.price:.2f}")  # Print the name and price of each asset


        # Get the user's action choice
        action = input("\nDo you want to [buy], [sell], [view] portfolio, or [exit]? ").strip().lower()
        if action == "buy":
            # If the user chooses to buy
            asset_name = input("Which asset do you want to buy (Stock/Crypto)? ").strip().capitalize()
            if asset_name in assets:  # Check if the entered asset name is valid
                amount = int(input(f"How many units of {asset_name} do you want to buy? "))  # Get the amount to buy
                portfolio.buy(assets[asset_name], amount)  # Call the buy method to purchase the asset
            else:
                print("Invalid asset name")  # Print a message if the asset name is invalid
        elif action == "sell":
            # If the user chooses to sell
            asset_name = input("Which asset do you want to sell (Stock/Crypto)? ").strip().capitalize()
            if asset_name in assets:  # Check if the entered asset name is valid
                amount = int(input(f"How many units of {asset_name} do you want to sell? "))  # Get the amount to sell
                portfolio.sell(assets[asset_name], amount)  # Call the sell method to sell the asset
            else:
                print("Invalid asset name")  # Print a message if the asset name is invalid
        elif action == "view":
            # If the user chooses to view their portfolio
            portfolio.view_portfolio(assets)  # Call the view_portfolio method to display the portfolio
        elif action == "exit":
            # If the user chooses to exit
            break  # Exit the infinite loop, ending the game
        else:
            print("Invalid action")  # Print a message if the entered action is invalid


if __name__ == "__main__":
    main()  # Call the main function to start the game