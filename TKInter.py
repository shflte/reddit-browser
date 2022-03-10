import tkinter as tk

#create the tkinter object
def CreateAWindow(size):
    window = tk.Tk()
    window.title("COOL Reddit Browser")
    window.geometry(size)

    return window

import Reddit
from tkinter.messagebox import showinfo
onhit = False
subr = "default"
def pickTrendingSubreddits(reddit, window, subr_list):
    topic = "Select the subreddit: "
    lable_topic = tk.Label(window, text=topic, font= ('Arial', 12), width=30, height=2)
    lable_topic.grid(row=0, padx=10)

    def openSubr(theSubr):
        global onhit, subr
        onhit = True
        subr = theSubr
        window.destroy()
    #Create the buttons
    button_list = []
    for i in range(0, len(subr_list)):
        button_list.append(tk.Button(window, text=subr_list[i], command=lambda c=i: openSubr(button_list[c].cget("text"))))
        button_list[i].grid(row=(i + 1), padx=10)

    #Enter the subreddit's name that is not on the window
    def getSubrFromEntry():
        another_subr = entry_another_subr.get()
        if another_subr == "":
            errorMessage = "No input"
            showinfo(title='Error', message=errorMessage)
        elif not Reddit.sub_exists(reddit, another_subr):
            errorMessage = another_subr + " doesn't exist."
            showinfo(title='Error', message=errorMessage)
        else: 
            global subr, onhit
            onhit = True
            subr = another_subr
            window.destroy()
    entry_another_subr = tk.Entry(window, show=None, font=('Arial', 14))
    entry_another_subr.grid(column=1, row=len(subr_list) + 2, padx=10)
    button_another_subr = tk.Button(window, text='Other subreddit: ', command=getSubrFromEntry)
    button_another_subr.grid(column=0, row=len(subr_list) + 2, padx=10)

    def exit():
        global onhit, subr
        onhit = True
        subr = 3
        window.destroy()
    button_exit = tk.Button(window, text='exit', command=exit)
    button_exit.grid(column=1, row=0)

    window.mainloop()

    #return the subreddit's name and shut the window
    #(the subreddit has been verified exists)
    global onhit
    if onhit:
        onhit = False
        return subr

post_name = "default"
def pickTrendingPost(window, trendingPostDict, subr_name):
    lable_topic = tk.Label(window, text=subr_name, font= ('Arial', 12), width=70, height=2)
    lable_topic.grid(row=0, padx=10)

    text = "Select the Post: "
    lable_text = tk.Label(window, text=text, font= ('Arial', 12), width=30, height=2)
    lable_text.grid(row=1, padx=10)

    def openPost(thePost):
        global onhit, post_name
        onhit = True
        post_name = thePost 
        window.destroy()
    #Create the buttons
    button_list = []
    trendingPostList = list(trendingPostDict.keys())
    for i in range(0, len(trendingPostList) - 1):
        button_list.append(tk.Button(window, text=trendingPostList[i], command=lambda c=i: openPost(button_list[c].cget("text"))))
        button_list[i].grid(row=(i + 2), padx=10)
    
    def back():
        global onhit, post_name
        onhit = True
        post_name = 0
        window.destroy()
    button_back = tk.Button(window, text='Back', command=back)
    button_back.grid(column=1, row=len(trendingPostList) + 0, padx=10)

    def exit():
        global onhit, post_name
        onhit = True
        post_name = 3
        window.destroy()
    button_exit = tk.Button(window, text='exit', command=exit)
    button_exit.grid(column=1, row=1)

    window.mainloop()

    #return the post's name
    global onhit
    if onhit:
        onhit = False
        return post_name

import GoogleTrans
signal = -1
def showText(selftext, post_name, window, dest):
    post_name = str(GoogleTrans.translate(post_name, "en", dest))
    lable_topic = tk.Label(window, text=post_name, font= ('Arial', 12), width=70, height=2)
    lable_topic.grid(row=1, padx=10)

    selftext = str(GoogleTrans.translate(selftext, "en", dest))
    lable_selftext = tk.Label(window, text=selftext, font= ('Arial', 12), width=90, height=15, padx=10)
    lable_selftext.grid(row=2, padx=10)

    def back():
        global signal
        signal = 0
        window.destroy()
    button_back = tk.Button(window, text='Back', command=back)
    button_back.grid(column=0, row=0)

    def exit():
        global signal
        signal = 3
        window.destroy()
    button_exit = tk.Button(window, text='exit', command=exit)
    button_exit.grid(column=1, row=0)

    def en():
        global signal
        signal = 4
        window.destroy()
    button_english = tk.Button(window, text='english', command=en)
    button_english.grid(column=1, row=1)
    def tw():
        global signal
        signal = 5
        window.destroy()
    button_chinese = tk.Button(window, text='chinese', command=tw)
    button_chinese.grid(column=1, row=2)
    def ko():
        global signal
        signal = 6
        window.destroy()
    button_korean = tk.Button(window, text='korean', command=ko)
    button_korean.grid(column=1, row=3)
    def ja():
        global signal
        signal = 7
        window.destroy()
    button_japanese = tk.Button(window, text='japanese', command=ja)
    button_japanese.grid(column=1, row=4)

    window.mainloop()

    return signal