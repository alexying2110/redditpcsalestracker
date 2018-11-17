import praw
import win32api


def main():
    keyWords = []
    keyWord = input("Enter keyword (type q to stop): ")

    while(keyWord != 'q'):
        keyWords.append(keyWord)
        keyWord = input("Enter keyword (type q to stop): ")

    #Users logs in because I don't feel like making a new account for myself
    userName = input("Enter Reddit username: ")
    passWord = input("Enter Reddit password: ")
    #praw OAuth
    bot = praw.Reddit(user_agent="salestracker",
                      username=userName,
                      password=passWord)

    sub = bot.subreddit('buildapcsales')

    print(keyWords)
    #set skip_existing to True to only notify user about new posts
    for submission in sub.stream.submissions(skip_existing=False):
        title = submission.title
        for key in keyWords:
            if key.lower() in title.lower():
                notify_user(title)

#plays a stupid little tune, there are probably better ways to do this but i already had this package
#installed anyways
def notify_user(title):
    win32api.Beep(440, 250)
    win32api.Beep(880, 125)
    win32api.Beep(440, 125)
    win32api.Beep(880, 125)
    win32api.Beep(440, 125)
    win32api.Beep(220, 250)
    print(title)


if __name__ == '__main__':
    main()
