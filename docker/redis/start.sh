docker run \
-p 6379:6379 \
-v $PWD/data:/data \
-v $PWD/conf/redis.conf:/etc/redis/redis.conf \
--privileged=true \
--name fachan-redis \
-d redis redis-server /etc/redis/redis.conf
