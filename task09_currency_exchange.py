USD_Amount = float(input("Enter the amount in USD:"))
Exchange_Rate = float(input("Enter the exchange rate:"))
ETB_Amount = USD_Amount * Exchange_Rate
print(f"The amount in ETB is: {ETB_Amount}ETB")