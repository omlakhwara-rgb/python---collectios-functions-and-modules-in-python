"""
Q- 4.Given the following nested dictionary representing an IPL cricket team squad:<br><br>team = {'CSK': {'captain': 'Dhoni', 'players': 18}, 'MI': {'captain': 'Rohit', 'players': 17}}<br><br>Write code to add a new team 'GT' with captain 'Hardik' and 16 players, then print all team names and their captains.
"""

team = {
    'CSK': {'captain': 'Dhoni', 'players': 18},
    'MI': {'captain': 'Rohit', 'players': 17}
}

team['GT'] = {'captain': 'Hardik', 'players': 16}

for name, info in team.items():
    print(name, "-", info['captain'])
