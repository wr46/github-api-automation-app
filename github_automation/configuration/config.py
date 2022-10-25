import os
from dotenv import load_dotenv

load_dotenv()
APP_NAME = os.getenv('APP_NAME', 'github-api-automation-app')
GITHUB_ORGANIZATION = os.getenv('GITHUB_ORGANIZATION', '')
GITHUB_HOSTNAME = os.getenv('GITHUB_HOSTNAME', '')
GITHUB_API_URL_VERSION = os.getenv('GITHUB_API_URL_VERSION', '/api/v3')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
LOG_LEVEL = os.getenv('LOG_LEVEL', 'WARNING').upper()
