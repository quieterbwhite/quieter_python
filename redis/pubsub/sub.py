import redis

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

pubsub = r.pubsub()
pubsub.subscribe(['hole'])

for item in pubsub.listen():
    print(item)
