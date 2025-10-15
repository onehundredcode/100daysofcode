class Song:
    #Represents a single song
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration  # duration in seconds

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.duration} sec)"
    
class Playlist:
    #Represents a playlist of songs
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f'Added {song} to playlist {self.name}')

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f'Removed {song} from playlist {self.name}')
        else:
            print(f'Song {song} not found in playlist {self.name}')

    def get_songs(self):
        return self.songs

    def __str__(self):
        return f"Playlist: {self.name}, Songs: {[str(song) for song in self.songs]}"
    
class Jukebox:
    #Represents a jukebox that can manage multiple playlists
    def __init__(self):
        self.playlists = {}

    def create_playlist(self, name):
        if name not in self.playlists:
            self.playlists[name] = Playlist(name)
            print(f'Created playlist {name}')
        else:
            print(f'Playlist {name} already exists')

    def delete_playlist(self, name):
        if name in self.playlists:
            del self.playlists[name]
            print(f'Deleted playlist {name}')
        else:
            print(f'Playlist {name} does not exist')

    def add_song_to_playlist(self, playlist_name, song):
        if playlist_name in self.playlists:
            self.playlists[playlist_name].add_song(song)
        else:
            print(f'Playlist {playlist_name} does not exist')

    def remove_song_from_playlist(self, playlist_name, song):
        if playlist_name in self.playlists:
            self.playlists[playlist_name].remove_song(song)
        else:
            print(f'Playlist {playlist_name} does not exist')

    def get_playlist_songs(self, playlist_name):
        if playlist_name in self.playlists:
            return self.playlists[playlist_name].get_songs()
        else:
            print(f'Playlist {playlist_name} does not exist')
            return []

    def __str__(self):
        return f"Jukebox with Playlists: {list(self.playlists.keys())}"
