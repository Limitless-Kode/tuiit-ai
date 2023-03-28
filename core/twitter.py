import tweepy
from decouple import config

class Twitter:
    def __init__(self, consumer_key=config('TWITTER_API_KEY'), consumer_secret=config('TWITTER_API_SECRET'), access_token=config('TWITTER_ACCESS_TOKEN'), access_token_secret=config('TWITTER_ACCESS_TOKEN_SECRET')):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
    
    def get_api(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        return tweepy.API(auth)
    
    def get_tweets(self, query, max_tweets=1000, lang='en'):
        api = self.get_api()
        tweets = []
        for tweet in tweepy.Cursor(api.search_tweets, q=query, lang=lang).items(max_tweets):
            tweets.append(tweet)
        return tweets
    
    def get_tweets_by_user(self, api, user, max_tweets=1000):
        tweets = []
        for tweet in tweepy.Cursor(api.user_timeline, id=user).items(max_tweets):
            tweets.append(tweet)
        return tweets

    def post_tweet(self, tweet):
        api = self.get_api()
        api.update_status(tweet)