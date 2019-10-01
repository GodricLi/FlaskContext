# by luffycity.com
import redis

conn = redis.Redis(host='140.143.227.206',port=6379,password='1234')

print(conn.keys())