# This is an example of what should be in config.py. Save this file as config.py
# and then change the defaults as needed. See README.md for details.
# Not all the various classes for the web server aren't necessary as long as the
# one it's using is present. TestingConfig is needed to run the unit tests.

import os

# Web server config
PAGINATE_BY = 10
class DeploymentConfig(object):
	DATABASE_URI = "postgresql://username:password@localhost:5432/merrily"
	DEBUG = False
	SECRET_KEY = os.environ.get("MERRILY_SECRET_KEY", os.urandom(12))

class DevelopmentConfig(object):
	DATABASE_URI = "postgresql://username:password@localhost:5432/merrily"
	DEBUG = True
	SECRET_KEY = os.environ.get("MERRILY_SECRET_KEY", os.urandom(12))

class TestingConfig(object):
	DATABASE_URI = "postgresql://username:password@localhost:5432/merrily-test"
	DEBUG = True
	SECRET_KEY = os.environ.get("MERRILY_SECRET_KEY", os.urandom(12))

# Doorbell values
A_PIN = 18
B_PIN = 23
THRESHOLD = 100
LOG_URL = "http://localhost:8089/ring"

# Client values
DOORBELL_SERVER = "localhost"
DOORBELL_PORT = 8088
PLAYER = "cvlc"
PLAYER_ARGS = "--play-and-exit"
ALERT_FILE = "ring.wav"
