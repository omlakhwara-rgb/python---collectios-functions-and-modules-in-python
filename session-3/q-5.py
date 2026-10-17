"""
Q -5. Build a function that takes two lists, one of YouTube video titles and one of their view counts, and returns a list of tuples with each title and its rounded view count (to the nearest thousand using round()).<br><br><em><strong>Hint:</strong> Use zip() to pair titles and counts, and round() inside a list comprehension.</em>
"""


def pair_videos_with_views(titles, views):
    
    return [(title, round(view, -3)) for title, view in zip(titles, views)]


video_titles = ["Python Tutorial", "SQL Basics", "VS Code Setup", "AI Trends"]
view_counts = [15234, 98765, 4567, 120345]

result = pair_videos_with_views(video_titles, view_counts)

print("Video views (rounded):")
for title, views in result:
    print(f"{title} - {views} views")
