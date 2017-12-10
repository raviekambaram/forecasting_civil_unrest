import json

for line in open('train_nega_tweets_2017.txt').readlines():
    tweet = json.loads(line)
    with open('traintwt.txt', 'a+') as f:
        json.dump([tweet["embersId"],0,tweet["text"]], f)
        #json.dump("false", f)
        #json.dump(tweet["text"], f)
        f.write('\n')
for line in open('train_posi_tweets_2017.txt').readlines():
    tweet = json.loads(line)
    with open('traintwt.txt', 'a+') as f:
        json.dump([tweet["embersId"],1,tweet["text"]], f)
        #json.dump("false", f)
        #json.dump(tweet["text"], f)
        f.write('\n')
f.close

for line in open('test_tweets.txt').readlines():
    tweet = json.loads(line)
    with open('tsttwt.txt', 'a+') as f:
        json.dump([tweet["embersId"],tweet["text"]], f)
        #json.dump("false", f)
        #json.dump(tweet["text"], f)
        f.write('\n')
f.close