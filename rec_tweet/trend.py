# -*- coding: utf-8 -*- 

from mongoengine import *

class Trend(Document):
    events = ListField()
    name = StringField(required=True, primary_key=True)
    promoted_content = ListField()
    query = StringField(required=True)
    url = StringField(required=True)
    
    def __init__(self, trend):
        super(Trend, self).__init__()
        self.events = trend['events']
        self.name = trend['name'].encode('utf-8', 'xmlcharrefreplace')
        self.promoted_content = trend['promoted_content']
        self.query = trend['query']
        self.url = trend['url']