import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_repository.delete_all()
album_repository.delete_all()

artist1 = Artist('Take That')
artist_repository.save(artist1)

artist2 = Artist('In Flames')
artist_repository.save(artist2)

album1 = Album('Everything Changes', artist1, 'Pop')
album_repository.save(album1)

album2 = Album('Siren Charms', artist2, 'Metal')
album_repository.save(album2)

artists = artist_repository.select_all()
albums = album_repository.select_all()

pdb.set_trace()
