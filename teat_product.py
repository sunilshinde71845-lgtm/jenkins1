from product import product_details

def test_product_details():
    result = product_details("P101", "Laptop", "2", "50000")

    expected = "Product ID: P101\nProduct Name: Laptop\nQuantity: 2\nPrice: 50000"

    assert result == expected