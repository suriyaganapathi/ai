"""
Database Connection Setup
==========================
Motor async MongoDB client initialization
"""

from motor.motor_asyncio import AsyncIOMotorClient
from config import settings
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize async MongoDB client
try:
    if settings.MONGO_URI:
        client = AsyncIOMotorClient(settings.MONGO_URI)
        db = client[settings.MONGO_DB_NAME]
        logger.info(f"✅ MongoDB Client initialized for {settings.MONGO_DB_NAME}")
    else:
        logger.warning("⚠️  MONGO_URI not set. Database features will fail.")
        client = None
        db = None
except Exception as e:
    logger.error(f"❌ Failed to initialize MongoDB client: {e}")
    client = None
    db = None


def get_db():
    """Return database instance"""
    return db


async def test_connection():
    """Test database connection on startup"""
    try:
        await client.admin.command('ping')
        logger.info("✅ Successfully connected to MongoDB")
        return True
    except Exception as e:
        logger.error(f"❌ Failed to connect to MongoDB: {e}")
        return False
