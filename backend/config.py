import os
from dotenv import load_dotenv
from pathlib import Path
from loguru import logger

load_dotenv()

url = Path(__file__).resolve().parent.parent

DB_HOST=os.getenv('DB_HOST')
DB_PORT=os.getenv('DB_PORT')
DB_USER=os.getenv('DB_USER')
DB_PASS=os.getenv('DB_PASS')
DB_NAME=os.getenv('DB_NAME')


DB_URL=f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

logger.add(f'{url}/logs/logs.log', rotation='20 KB', compression='zip')

