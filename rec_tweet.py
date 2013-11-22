import time
from twython import Twython, TwythonError
from trend import Trend
from status import Status
from mongoengine import connect

connect('twitter')
twitter = Twython("iDGDpOTDVj7mwGDD4pkAMw", "rKOrMHCvsP98lISbyXnHPaR7HFWj44PsAa4Yy7cCQvE", 
    "222814276-KsT3JiNkqUCALLKrfFegVenxi229thKKxjkM2Zpr", "soCtSgfJyzuAEhXvN466LZao7Xc5RcenjFbTmd1TA")

def search_tweets(trend):
    try:
        search_results = twitter.search(q=trend.query,  lang='es', count='100')
    except TwythonError as e:
        print e
    aux = 0
    for status in search_results.get(u'statuses', []):
        s = Status(status, trend)
        print s.text
        s.save()

def get_place_trends(woeid):
    try:
        search_results = twitter.get_place_trends(id = woeid)
    except TwythonError as e:
        print e

    if search_results:
        previous_trends = trends.copy()
        trends.clear()
        for trend in search_results[0].get('trends', []):       
            t = Trend(trend)       
            trends[t.name] = t    
            search_tweets(t)     
            t.save()                        
            print t.name

starting_point = time.time()
elapsed_time = 0 
elapsed_time_int = 0
trends = {}
while (True):
    if(elapsed_time_int == 1):
        get_place_trends(23424787)
        print "El valor de elapsed_time_int es " + str(elapsed_time_int)
        starting_point = time.time()
        elapsed_time_int = 0
        print trends
        break
        print "El nuevo valor de elapsed_time_int es " + str(elapsed_time_int)
    else:
        elapsed_time = time.time() - starting_point
        elapsed_time_int = int(elapsed_time)
        print elapsed_time_int