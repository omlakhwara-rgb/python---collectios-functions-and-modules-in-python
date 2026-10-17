"""
Q- 1. Create a Python list called playlist containing five of your favorite song names, then use a for loop to print each song with its position in the playlist (starting from 1).
"""

playlist = ["Tum Hi Ho","Tera Ban Jaunga","Kal Ho Naa Ho ","Kabira","Channa Mereya"]

for i in range(len(playlist)):
    print(f"{i+1}. {playlist[i]}")