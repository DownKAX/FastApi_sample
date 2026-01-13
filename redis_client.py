import os
from redis.asyncio import Redis, ConnectionPool
import redis

redis_host = os.getenv("REDIS_HOST", "localhost")
pool = ConnectionPool(host=redis_host, port=6379, db=0, decode_responses=True)
sync_pool = redis.ConnectionPool(host=redis_host, port=6379, db=0, decode_responses=True)

async def get_async_redis():
    return Redis(connection_pool=pool)

async def get_sync_redis():
    return Redis(connection_pool=sync_pool)