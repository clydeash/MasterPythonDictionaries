product_object1 = {
    "name": "Laptop",
    "price": 1000
}
product_object2 = {
    "name": "Keyboard",
    "price": 50
}
product_object3 = {
    "name": "Mouse",
    "price": 25
}
product_object4 = {
    "name": "Monitor",
    "price": 200
}
product_object5 = {
    "name": "Webcam",
    "price": 50
}

products = [product_object1, product_object2, product_object3, product_object4, product_object5]

for product in products:
    print(f"Product Name: {product['name']}, Price: {product['price']}")
