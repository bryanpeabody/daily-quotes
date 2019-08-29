import sys
import tweepy
import random

def post_to_twitter():
    #
    # Setup the Twitter API tokens
    #
    consumer_key = sys.argv[1]
    consumer_secret = sys.argv[2]

    access_token = sys.argv[3]
    access_token_secret = sys.argv[4]

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #
    # Read in the quotes file
    #
    with open("./quotes.txt") as f:
        content = f.readlines()

    content = [x.strip() for x in content]

    #
    # Pick a random number from max length of quotes file
    #
    length = len(content)
    idx = random.randint(0,length-1)

    #
    # Post to Twitter
    #
    thequote = content[idx]

    if len(thequote) > 0:
        api = tweepy.API(auth)
        api.update_status(thequote)

if __name__ == "__main__":
    # 0 is file name, then param1, param2 ...
    if len(sys.argv) != 5:
        print("Please pass in consumer key, consumer secret, access token and access token secret.")
        exit()

    # Parameters were good, post to twitter
    post_to_twitter()