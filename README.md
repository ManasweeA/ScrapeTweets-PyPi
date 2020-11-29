Scrape Twitter Tweets
===================


ScrapeTweets is a Python package that scrapes all the tweets from the Twitter API by using Hashtags. This data can be used for various purposes like Education, Research, News, etc.

----------


Installation
-------------
Install directly from my [PyPi](https://github.com/ManasweeA/ScrapeTweets-PyPi)

> pip install ScrapeTweets

Or Clone the [Repository](https://github.com/ManasweeA/ScrapeTweets-PyPi) and install

> python3 setup.py install

Parameters
-------------

## * Authorization 
-------------
The Authorization token when you visit Twitter.

## * x-guest-token
-------------
The x-guest-token when you visit Twitter.

## * hashtag
-------------
The hashtag to search on Twitter.

## * count
-------------
The number of tweets to fetch from Twitter.


Attributes
-------------

## * setAuthorization(authorization_token)
-------------
Set the Authorization Token.

## * setGuestToken(x-guest-token)
-------------
Set the x-guest-token.

## * fetchTweetByHashTagandCount(hashtag, count)
-------------
Fetch all the tweets using Hashtag and Count.



<i class="icon-file"></i> Documentation
-------------

### 1.  Install the package
>  pip install ScrapeTweets

### 2. Import the library
>  from ScrapeTweets import ScrapeTweets

### 3. Create an object for ScrapeTweets class
> st = ScrapeTweets()

### 4. Set The Authorization Token
> st.setAuthorization(authorization_token)

### 5. Set The x-guest-token
> st.setGuestToken(x-guest-token)

### 5. Predict your Test Set results
> all_tweets_fetched = st.fetchTweetByHashTagandCount(hashtag, count)

----------



Example Code
-------------

```
from ScrapeTweets import ScrapeTweets

st = ScrapeTweets()
st.setAuthorization('Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA')
st.setGuestToken('1333095583104462848')
all_tweets_fetched = st.fetchTweetByHashTagandCount('lamborghini', 25)

# print(all_tweets_fetched)

for no, tweet in enumerate(all_tweets_fetched):
    print("Tweet No : ", no+1)
    print("Tweet text : ", all_tweets_fetched[tweet]['full_text'])
    # break

```


----------



Footnotes
-------------

You can find the code at my [Github](https://github.com/ManasweeA/ScrapeTweets-PyPi).



Connect with me on Social Media
-------------

* [www.github.com/ManasweeA](www.github.com/ManasweeA)
* [https://www.linkedin.com/in/manaswee0612/](https://www.linkedin.com/in/manaswee0612/)
