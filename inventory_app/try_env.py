import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

EMAIL = os.environ.get("EMAIL")
PASS = os.environ.get("PASS")
print(EMAIL)
print(PASS)