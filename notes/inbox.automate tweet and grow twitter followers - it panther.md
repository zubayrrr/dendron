---
id: k4jhs7x3d9s341iavf0w043
title: Automate Tweet and Grow Twitter Followers   It Panther
desc: ''
updated: 1652786933915
created: 1652786933915
tags:
  - articles
---

# [Automate Tweet and Grow Twitter Followers - IT Panther](https://www.itpanther.com/automate-tweet/)

In this article I am going to show you steps to automate tweet. We are going to use the most popular programming language Python. If you want other automation ideas then you can read [here](https://www.itpanther.com/python-automation-ideas-for-beginners-with-examples/).

Prerequisites:

1.  Download & Install [Python](https://www.python.org/downloads/)
2.  Install [Tweepy](https://docs.tweepy.org/en/latest/install.html)

## Twitter Developer Account

You need to register with [Twitter Developer Account](https://developer.twitter.com/) in order to get API Token and API Secret Keys. These will be required to authenticate to twitter on your behalf. Once you make a for twitter developer account than it is probably going to take approximately 24 hours before Twitter team reviews and approves your request.

## Twitter Developer Account Setup to Automate Tweet

You can follow this [Twitter’s official link](https://developer.twitter.com/en/docs/developer-portal/overview) for initial setup of your account.

## Download Inspirational Quotes Data

In this program we are using Inspirational Quotes which can be [downloaded from here](https://raw.githubusercontent.com/akhiltak/inspirational-quotes/master/Quotes.csv). This file contains around 75000+ Inspirational Quotes. We are going to read quotes from this file and tweet it.

Feel free to use any other dataset if you want.

## Python Program to Automate Tweet

Here is the complete code which I have written, of-course you can change it as per your need.

```
import tweepy
import pandas as pd
import time

latest_tweet_number = 0


with open('C:\\twitter\\latest.txt') as f:
    latest_tweet_number = int(f.read())

print(latest_tweet_number)

import pandas as pd
df = pd.read_csv(r'C:\Users\USER\Downloads\quotes.csv', sep=';')

def tweet_now(msg):
    msg = msg[0:270]
    try:

        auth = tweepy.OAuthHandler("DthisisnotrealEcjpTv1", 
            "h3dHaEQrjlOGT5Bqtw1DthisisnotrealLgNjVV0L05hRJ")
        auth.set_access_token("2517455480-UQBnDthisisnotrealSn9CI5oN", 
            "2WNbmrhXWDthisisnotrealNKBzUL")
        api = tweepy.API(auth)
        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        api.update_status(msg)
        print(msg)

        print("Tweeted")
    
    except Exception as e:
        print(e)

for idx, rows in df.iterrows():
    if idx <= latest_tweet_number:
        continue
        
    hashtags = '#inspirational #inspiration #motivation #motivational #inspirationalquotes #inspire #motivationalquotes #quotes #love #quoteoftheday #success #believe #mindset #life #positivevibes #entrepreneur #quote #positivity #goals #selflove #happiness #lifestyle #successquotes #bhfyp #yourself #thoughts #instadaily #loveyourself #photooftheday #bhfyp'
    tweet_now(rows['QUOTE'] + ' - ' + rows['AUTHOR'] + '\n\n\n' + hashtags)
    
    with open('C:\\twitter\\latest.txt',"w") as f:
        f.write(str(idx))

    print("done")
    time.sleep(1800)
    
```

## Scheduling Program

If you want to run this program 24\*7 then you need to make sure that you are running it on one of the servers which remains always available. I would recommend to use IBM Cloud as you can just sign-up there without the need of using any Credit Card.

I tried using IBM Cloud Functions which gives you option to run your Python program without the need of creating any servers. IBM Cloud Function is server-less which can be used to trigger your python code based on any Trigger or Scheduled Frequency.

## Automate Tweets Video

If you are someone who likes to see the steps in order to understand it better than you can watch this video.
