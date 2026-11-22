import sys

def product_details(product_id, name, quantity, price):
    return f"Product ID: {product_id}\nProduct Name: {name}\nQuantity: {quantity}\nPrice: {price}"

if __name__ == "__main__":
    product_id = sys.argv[1]
    name = sys.argv[2]
    quantity = sys.argv[3]
    price = sys.argv[4]

    print("\nProduct Details")
    print("----------------")
    print(product_details(product_id, name, quantity, price))