class Song:
    # Represents a single song object
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration  # duration in seconds

    # String representation of the song object
    def __str__(self):
        return f"{self.title} by {self.artist} ({self.duration} sec)"
    
class Playlist:
    # Represents a playlist of song objects
    def __init__(self, name):
        self.name = name
        # Init an empty list to hold songs
        self.songs = []

    # Method to add a song to the playlist
    def add_song(self, song):
        self.songs.append(song)
        print(f'Added {song} to playlist {self.name}')

    # Method to remove a song from the playlist
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f'Removed {song} from playlist {self.name}')
        else:
            print(f'Song {song} not found in playlist {self.name}')

    # Method to get all songs in the playlist
    def get_songs(self):
        return self.songs

    # String representation of the playlist
    def __str__(self):
        return f"Playlist: {self.name}, Songs: {[str(song) for song in self.songs]}"
    
class Jukebox:
    # Represents a jukebox that can manage multiple playlists
    def __init__(self):
        # Init an empty dictionary to hold playlists
        self.playlists = {}

    # Method to create a new playlist
    def create_playlist(self, name):
        if name not in self.playlists:
            self.playlists[name] = Playlist(name)
            print(f'Created playlist {name}')
        else:
            print(f'Playlist {name} already exists')

    # Method to delete a playlist
    def delete_playlist(self, name):
        if name in self.playlists:
            del self.playlists[name]
            print(f'Deleted playlist {name}')
        else:
            print(f'Playlist {name} does not exist')

    # Method to add a song to a specific playlist
    def add_song_to_playlist(self, playlist_name, song):
        if playlist_name in self.playlists:
            self.playlists[playlist_name].add_song(song)
        else:
            print(f'Playlist {playlist_name} does not exist')

    # Method to remove a song from a specific playlist
    def remove_song_from_playlist(self, playlist_name, song):
        if playlist_name in self.playlists:
            self.playlists[playlist_name].remove_song(song)
        else:
            print(f'Playlist {playlist_name} does not exist')

    # Method to get all songs from a specific playlist
    def get_playlist_songs(self, playlist_name):
        if playlist_name in self.playlists:
            return self.playlists[playlist_name].get_songs()
        else:
            print(f'Playlist {playlist_name} does not exist')
            return []

    # String representation of the jukebox
    def __str__(self):
        return f"Jukebox with Playlists: {list(self.playlists.keys())}"
