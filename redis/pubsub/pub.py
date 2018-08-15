import redis

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
r.publish("channel_docid", {"docid":"8a3a60fe-1426-4d6d-8d27-66707f3ac58c", "date":"2015-07-12"})
