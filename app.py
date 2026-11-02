def cart_related(cart, item, quantity):
    """Add an item to the customer's cart."""
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    if item not in cart:
        cart[item] = 0

    cart[item] += quantity
    return cart


def place_order(cart):
    """Return a simple order summary."""
    total_items = sum(cart.values())
    return {
        "items": cart,
        "total_items": total_items,
        "status": "Order created successfully"
    }


if __name__ == "__main__":
    my_cart = {}
    cart_related(my_cart, "Burger", 2)
    cart_related(my_cart, "Fries", 1)
    print(place_order(my_cart))
