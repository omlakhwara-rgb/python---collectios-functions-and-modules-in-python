"""
Q- 1. Given a list of cricket scores: [56.7, 102.3, 88.9, 45.2, 120.8], use the round() function to create a new list with each score rounded to the nearest integer and print both the original and rounded lists.
"""

cricket_scores = [56.7, 102.3, 88.9, 45.2, 120.8]

score_rounded = [round(score) for score in cricket_scores]


print ("Original Score: ",cricket_scores)
print("Rounded Score : ", score_rounded)
