#𓆰𝐑𝐀𝐍𝐀 𝐉𝐈𝐈 𓆪
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "22182189"))
API_HASH = environ.get("API_HASH", "5e7c4088f8e23d0ab61e29ae11960bf5")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER = int(environ.get("OWNER", "6187058869"))
CREDIT = "𓆰𝐑𝐀𝐍𝐀 𝐉𝐈𝐈 𓆪"
AUTH_USER = os.environ.get('AUTH_USERS', '22182189,6187058869').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
