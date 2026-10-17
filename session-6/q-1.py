"""
Q- 1.Given two lists — one of product names and one of their prices — use the zip() function to create a dictionary mapping each product to its price, then print the dictionary.
"""

products = ["Shoes", "Mobile", "Laptop"]
prices = [2000, 15000, 50000]

playlist = dict(zip(products, prices))

print(playlist)
