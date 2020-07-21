import codecs
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import glob

class CreateData:

    def __init__(self):
        self.spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    def find_artist_id(self, artist_name):
        results = self.spotify.search(q='artist:' + artist_name, type='artist')
        return results['artists']['items'][0]['id']
        pass

    def find_album_id(self, album_name):
        results = self.spotify.search(q='album:' + album_name, type='album')
        return results['albums']['items'][0]['id']
        pass

    def find_track_id(self, artist_name, track_name):
        results = self.spotify.search(q='artist:' + artist_name + ' track:' + track_name, type='track')
        return results['tracks']['items'][0]['id']

    def match_songs_to_years(self):
        filenames = glob.glob("../data/lyrics_tagged/*.txt")
        for filename in filenames:
            try:
                length = len(filename.split("_"))
                artist_name = filename.split("_")[1].split("\\")[1] + " " + filename.split("_")[2]
                track_name = ' '.join(filename.split("_")[3:length - 2])
                track_album = self.spotify.track(self.find_track_id(artist_name, track_name))['album']
                album_year = track_album['release_date'][0:4]
                with codecs.open(filename, "a") as f:
                    f.write("\n" + "year: " + str(album_year))
            except:
                continue


data = CreateData()
data.match_songs_to_years()


