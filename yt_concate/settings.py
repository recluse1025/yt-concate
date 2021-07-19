import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('API_KEY')


DOWNLOADS_DIR = 'downloads'
# os.path.join 連接路徑
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'vodeos')
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'captions')