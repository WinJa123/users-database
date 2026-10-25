import os
from dotenv import load_dotenv
from pathlib import Path
from loguru import logger

load_dotenv()

url = Path(__file__).resolve().parent.parent

URL_FROM_ENV=os.getenv('DB_URL')
DB_URL=f'sqlite:///{url}\{URL_FROM_ENV}'

logger.add(f'{url}/logs/logs.log', rotation='20 KB', compression='zip')