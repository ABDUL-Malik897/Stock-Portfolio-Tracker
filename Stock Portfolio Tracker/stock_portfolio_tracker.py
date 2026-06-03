stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320,
    "AMZN": 150
}

total_investment = 0
portfolio = []

print("\nAvailable Stocks and Prices:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")


num_stocks = int(input("\nHow many different stocks do you want to buy? "))


for i in range(num_stocks):
    print(f"\nStock Entry {i + 1}")
    stock_name = input("Enter stock name: ").upper()
    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        stock_price = stock_prices[stock_name]
        investment = stock_price * quantity
        total_investment += investment
        portfolio.append([stock_name, quantity, stock_price, investment])
        print(f"Added {quantity} shares of {stock_name}")
        print(f"Investment Amount: ${investment}")
    else:
        print("Stock not available in database.")

for item in portfolio:
    print(f"Stock: {item[0]}")
    print(f"Quantity: {item[1]}")
    print(f"Price per Share: ${item[2]}")
    print(f"Total Investment: ${item[3]}")

print(f"\nTotal Portfolio Value = ${total_investment}")

file = open("portfolio.txt", "w")

file.write("Portfolio Summary -->\n")

for item in portfolio:
    file.write(f"Stock: {item[0]}\n")
    file.write(f"Quantity: {item[1]}\n")
    file.write(f"Price per Share: ${item[2]}\n")
    file.write(f"Total Investment: ${item[3]}\n")

file.write(f"\nTotal Portfolio Value = ${total_investment}")
file.close()
print("\nPortfolio summary saved successfully in 'portfolio.txt'")