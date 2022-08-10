# Homework 1
# Author: Peter Bachman
# Date: 08/??/2022

# TODO Finish print function
# TODO Format print function correctly
# TODO Finish history function
# TODO Create Comments for functions
# TODO Sell Price is changed every time, not set to the class
# TODO Create proper errors?

# Import a few modules
import random


# Portfolio class
class Portfolio:
    def __init__(self):
        self.transactions = {}
        self.historyLine = 1
        self.portfolio = {"Cash": 0}

    # Print what is in the portfolio
    # NOT FINISHED
    def __str__(self):
        report = "cash: $" + str(self.portfolio["Cash"])
        return report

    def addCash(self, cash):
        """Add cash to the Portfolio class

        Args:
            cash (float): Non-negative number
        """

        if cash < 0:
            print("Cannot add a negative amount of cash")
        else:
            self.portfolio["Cash"] += cash

    def withdrawCash(self, cash):
        """Remove cash from the Portfolio class

        Args:
            cash (float): Non-negative number
        """

        # Cannot withdraw more cash than the accout has, and also cannot
        # withdraw a negative amount of cash
        if cash > self.portfolio["Cash"]:
            print("Cannot withdraw more cash than is in account.")
        elif cash < 0:
            print("Cannot withdraw negative amount.")
        else:
            self.portfolio["Cash"] -= cash

    def buyMutualFund(self, amt, mtf):
        """Purchase shares of a Mutual Fund

        Args:
            amt (float): Non-negative number
            mtf (Class): Mutual Fund Class
        """

        if amt > self.portfolio["Cash"]:
            print("Cannot buy more shares than you can afford.")
        elif amt < 0:
            print("Cannot buy negative amount of shares.")
        else:
            self.portfolio["Cash"] -= amt
            self.portfolio[mtf.name] = [amt, "Mutual Fund", mtf.sellPrice]
            self.transaction(mtf.name, "Mutual Fund", "Buy", amt, 1)

    # Sell Mutual Fund Function
    def sellMutualFund(self, mtf, amt):
        if self.portfolio[mtf][0] < amt:
            print("Cannot sell more shares than you have")
        else:
            self.portfolio["Cash"] += amt * self.portfolio[mtf][2]
            self.portfolio[mtf][0] -= amt
            self.transaction(mtf, "Mutual Fund", "Sell", amt,
                             self.portfolio[mtf][2])
            # Remove value from dictionary if all shares are sold
            if self.portfolio[mtf][0] == 0:
                self.portfolio.pop(mtf)

    # Buy Stock Function
    def buyStock(self, amt, stock):
        if amt * stock.buyPrice > self.portfolio["Cash"]:
            print("Cannot buy more shares than you can afford.")
        elif amt < 0:
            print("Cannot buy negative amount of shares.")
        elif type(amt) != int:
            print("Stock amount must be an integer.")
        else:
            self.portfolio["Cash"] -= amt
            self.portfolio[stock.name] = [amt, "Stock", stock.sellPrice]
            self.transaction(stock.name, "Stock", "Buy", amt, stock.buyPrice)

    # Sell Stock Function
    def sellStock(self, stock, amt):
        if self.portfolio[stock][0] < amt:
            print("Cannot sell more shares than you have")
        else:
            self.portfolio["Cash"] += amt * self.portfolio[stock][2]
            self.portfolio[stock][0] -= amt
            self.transaction(stock, "Stock", "Sell", amt,
                             self.portfolio[stock][2])
            # Remove value from dictionary if all shares are sold
            if self.portfolio[stock][0] == 0:
                self.portfolio.pop(stock)

    # Transaction Function: Tracks the transactions made
    def transaction(self, name, fund, type, amt, price):
        historyLine = str(len(self.transactions) + 1)
        self.transactions[historyLine] = {"Name": name,
                                          "Fund Type": fund,
                                          "Transaction Type": type,
                                          "Amount": amt,
                                          "Price Per Share": price,
                                          "Total Price": price * amt}

    # History Function
    # NOT FINISHED
    def history(self):
        print(self.transactions)


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
