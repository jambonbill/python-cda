# pip install python-dotenv
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

API_KEY = os.environ.get("API_KEY", "default")

print(API_KEY)
# a3491fb2-000f-4d9f-943e-127cfe29c39c