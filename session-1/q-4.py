"""
Q- 4. Create a new list called weekend_plan with at least 5 items representing things you want to do this weekend (mix of strings and numbers). Remove the last item using the pop() method and display the removed item and the updated list.
"""

weekend_plan = ["Play Cricket","Going to a Temple",1,"Watch a Movie","Night out with Friends"]

remove_item = weekend_plan.pop()

print("Removed Item: ", remove_item)
print("Updated List: ", weekend_plan)