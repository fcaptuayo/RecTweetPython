# -*- coding: utf-8 -*- 

import time
from twython import Twython, TwythonError
from trend import Trend
from status import Status
from mongoengine import connect

connect('twitter')
twitter = Twython("", "", "", "")

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

starting_point = time.time()
elapsed_time = 0 
elapsed_time_int = 0
trends = {}
while (True):
    if(elapsed_time_int == 1):
        try:
            search_results = twitter.get_place_trends(id = 23424787)
        except TwythonError as e:
            print e

        if search_results:
            previous_trends = trends.copy()
            trends.clear()
            for trend in search_results[0].get('trends', []):       
                t = Trend(trend)       
                trends[t.name] = t    
                search_tweets(t)     
                if(previous_trends.get(t.name)):
                    del trends[t.name]
                t.save()                        
                print t.name
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