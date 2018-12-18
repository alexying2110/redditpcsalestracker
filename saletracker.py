import praw
from win10toast import ToastNotifier


def main():
    notification = ToastNotifier()
    
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
                      password=passWord,
                      client_id = "",
                      client_secret = "")

    sub = bot.subreddit('buildapcsales')
    
    print(keyWords)
    #set skip_existing to True to only notify user about new posts
    for submission in sub.stream.submissions(skip_existing=False):
        title = submission.title
        for key in keyWords:
            if key.lower() in title.lower():
                print(title)
                notification.show_toast(title, key.lower())

if __name__ == '__main__':
    main()
