import redis
import json
import time
from datetime import timedelta

from database_config import redis_client


def add_apikey_to_redis(api_key, subscription=None):
    user_quota = {
        "regular": {"per_minute":5, "hourly": 300, "daily": 3600},
        "premium": {"per_minute":100, "hourly": 6000, "daily": 72000}
    }
    if not subscription:
        quotas = user_quota["regular"]
    else:
        quotas = user_quota.get(subscription)
        if not quotas:
            print({"error": "Invalid subscription"})
            return 
    redis_client.set(api_key, json.dumps(quotas))


def check_usage_limit(api_key):
    quotas = redis_client.get(api_key)
    if not quotas:
        return -1
    current_timestamp = int(time.time())
    quotas = json.loads(quotas.decode('utf-8'))
    minute_quota = quotas["per_minute"]
    rate_limit_key = f"minute:{api_key}"
    # Remove timestamps older than 1 minute
    redis_client.zremrangebyscore(rate_limit_key, '-inf', current_timestamp - 60)
    # Count the number of requests made in the last minute
    num_requests = redis_client.zcard(rate_limit_key)
    # If the number of requests is less than minute_quota, allow the request
    if num_requests >= minute_quota:
        return False
    # Add the current timestamp to the sorted set
    redis_client.zadd(rate_limit_key, {current_timestamp: current_timestamp})
    return True


def add_jwt_to_redis(jwt, ttl=timedelta(minutes=15)):
    redis_client.set("jwt_"+jwt, "valid", ex=ttl) 


def check_jwt_expiration(jwt):
    if redis_client.exists("jwt_"+jwt):
        return True
    return False 


def expire_jwt(jwt):
    redis_client.expire("jwt_"+jwt, 0)