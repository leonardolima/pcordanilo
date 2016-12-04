from random import randint
from time import sleep
import tweepy
import config

def get_tweets(name, api):
    lst = []
    statuses = api.user_timeline(id = name, count = 500, include_rts = False)
    
    for status in statuses:
        status_encoded = status.text.encode('utf-8')
        if 't.co' not in status_encoded and '@' not in status_encoded:
            lst.append(status_encoded)

    return lst

def save_tweet(tweet):
    txt_file = open("mytweets.txt", "w")
    txt_file.write("%s" % tweet)
    txt_file.close()

def read_tweets():
    lst = []

    with open('mytweets.txt') as f:
        for line in f:
            lst.append(line)
            if 'str' in line:
                break

    return lst

def get_random_tweet(fst_lst, snd_lst):
    old_tweets = read_tweets()

    while True:
        fst_tweet = fst_lst[randint(0,len(fst_lst))]
        snd_tweet = snd_lst[randint(0,len(snd_lst))]

        if fst_tweet in old_tweets or snd_tweet in old_tweets:
            fst_tweet = fst_lst[randint(0,len(fst_lst))]
            snd_tweet = snd_lst[randint(0,len(snd_lst))]

        else:
            break

    decides = randint(0,1)
    if decides == 0:
        return fst_tweet
    else:
        return snd_tweet

def main():

    auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN_KEY, config.ACCESS_TOKEN_SECRET)
    
    api = tweepy.API(auth)

    while True:
        fst_lst = [] # pecesiqueira tweets
        snd_lst = [] # danilo tweets
        
        fst_lst = get_tweets('pecesiqueira', api)
        snd_lst = get_tweets('danilordgss', api)
        
        tweet = get_random_tweet(fst_lst, snd_lst)
        api.update_status(tweet)
        save_tweet(tweet)
        sleep(21600)

if __name__ == "__main__":
    main()
