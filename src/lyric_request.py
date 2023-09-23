from lyricsgenius import Genius
from secrets import twitter_secrets as ts
import random
import re

# parent class for LyricsFetcher
class Artist:
    def __init__(self, access_token, artist_name):
        self.genius = Genius(access_token)
        self.artist_name = artist_name
        self.artist = self.genius.search_artist(artist_name, max_songs=1, sort="popularity")

    def __str__(self):
        return f'Artist class for {self.artist_name}'

    def get_songs(self):
        # songs are formatted like this {'songs':[{song1data}, {song2data}], 'next-page':x} can be optimized,
        # uses artist_songs method to acquire shorts lists of songs from artist. Can be optimized to one step
        artist_id = self.artist.id
        song_list = list(self.genius.artist_songs(artist_id, sort='title', page=1, per_page=50)['songs'])
        page_counter = 1

        # gets all songs and song data of artist using artist_songs method
        while self.genius.artist_songs(artist_id, sort='title', page=page_counter, per_page=50)['next_page'] != None:
            page_counter += 1
            song_list.extend(self.genius.artist_songs(artist_id, sort='title', page=page_counter, per_page=50)['songs'])

        # adds song to list if it has lyrics and your artist isn't a feature
        name_list = [song['title'] for song in song_list if
                    song['lyrics_state'] == 'complete' and song['artist_names'].lower() == self.artist_name.lower()]
        name_tuple = tuple(name_list)
        name_list = list(name_tuple)

        # removes unicode nospace character
        for song in name_list:
            song_en = song.encode('ascii', 'ignore')
            song = song_en.decode()
        return name_list
    
    # returns list of songs from text file
    def song_list(self):
        with open(f'{self.artist.name}SongsList.txt', 'r') as songs_file:
            song_list = songs_file.readlines()
            songs_file.close()
        return song_list

# To fetch lyrics from genius using lyric genius library, returns filtered lyrics
class LyricsFetcher(Artist):
    def __init__(self, access_token, artist_name):
        Artist.__init__(self, access_token, artist_name)

    def find_random_song(self):
        # Returns type Song
        return self.artist.songs[random.randint(0, len(self.artist.songs) - 1)]

    # Get the lyrics for a song from genius using artist name, and song title
    def fetch_lyrics(self, song):
        # Formatting lyrics
        lyrics = song.to_text()
        lyrics_pattern = re.compile(r'(\[[A-Za-z\?]+\]|Embed|You might also like)')
        new_lyrics = lyrics_pattern.sub('', lyrics)
        new_lyrics = new_lyrics.splitlines()
        new_lyrics = new_lyrics[1:]
        use_lyrics = ''
        for line in new_lyrics:
            use_lyrics += line + '\n'

        return use_lyrics