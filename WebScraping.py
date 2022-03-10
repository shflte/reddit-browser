import requests
import re

def getTrendingSubreddits():
    #get the html
    url = "https://www.reddit.com/subreddits/leaderboard/"
    html = requests.get(url).text

    with open("html.txt", "w", encoding="utf-8") as f:
        f.write(html)

    #return a list of trending subreddits
    result = re.findall("href=\"/r/(.+?)/\"", html)
    return result
