import os
from dotenv import load_dotenv


load_dotenv()
TELEGRAM_BOT_KEY = os.environ.get('TELEGRAM_BOT_KEY')
