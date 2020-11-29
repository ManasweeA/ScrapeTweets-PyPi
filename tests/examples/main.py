from ScrapeTweets import ScrapeTweets

st = ScrapeTweets()
st.setAuthorization('Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA')
st.setGuestToken('1333095583104462848')
all_tweets_fetched = st.fetchTweetByHashTagandCount('car', 25)

# print(all_tweets_fetched)

for no, tweet in enumerate(all_tweets_fetched):
    print("Tweet No : ", no+1)
    print("Tweet text : ", all_tweets_fetched[tweet]['full_text'])
    # break

