from lyric_request import Artist

# This is a script you should run once. It will create a text file containing all songs by your artist
songs = Artist.get_songs()
print(songs)

# write songs to text file with each song on a different line.
with open('artist_rotation.txt', 'w') as song_f:
    song_counter = 0 
    for song in songs:
        try:
            song_f.write(f'{song}\n')
            song_counter += 1
        except(UnicodeEncodeError):
            song_f.write('')
    print(f'Wrote {song_counter} songs to file.')
    song_f.close()

with open('artist_rotation.txt', 'r') as song_f:
    try: 
        songs_list = song_f.read()
        print(f'Successfully read file!\n{songs_list}')
    except: 
        print('Error: could not read file.')