from redis.asyncio.client import Redis
from config import settings

redis_client = Redis(
    host="redis",
    port=settings.redis.redis_port,
    db=0
)
