"""
Q- 3.Suppose you have two lists: one with IPL team names and another with their total points this season. Use zip() to combine them into a dictionary, then print only the teams that have more than 10 points.<br><br><em><strong>Hint:</strong> After creating the dictionary, use a for loop to filter and print.</em>
"""

teams = ["CSK", "MI", "GT", "RCB"]
points = [12, 8, 15, 9]

ipl_dict = dict(zip(teams, points))

for team, pts in ipl_dict.items():
    if pts > 10:
        print(team, "-", pts)
