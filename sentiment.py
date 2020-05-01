import tweepy
import csv
import pandas as pd
import re
from textblob import TextBlob
#from textblob import Word
#from textblob.classifiers import NaiveBayesClassifier
from textblob_analysis import cl
consumer_key = 'fM9sSIoN9oTuC65TQTA42AcGh'
consumer_secret = 'LeSnaQFeoHeCE8LqCHqDqeSyL6ZVSHz946NzwFpgB4qypTuodr'
access_token = '625427849-XFSWT7dRokATsiiuHGHMwigYurnm2hDMTi6FFXye'
access_token_secret = 'V5Nt3hnmIuVTZWMEKKS1jHZFDIe2LV0SZDyeJuWVPKpBC'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


def pre_process(tweets):
    tweets = tweets.lower()  # convert text to lower-case
    tweets = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','', tweets)  # remove URLs
    tweets = re.sub('@[^\s]+','', tweets)  # remove usernames
    tweets = re.sub(r'#([^\s]+)', r'\1', tweets)# remove the # in #hashtag
    return tweets

# Open/Create a file to append data
#Use csv Writer










string1="('"
string2="',"
string3="),"


def fetch_new_tweets():
    ticker = input("enter sen stock ticker")
    file_name = ticker + "_sentiment.csv"
    csvFile = open(file_name, 'a')
    csvWriter = csv.writer(csvFile)
    q = input("enter stock keyword:")
    count = 1
    print("=================================================")
    print(" Fetching new tweets ")
    print("=================================================")
    for tweet in tweepy.Cursor(api.search,q,count=100,lang="en",since="2020-04-10",tweet_mode='extended').items(10000):
        temp=tweet.full_text
        temp=pre_process(temp)
        blob=TextBlob(temp)
        sentiment=blob.sentiment.polarity
        subjectivity=blob.sentiment.subjectivity
        classification=cl.classify(temp)
        if(blob.sentiment.subjectivity>0 and blob.sentiment.polarity!=0):
        #print(count,": "+string1+temp+string2+"sentiment"+string3)
            print(count, ": " + temp +"sentiment: ",cl.classify(temp))
            count=count+1
            #csvWriter.writerow([count,tweet.id,tweet.full_text.encode('utf-8'),sentiment,subjectivity,classification])
            csvWriter.writerow([count,tweet.id, tweet.full_text.encode('utf-8'),classification])


fetch_new_tweets()







