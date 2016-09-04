#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
import time

from markovbot import MarkovBot

tweetbot = MarkovBot()

dirname = os.path.dirname(os.path.abspath(__file__))
book = os.path.join(dirname, u'politicaBrasileira.txt')
tweetbot.read(book)

my_first_text = tweetbot.generate_text(30)

print(u'\ntweetbot says: "%s"' % (my_first_text))

# Consumer Key (API Key)
cons_key = '1rVz2u5o37F6ycuQiXqYpmvz7'
# Consumer Secret (API Secret)
cons_secret = 'r1z2vJLwUExkWDm0vgVKgUYLT5cB5jRcUQDxizbBp6jIYGv4Op'
# Access Token
access_token = '772074137258954752-g9yoZSIRVmhA9EQmyAfDAx5Hfef1G7w'
# Access Token Secret
access_token_secret = 'sqkQRyOWKSXXSxZHqVWwKZZoJpXHnLar7nlT2z1O1ot8Z'

# Log in to Twitter
tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)

targetstring = 'professorpolitica'

keywords = ['política', 'educação', 'saúde', 'pobreza', 'eleições']

prefix = None
suffix = None
maxconvdepth = None

tweetbot.twitter_autoreply_start(targetstring, keywords=keywords, prefix=prefix, suffix=suffix, maxconvdepth=maxconvdepth)
tweetbot.twitter_tweeting_start(days=0, hours=0, minutes=1, keywords=None, prefix=None, suffix='#hackathonSprinklr #politica #imparcialidade')

secsinweek = 7 * 24 * 60 * 60
time.sleep(secsinweek)

tweetbot.twitter_autoreply_stop()

tweetbot.twitter_tweeting_stop()
