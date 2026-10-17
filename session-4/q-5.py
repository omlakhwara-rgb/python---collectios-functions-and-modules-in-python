"""
Q -5.Take a tuple of your last 7 WhatsApp call durations in minutes (e.g., (12, 5, 0, 20, 7, 3, 15)), convert it to a list, remove all calls shorter than 5 minutes, then convert it back to a tuple and print the result.<br><br><em><strong>Hint:</strong> Use a for loop or list comprehension to filter the list before converting back to tuple.</em>
"""

call_durations = (12, 5, 0, 20, 7, 3, 15)

durations_list = list(call_durations)
filtered_list = [d for d in durations_list if d >= 5]
final_tuple = tuple(filtered_list)

print(final_tuple)
