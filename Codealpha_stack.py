
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "AMZN": 140
}

portfolio = {}
total_investment = 0

print("Available stocks:", ", ".join(stock_prices.keys()))


while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    
    if stock not in stock_prices:
        print("Stock not available.")
        continue
    
    quantity = int(input("Enter quantity: "))
    portfolio[stock] = quantity


print("\n--- Portfolio Summary ---")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_investment += value
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")
save = input("\nSave to file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock},{qty},{stock_prices[stock]}\n")
        file.write(f"Total Investment: ${total_investment}")
    
    print("Portfolio saved to portfolio.txt")