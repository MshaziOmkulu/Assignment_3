def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if the discount is 20% or more.

    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage.

    Returns:
    float: The final price after applying the discount if applicable.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price

# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: $"))
    discount = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount)

    if discount >= 20:
        print(f"Discount applied. The final price is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The final price remains: ${final_price:.2f}")

except ValueError:
    print("Please enter valid numeric values for price and discount.")
