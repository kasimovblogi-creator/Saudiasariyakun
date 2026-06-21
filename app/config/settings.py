from dotenv import load_dotenv
import os

load_dotenv()

# ==========================================
# BOT
# ==========================================

BOT_TOKEN = os.getenv("BOT_TOKEN")

# ==========================================
# ADMIN & GROUP
# ==========================================

ADMIN_ID = int(
    os.getenv("ADMIN_ID", 0)
)

GROUP_ID = int(
    os.getenv("GROUP_ID", -1003990513372)
)

# ==========================================
# CHANNEL
# ==========================================

CHANNEL_USERNAME = os.getenv(
    "CHANNEL_USERNAME",
    "@saudiya_sari1"
)

# ==========================================
# DATABASE
# ==========================================

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URL = (
    f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)