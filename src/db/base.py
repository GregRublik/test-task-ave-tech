from redis.asyncio.client import Redis
from config import settings

# redis_client = aioredis.StrictRedis(host="localhost", port=settings.redis.redis_port, db=0)

redis_client = Redis(host="localhost", port=settings.redis.redis_port, db=0)
