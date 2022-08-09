# Homework 1
# Author: Peter Bachman
# Date: 08/??/2022

# Import a few modules
import random


# Portfolio class
class Portfolio:
    def __init__(self):
        self.history = {}
        self.portfolio = {"Cash": 0}

    # Print what is in the portfolio
    def __str__(self):
        print("cash: $" + self.portfolio["Cash"])

    # Add Cash Function
    def addCash(self, cash):
        if cash < 0:
            print("Cannot add a negative amount of cash")
        else:
            self.portfolio["Cash"] += cash

    # Withdraw Cash Function
    def withdrawCash(self, cash):
        # Cannot withdraw more cash than the accout has, and also cannot
        # withdraw a negative amount of cash
        if cash > self.portfolio["Cash"]:
            print("Cannot withdraw more cash than is in account.")
        elif cash < 0:
            print("Cannot withdraw negative amount.")
        else:
            self.portfolio["Cash"] -= cash

    # Buy Mutual Fund Function
    def buyMutualFund(self, amt, mtf):
        if amt > self.portfolio["Cash"]:
            print("Cannot buy more shares than you can afford.")
        elif amt < 0:
            print("Cannot buy negative amount of shares.")
        else:
            self.portfolio["Cash"] -= amt
            self.portfolio[mtf.name] = [amt, "Mutual Fund"]
            self.history(mtf.name, "Mutual Fund", "Buy", amt, 1)

    # Sell Mutual Fund Function
    def sellMutualFund(self, amt, mtf):
        if self.portfolio[mtf.name][0] < amt:
            print("Cannot sell more shares than you have")
        else:
            self.portfolio["Cash"] += amt * mtf.sellPrice
            self.portfolio[mtf.name][0] -= amt
            self.history(mtf.name, "Mutual Fund", "Sell", amt, mtf.sellPrice)
            # Remove value from dictionary if all shares are sold
            if self.portfolio[mtf.name][0] == 0:
                self.portfolio.pop(mtf.name)

    # Buy Stock Function
    def buyStock(self, stock, amt):
        if amt * stock.buyPrice > self.portfolio["Cash"]:
            print("Cannot buy more shares than you can afford.")
        elif amt < 0:
            print("Cannot buy negative amount of shares.")
        elif type(amt) != int:
            print("Stock amount must be an integer.")
        else:
            self.portfolio["Cash"] -= amt
            self.portfolio[stock.name] = [amt, "Stock"]
            self.history(stock.name, "Stock", "Buy", amt, stock.buyPrice)

    # Sell Stock Function
    def sellStock(self, stock, amt):
        if self.portfolio[stock.name][0] < amt:
            print("Cannot sell more shares than you have")
        else:
            self.portfolio["Cash"] += amt * stock.sellPrice
            self.portfolio[stock.name][0] -= amt
            self.history(stock.name, "Stock", "Sell", amt, stock.sellPrice)
            # Remove value from dictionary if all shares are sold
            if self.portfolio[stock.name][0] == 0:
                self.portfolio.pop(stock.name)

    # History Function
    def history(self, name, fund, transaction, amt, price):
        self.history[len(self.history)] = {"Name": name,
                                           "Fund Type": fund,
                                           "Transaction Type": transaction,
                                           "Amount": amt,
                                           "Price Per Share": price,
                                           "Total Price": price * amt}


# Mutual Fund Class
class MutualFund:
    def __init__(self, symbol):
        self.name = symbol
        self.sellPrice = random.uniform(0.9, 1.2)


# Stock Class
class Stock:
    def __init__(self, price, symbol):
        self.name = symbol
        self.buyPrice = price
        self.sellPrice = price * random.uniform(0.5, 1.5)

# TEST CLASSES
portfolio = Portfolio()
portfolio.addCash(300.50)
s = Stock(20, "HFH")
portfolio.buyStock(5, s)
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
portfolio.buyMutualFund(10.3, mf1)
portfolio.buyMutualFund(2, mf2)
print(portfolio)
portfolio.sellMutualFund("BRT", 3)
portfolio.sellStock("HFH", 1)
portfolio.withdrawCash(50)
portfolio.history()
