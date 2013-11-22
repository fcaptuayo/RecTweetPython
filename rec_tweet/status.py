# -*- coding: utf-8 -*- 

from trend import Trend
from mongoengine import *

class Status(Document):
    """docstring for Status"""

    contributors = DictField()
    truncated = BooleanField()
    text = StringField(required=True)
    in_reply_to_status_id = IntField()
    favorite_count = IntField()
    source = StringField()
    retweeted = BooleanField()
    coordinate = DictField()
    entities = DictField()
    in_reply_to_screen_name = StringField()
    in_reply_to_user_id = IntField()
    retweet_count = IntField()
    id_str = StringField(primary_key=True)
    favorited = BooleanField()
    user = DictField()
    geo = DictField()
    in_reply_to_user_id_str = StringField()
    in_reply_to_status_id_str = StringField()
    lang = StringField()
    created_at = StringField()
    metadata = DictField()
    place = DictField()
    trend = ReferenceField(Trend, reverse_delete_rule=CASCADE)


    def __init__(self, status, trend):
        super(Status, self).__init__()
        self.contributors = status['contributors']
        self.truncated = status['truncated']
        self.text = status['text']
        self.in_reply_to_status_id = status['in_reply_to_status_id']
        self.favorite_count = status['favorite_count']
        self.source = status['source']
        self.retweeted = status['retweeted']
        self.coordinate = status['coordinates']
        self.entities = status['entities']
        self.in_reply_to_screen_name = status['in_reply_to_screen_name']
        self.in_reply_to_user_id = status['in_reply_to_user_id']
        self.retweet_count = status['retweet_count']
        self.id_str = status['id_str']
        self.favorited = status['favorited']
        self.user = status['user']
        self.geo = status['geo']
        self.in_reply_to_user_id_str = status['in_reply_to_user_id_str']        
        self.in_reply_to_status_id_str = status['in_reply_to_status_id_str']
        self.lang = status['lang']
        self.created_at = status['created_at']
        self.metadata = status['metadata']
        self.place = status['place']
        self.trend = trend