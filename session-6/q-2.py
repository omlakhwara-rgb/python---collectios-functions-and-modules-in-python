"""
Q- 2.Write a loop that takes two lists: usernames and their follower counts, and manually creates a dictionary (without using zip()) that maps each username to its follower count, similar to how Instagram tracks followers.
"""

usernames = ["raj_07", "ananya_xo", "om_coder"]
followers = [120, 500, 300]

insta_dict = {}

for i in range(len(usernames)):
    insta_dict[usernames[i]] = followers[i]

print(insta_dict)
