# Calculate Final Price After Discount
def calculate_discount(price, discount_percent):
    return price - (price * (discount_percent / 100)) if discount_percent >= 20 else price


# prompting user for input
price = float(input("Original price: "))
discount_percent = float(input("Discount percentage: "))

# Final Price Calculation
print(f"Final price: {calculate_discount(price, discount_percent):.2f}")
