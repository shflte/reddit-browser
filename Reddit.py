import praw

#OAuth 
#send id, secret to the authentication server and get the token.
def getReddit():
    clientId = "7ejjrOE6_uF76g"
    clientSecret="GAn6IXyVkW-BlXr3uVpboDUB-9qisw"
    userAgent="used for SH's final project"

    reddit = praw.Reddit(client_id=clientId,
                        client_secret=clientSecret,
                        user_agent=userAgent)
    return reddit
    #return a reddit object if the info. work, return None if some info. be provided wrongly

#make request to API server with the token
def getSubreddit(reddit, subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    return subreddit

#return a title-selftext dictionary
def getHotPosts(subreddit):
    PostList = []
    for post in subreddit.hot(limit=10):
        PostList.append(post)
    
    t_s_dict = dict()
    for post in PostList:
        t_s_dict[post.title] = post.selftext

    return t_s_dict

from prawcore import NotFound

#check if the subreddit exist
def sub_exists(reddit, subr_name):
    exists = True
    try:
        reddit.subreddits.search_by_name(subr_name, exact=True)
    except NotFound:
        exists = False
    return exists