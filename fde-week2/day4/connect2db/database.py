import psycopg
import os
from dotenv import load_dotenv

"""
This module provides functionality to connect to a PostgreSQL database using psycopg.
It loads the database URL from the environment variables and provides a helper function
to get a new database connection.
Steps
1. load dotenv
2. get the DATABASE_URL from environment variables
3. connect to the database using psycopg with a get helper function
"""

load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment.")


def get_connection():
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL is not set in the environment.")
    return psycopg.connect(DATABASE_URL)