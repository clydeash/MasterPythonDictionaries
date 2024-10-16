restaurant_object1 = {
    "name": "The Cheesecake Factory",
    "cuisine_type": "American"
}
restaurant_object2 = {
    "name": "Nobu",
    "cuisine_type": "Japanese"
}
restaurant_object3 = {
    "name": "Olive Garden",
    "cuisine_type": "Italian"
}
restaurant_object4 = {
    "name": "Red Lobster",
    "cuisine_type": "Seafood"
}
restaurant_object5 = {
    "name": "In-N-Out Burger",
    "cuisine_type": "Fast Food"
}

restaurants = [restaurant_object1, restaurant_object2, restaurant_object3, restaurant_object4, restaurant_object5]

for restaurant in restaurants:
    print(f"Restaurant Name: {restaurant['name']}, Cuisine Type: {restaurant['cuisine_type']}")