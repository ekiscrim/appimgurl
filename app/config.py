import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TESTING = True
SECRET_KEY = 'SecretKeyParaSesions'

# uri de sqlalchemy

CSRF_ENABLED = True
CSRF_SESSION_KEY = "algoimposiblededescifrar"