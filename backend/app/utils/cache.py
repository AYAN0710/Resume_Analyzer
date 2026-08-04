import json
import redis
from app.config.settings import settings
from app.utils.logger import logger

redis_client=redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    decode_responses=True
)

def connect_check():
    try:
        redis_client.ping()
        logger.success("Redis connected successfully.")
    except Exception as e:
        logger.error(f"Redis connection failed: {e}")
        
def set_cache(key:str,value):
    redis_client.setex(settings.CACHE_TTL,json.dumps(value))
    
def delete_cache(key:str):
    redis_client.delete(key)
    
def clear_cache():
    redis_client.flushdb()
    logger.warning("Redis cache cleared.")
    
def cache_exists(key:str):
    return redis_client.exists(key)

def generate_cache_key(prefix,identifier):
    return f"{prefix}_{identifier}"