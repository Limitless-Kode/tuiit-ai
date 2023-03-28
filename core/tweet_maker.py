from core.openai import OpenAI
from core.google_sheet import GoogleSheet

class TweetMaker:
    def __init__(self, generator: OpenAI, sheet: GoogleSheet):
      self.openAi = generator;
      self.sheet = sheet;

    def makeTweets(self, limit=1):

      tweets = []
      # get first 10 topics from sheet
      topics = self.sheet.get_col(1)[1:limit+1]

      # get first 10 interests from sheet
      interests = self.sheet.get_col(2)[1:limit+1]

      # get first 10 prompts from sheet
      prompts = self.sheet.get_col(3)[1:limit+1]

      # for each topic, interest and prompt
      for topic in topics:
        # generate a tweet
        tweet = self.openAi.get_completion(f'Write a twitter post for the topic {topic}')
        # add it to the list of tweets
        tweets.append(tweet)

      # return the list of tweets
      return tweets
