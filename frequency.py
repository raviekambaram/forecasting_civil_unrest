import sys
import string
import json


# Parse tweets to Json and returns a list of text content
def load_tweets(fn):
    # Load tweets
    tweets_file = open(fn)
    tweets = []

    for tweet in tweets_file:
        # Parse input strings as Json
        json_tweet = json.loads(tweet)
        # Check that there is a text field
        if "text" in json_tweet.keys():
            text = json_tweet["text"].encode('utf-8')
            tweets.append(text)
    return tweets


# Builds a list of whitespace delimited tokens from a list of strings.
def extract_terms(words):
    terms_unique = []
    # Get non-unique terms.
    terms_non_unique = words.split()
    for term in terms_non_unique:
        if term not in terms_unique: terms_unique.append(term)
    return terms_unique


# Calculates the histogram values for terms in a series of tweets.
def cal_freq(terms, words,fname):
    # Calculate number of terms in all tweets.
    terms_total = len(words.split())
    word =[]
    # Count all occurrences
    with open(fname, 'w+') as outfile:
        for term in terms:
            word = ''.join(e for e in term if e.isalnum())
            #print word
            count = words.count(word)
            if len(word) > 6 and count > 75:
                outfile.write(word+'\n')


def main():
    # load the tweets file
    input_file = 'train_posi_tweets_2017.txt'
    fname = 'posStopWords.txt'
    # get the list of tweets
    tweets = load_tweets(input_file)
    # merge the tweets into a string
    tweets_join = ' '.join(tweets)
    # get a list of terms
    terms = extract_terms(tweets_join)
    # calculate list of frequencies
    cal_freq(terms, tweets_join,fname)

    input_file = 'train_nega_tweets_2017.txt'
    fname = 'negStopWords.txt'
    # get the list of tweets
    tweets = load_tweets(input_file)
    # merge the tweets into a string
    tweets_join = ' '.join(tweets)
    # get a list of terms
    terms = extract_terms(tweets_join)
    # calculate list of frequencies
    cal_freq(terms, tweets_join, fname)

if __name__ == '__main__':
    main()