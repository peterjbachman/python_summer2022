# Homework 1
# Author: Peter Bachman
# Date: 08/13/2022

# Import module
import random


# Portfolio class
class Portfolio:
    def __init__(self):
        # Set up variables in the class
        self.transactions = {}
        self.historyLine = 1
        self.portfolio = {"Cash": 0}

    # Print what is in the portfolio
    def __str__(self):
        # First create the report line
        report = "cash: $" + str(self.portfolio["Cash"]) + "\n"
        reportStock = "stock: "
        reportMF = "mutual fund: "
        firstStock = True
        firstMF = True
        # For each key in the dicitionary
        for i in enumerate(self.portfolio.keys()):
            # Exclude the dictionary value for 'Cash'
            if i[0] == 0:
                continue
            name = i[1]
            # If the dictionary value is a stock, add to the stock string
            if self.portfolio[name][1] == "Stock":
                # If it's the first stock to show up, append it to the string
                # and then line break
                if firstStock:
                    reportStock += str(self.portfolio[name][0]) + \
                        " " + name + "\n"
                    firstStock = False
                # Sort of a hacked job of doing line justifications but it
                # works for now.
                else:
                    reportStock += "       " + str(self.portfolio[name][0]) + \
                        name + "\n"
            # Do the same with the mutual funds
            if self.portfolio[name][1] == "Mutual Fund":
                if firstMF:
                    reportMF += "{:.2f}".format(self.portfolio[name][0]) + \
                        " " + name + "\n"
                    firstMF = False
                else:
                    reportMF += "             " + \
                        "{:.2f}".format(self.portfolio[name][0]) + \
                        " " + name + "\n"
        report += reportStock + reportMF
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
            self.portfolio[mtf.name] = [amt, "Mutual Fund"]
            self.transaction(mtf.name, "Mutual Fund", "Buy", amt, 1)

    # Sell Mutual Fund Function
    def sellMutualFund(self, mtf, amt):
        """Sell Mutual Funds

        Args:
            mtf (str): Name of Mutual Fund already added to portfolio
            amt (float): non-negative amount
        """
        sellPrice = random.uniform(0.9, 1.2)
        if self.portfolio[mtf][0] < amt:
            print("Cannot sell more shares than you have")
        else:
            self.portfolio["Cash"] += amt * sellPrice
            self.portfolio[mtf][0] -= amt
            self.transaction(mtf, "Mutual Fund", "Sell", amt,
                             sellPrice)
            # Remove value from dictionary if all shares are sold
            if self.portfolio[mtf][0] == 0:
                self.portfolio.pop(mtf)

    # Buy Stock Function
    # These are the same as the mutual fund functions.
    def buyStock(self, amt, stock):
        if amt * stock.buyPrice > self.portfolio["Cash"]:
            print("Cannot buy more shares than you can afford.")
        elif amt < 0:
            print("Cannot buy negative amount of shares.")
        elif type(amt) != int:
            print("Stock amount must be an integer.")
        else:
            self.portfolio["Cash"] -= amt
            self.portfolio[stock.name] = [amt, "Stock", stock.buyPrice]
            self.transaction(stock.name, "Stock", "Buy", amt, stock.buyPrice)

    # Sell Stock Function
    def sellStock(self, stock, amt):
        sellPrice = self.portfolio[stock][2] * random.uniform(0.5, 1.5)
        if self.portfolio[stock][0] < amt:
            print("Cannot sell more shares than you have")
        else:
            self.portfolio["Cash"] += amt * sellPrice
            self.portfolio[stock][0] -= amt
            self.transaction(stock, "Stock", "Sell", amt, sellPrice)
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
    def history(self):
        # For each of the keys in the transaction dictionary, print out
        # the details of the transaction
        for i in enumerate(self.transactions.keys()):
            string = "Name: " + self.transactions[i[1]]["Name"] + "\n"
            string += "    Type: " + \
                self.transactions[i[1]]["Fund Type"] + "\n"
            string += "    Transaction: " + \
                self.transactions[i[1]]["Transaction Type"] + "\n"
            string += "    Amount: " + \
                str(self.transactions[i[1]]["Amount"]) + "\n"
            string += "    Price Per Share: " + \
                str(self.transactions[i[1]]["Price Per Share"]) + "\n"
            string += "    Total Price: " + \
                str(self.transactions[i[1]]["Total Price"]) + "\n"
            print(string)


# Mutual Fund Class
class MutualFund:
    def __init__(self, symbol):
        self.name = symbol


# Stock Class
class Stock:
    def __init__(self, price, symbol):
        self.name = symbol
        self.buyPrice = price


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
