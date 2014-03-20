# -*- coding: utf-8 -*- 
#Alcamena 10 tendencias en la base de datos.#    
from twython import Twython, TwythonError
from trend import Trend
from mongoengine import connect
connect('twitter')
twitter = Twython("iDGDpOTDVj7mwGDD4pkAMw", "rKOrMHCvsP98lISbyXnHPaR7HFWj44PsAa4Yy7cCQvE", 
    "222814276-KsT3JiNkqUCALLKrfFegVenxi229thKKxjkM2Zpr", "soCtSgfJyzuAEhXvN466LZao7Xc5RcenjFbTmd1TA")

try:
    search_results = twitter.get_place_trends(id = 23424787)
    for trend in search_results[0].get('trends', []):       
        t = Trend(trend)       
        t.save()   
except TwythonError as e:
    print e
