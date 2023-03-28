from core.openai import OpenAI
from core.twitter import Twitter
from core.tweet_maker import TweetMaker
from core.google_sheet import GoogleSheet

def boot():
  # Load topics, inter.., prompts from google sheet
  topicsInterestsAndPromptsSheet = GoogleSheet('topics, interests and prompts')
  print(topicsInterestsAndPromptsSheet)
  
  # Using TweetMaker to generate/make tweets
  tweetMaker = TweetMaker(OpenAI(), topicsInterestsAndPromptsSheet)
  tweets = tweetMaker.makeTweets()
  print(tweets)

  twitter = Twitter()
  twitter.post_tweet(tweets[0].text)
  # twitter.post_tweet('Hello, this is an example tweet`` from a twitter bot')

if __name__ == '__main__':
  boot()