
from sklearn.linear_model import LogisticRegression
import json
import simplejson
f1 = open('negStopWords.txt', 'r+')
stopwords = [(i) for i in f1.readlines() ]
f1.close()
tweets = []
f = open('traintwt.txt')
for line in f.readlines():
    tweets.append(json.loads(line))
# Extract the vocabulary of keywords
f.close()
vocab = dict()
for tweet_id, class_label, text in tweets:
    for term in text.split():
        term = term.lower()
        if len(term) > 3 and term not in stopwords:
            if vocab.has_key(term):
               vocab[term] = vocab[term] + 1
            else:
                vocab[term] = 1

# Remove terms whose frequencies are less than a threshold (e.g., 20)
vocab = {term: freq for term, freq in vocab.items() if freq > 20}
# Generate an id (starting from 0) for each term in vocab
vocab = {term: idx for idx, (term, freq) in enumerate(vocab.items())}
#print 'The list of keywords that are considered: '
#print vocab

# Generate X and y
X = []
y = []
for tweet_id, class_label, tweet_text in tweets:
    x = [0] * len(vocab)
    terms = [term for term in tweet_text.split() if len(term) > 2]
    for term in terms:
        if vocab.has_key(term):
            x[vocab[term]] += 1
    y.append(class_label)
    X.append(x)

# 10 folder cross validation to estimate the best w and b
clf = LogisticRegression()
clf.fit(X, y)
#print clf.score(X,y)
#scores = cross_validation.cross_val_score(clf,X,y,cv = 10)
#print scores
#print scores.mean()

# predict the class labels of new tweets
tweets = []
ff =open('tsttwt.txt','r+')
for line in ff.readlines():
    tweets.append(json.loads(line))
ff.close
# Generate X for testing tweets
X = []
for tweet_id, tweet_text in tweets:
    x = [0] * len(vocab)
    terms = [term for term in tweet_text.split() if len(term) > 4]
    for term in terms:
        if vocab.has_key(term):
            x[vocab[term]] += 1
    X.append(x)
y = clf.predict(X)
# lr.predict_proba(X) will return you the predict probabilities




f = open('predictions.txt', 'w')
#print tweets
pred_dict={}

for idx, [tweet_id, tweet_text] in enumerate(tweets):
    if y[idx] == 0:
        pre = 'true'
    else:
        pre = 'false'
    pred_dict[tweet_id] = pre
    #pred_dict = {tweet_id.encode('utf-8'),pre}
    #pred_dict = pre


    #pred_dict.append(tweet_id.encode('utf-8'),pre.encode('utf-8'))

    #f.write('\n')

json.dump(pred_dict, f)
#simplejson.dumps(pred_dict,f)
f.close()


#print '\r\nAmong the total {1} tweets, {0} tweets are predicted as positive.'.format(sum(y), len(y))
