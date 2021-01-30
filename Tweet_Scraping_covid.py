#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 17:22:56 2021

@author: zake
"""

import tweepy
import sys

class MystreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)
        
    def on_error(self, status_code):
        print(status_code)
        



consumer_key = "????"
consumer_secret = "???"
acces_token = "???"
access_token_secret = "???"








auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acces_token, access_token_secret)
api = tweepy.API(auth)

if (not api):
    print("Authentication failed")
    sys.exit(-1)
    
MyStreamListener = MystreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = MyStreamListener)
myStream.filter(track=['covid'])



    