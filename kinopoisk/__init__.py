from movie import Movie, Trailer
from person import Person

VERSION = (0, 5, 1)
__version__ = '.'.join(map(str, VERSION))

__all__ = ['Movie', 'Person', 'Trailer']