import csv
import re
import sys

import tweepy
from textblob import TextBlob

# Step 1 - Autenticacion con el api de twiter
consumer_key = 'OoKtdnkn2PhPdVopgcPPVszBL'
consumer_secret = 'zJCI08nnQ7wGiosCOe7Udbu4PlpchanXFbjytZZJFkontr2wOC'

access_token = '572213920-pfExxBDxG4W7gu6ke8Yh1xexYcypE9QOddfvpY6u'
access_token_secret = 'C2tOsrGpF48uBoxVjcyHYptljLpfAesln2ABZacpLy1mL'

# Step 2 - pasamos parametros
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Step 3 - los re-twiter buscando
public_tweets = api.search(sys.argv[1])


# Step 4 - Separamos los twiter
def clean_tweet(tweet):
    tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
    return tweet


# Step 5 - Segundo parametros
f = open(sys.argv[2], 'wt')
try:
    # Step 5.0 - guardamos
    writer = csv.writer(f)
    writer.writerow(('Tweet', 'Sentiment'))

    # Step 5.1 - recorremos los tweets
    for tweet in public_tweets:
        cleaned_tweet = clean_tweet(tweet.text)
        _analysis = TextBlob(cleaned_tweet)

        # Step 5.2 - si verifica polaridad
        if (_analysis.sentiment.polarity > 0):
            sentiment = 'POSITIVE'
        elif (_analysis.sentiment.polarity == 0):
            sentiment = 'NEUTRAL'
        else:
            sentiment = 'NEGATIVE'
        writer.writerow((cleaned_tweet, sentiment))

finally:
    f.close()

# Step 5 - fin del documento
print(open(sys.argv[2], 'rt').read())


# EXAMPLE  python demo.py  "palabra_a_buscar" "nombre_archivo.csv"
