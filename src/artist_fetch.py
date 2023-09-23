from lyric_request import LyricsFetcher
import random
from secrets import twitter_secrets as ts

# task: fetches artist (daily rotation) from genius, returning name
try:
    with open('artist_rotation.txt', 'r') as names:
        names_list = names.readlines()
        names.close()
except:
    print('Cannot open file.')

daily_name = names_list[random.randint(0,len(names_list))]
daily_artist = LyricsFetcher(ts.GENIUS_TOKEN, daily_name)