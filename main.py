import GoogleTrans
import TKInter
import Reddit
import WebScraping

hierarchy = 1
while hierarchy:
    reddit = Reddit.getReddit()
    subr_list = WebScraping.getTrendingSubreddits()
    if hierarchy == 1:
        #initialize
        subr_name = -1
        size = "500x1000"
        window = TKInter.CreateAWindow(size)
        subr_name = TKInter.pickTrendingSubreddits(reddit, window, subr_list)
        if subr_name == 3:
            hierarchy = 0
            continue
        else:
            hierarchy = 2
            continue
    elif hierarchy == 2:
        #initialize
        post_name = -1
        size = "900x500"
        window = TKInter.CreateAWindow(size)

        subreddit = Reddit.getSubreddit(reddit, subr_name)
        trendingPostDict = Reddit.getHotPosts(subreddit)
        post_name = TKInter.pickTrendingPost(window, trendingPostDict, subr_name)
        if post_name == 0:
            hierarchy = 1
            continue
        elif post_name == 3:
            hierarchy = 0
            continue
        else:
            hierarchy = 3
            continue
    elif hierarchy == 3:
        #initialize
        signal = -1
        src = "en"
        dest = "en"
        while (hierarchy != 0 and hierarchy != 2):
            size = "1200x400"
            window = TKInter.CreateAWindow(size)
            selftext = trendingPostDict[post_name]
            signal = TKInter.showText(selftext, post_name, window, dest)
            if signal == 0:
                hierarchy = 2
                continue
            elif signal == 3:
                hierarchy = 0
                continue
            elif signal == 4:
                dest = "en"
                continue
            elif signal == 5:
                dest = "zh-tw"
                continue
            elif signal == 6:
                dest = "ko"
                continue
            elif signal == 7:
                dest = "ja"
                continue
