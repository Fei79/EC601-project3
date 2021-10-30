import tweepy
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"C:\Users\12691\Desktop"
from google.cloud import language

consumer_key = "H1twF5WRZHGoFGM2XaeQAHnvp"
consumer_secret = "mFn5Kx1eHUbKjmcNxkL3ygCvGSUe310oNjmvlPhm3EzHE8Ol3C"
access_token = "1442149855195852808-6J92gIbJY72UvceHuqCTx6YriPqQ5H"
access_token_secret = "l1sFRIPsmPCnXguH1LtWuhxljNeOq96HzIThjOfoSAabA"

def authentication(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

print("The movie or show you want to watch: ", end=" ")
keyword=input()

total_tweets=10
def search_tweets(keyword,total_tweets):
    api = authentication(consumer_key, consumer_secret, access_token, access_token_secret)
    search_result = tweepy.Cursor(api.search_full_archive,
                                  label='search', query=keyword).items(total_tweets)
    for tweet in search_result:
        return tweet.text

client = language.LanguageServiceClient()
type_=language.Document.Type.PLAIN_TEXT
encoding_type=language.EncodingType.UTF32
document = {"content":search_tweets(keyword,total_tweets),"type_":type_}
response = client.analyze_sentiment(request={"document":document, "encoding_type":encoding_type})
sentiment = response.document_sentiment

def content_status():
    if sentiment.score <= -0.25:
        status = 'Negative'
    elif sentiment.score <= 0.25:
        status = 'Neutral'
    else:
        status = 'Positive'
    return status

print(search_tweets(keyword,total_tweets))
print("Sentiment score is: ", end= " ")
print(sentiment.score)
print("Sentiment magnitude is: ", end=" ")
print(sentiment.magnitude)
print("Sentiment status is: ", end=" ")
print(content_status())
