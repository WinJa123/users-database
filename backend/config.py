import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

url = Path(__file__).resolve().parent.parent

URL_FROM_ENV=os.getenv('DB_URL')
DB_URL=f'sqlite:///{url}\{URL_FROM_ENV}'