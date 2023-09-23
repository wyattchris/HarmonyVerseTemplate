import tweepy
# Import for keys, and lyric fetching
from secrets import twitter_secrets as ts
from artist_fetch import daily_artist as artist
from poem_creator import PoemCreator

# Store all required keys and secrets
consumer_key = ts.CONSUMER_KEY
consumer_secret = ts.CONSUMER_SECRET
access_token = ts.ACCESS_TOKEN
access_secret = ts.ACCESS_SECRET
client_id = ts.CLIENT_ID
client_secret = ts.CLIENT_SECRET
bearer = ts.BEARER_TOKEN

# Create client and authorize
client = tweepy.Client(bearer, consumer_key, consumer_secret,
                       access_token, access_secret)

# Fetch random artist of the day and random song
song_title = artist.find_random_song()
lyrics = artist.fetch_lyrics(song_title)

# Turn song into poem tweet
my_poem_creator = PoemCreator()
poem_tweet = my_poem_creator.generate_haiku(lyrics)
first_colon_index = str(song_title).index(':')
substring = str(song_title)[:first_colon_index]
final_tweet = f'{poem_tweet}\n - {substring}'

print(f'Tweet: \n {final_tweet}')
print(len(final_tweet))

# Tweet haiku
client.create_tweet(final_tweet)
