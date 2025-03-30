def calculate_discount(price, discount_percentage):
    """
    Calculate the final price after applying a discount.
    If the discount is 20% or higher, apply the discount.
    Otherwise, return the original price.
    """
    if discount_percentage >= 20:
        discount_amount = price * (discount_percentage / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

try:
    price = float(input("Enter the price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    final_price = calculate_discount(price, discount_percentage)

    if final_price < price:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")

