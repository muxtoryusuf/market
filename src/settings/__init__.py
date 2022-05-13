import os
from decouple import config

DEBUG = config('DEBUG', default=True, cast=bool)

if DEBUG:
    from .development import *
else:
    from .production import *
