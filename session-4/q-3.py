"""
Q- 3. Convert the tuple order = ('Burger', 'Fries', 'Coke') into a list, add 'Ice Cream' to the end, then convert it back to a tuple and print the final tuple.
"""
t1 = ('Burger', 'Fries', 'Coke')

order_list = list(t1)
order_list.append('Ice Cream')
t1 = tuple(order_list)

print(t1)
