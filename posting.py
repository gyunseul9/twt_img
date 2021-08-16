# -*- coding: utf-8 -*-

import os
import re
import time
import tweepy
import requests
import configparser
from bs4 import BeautifulSoup
from datetime import datetime

CNF_INI = '/home/ubuntu/twt_img/config.ini'
ERR_URI = '/home/ubuntu/twt_img/'

config = configparser.ConfigParser()
config.read(CNF_INI)
CKEY = config['twitter@lonbekim']['consumer_key']
CSECRET = config['twitter@lonbekim']['consumer_secret']
ATOKEN = config['twitter@lonbekim']['access_token']
ASECRET = config['twitter@lonbekim']['access_secret']

def send_twitter():
  
  message = '@lonbekim\n#앤비팁스\n#케이브업\n'

  auth = tweepy.OAuthHandler(CKEY, CSECRET)
  auth.set_access_token(ATOKEN, ASECRET)

  api = tweepy.API(auth)
  #api.update_status(message)

  photo = '/home/ubuntu/twt_image/caveup1.jpg'

  api.update_with_media(status=message, filename=photo)

try:
  send_twitter()
except Exception as e:
  with open(ERR_URI+'error.log','a') as file:
    file.write('{} You got an error: {}\n'.format(datetime.today().strftime('%Y-%m-%d %H:%M:%S'),str(e)))

