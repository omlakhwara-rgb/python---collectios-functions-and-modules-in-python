"""
Q- 3.Simulate a Flipkart shopping cart: prices = [299, 499, 150, 1200, 350]. Use a for loop to calculate and print the total cart value.
"""

prices = [299, 499, 150, 1200, 350]

total = 0

for i in range(len(prices)):
    total += prices[i] 

print("Total cart value =", total)