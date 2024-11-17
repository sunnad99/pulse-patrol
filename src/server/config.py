import os
import urllib

from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")


# URL-encode the user and password
POSTGRES_USER_ENCODED = urllib.parse.quote_plus(POSTGRES_USER)
POSTGRES_PASSWORD_ENCODED = urllib.parse.quote_plus(POSTGRES_PASSWORD)
