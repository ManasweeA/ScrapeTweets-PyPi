import requests
import json

class ScrapeTweets:
    def __init__(self):
        self.authorization = ''
        self.guestToken = ''
        
    def setAuthorization(self, data):
        self.authorization = data

    def setGuestToken(self, data):
        self.guestToken = data
    
    def fetchTweetByHashTagandCount(self, hashtag, count):
        self.header={'authorization':self.authorization,
        'x-guest-token':self.guestToken}

        URL = 'https://api.twitter.com/2/search/adaptive.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media_availability=true&send_error_codes=true&simple_quoted_tweet=true&q=%23'+ hashtag +'&count='+ str(count) +'&query_source=typed_query&pc=1&spelling_corrections=1&ext=mediaStats%2ChighlightedLabel'

        x = requests.get(URL,headers=self.header)
        x=x.json()

        print(x)
        all_tweets = x['globalObjects']['tweets']

        return all_tweets