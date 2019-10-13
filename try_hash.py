import hashlib
import time
import sys

##CONSTANT
STR_COUNT = 10000

org = sys.argv[1]

def randomsalt():
    import string, random
    at = string.ascii_lowercase + string.ascii_uppercase
    return ''.join([random.choice(at) for i in range(10)])

def salthash(s):
    return hashlib.sha256((randomsalt() + s).encode('utf-8')).hexdigest()

def stretching(s):
    for x in range(STR_COUNT):
        s = salthash(s)
    return s

start = time.time()
h_st = stretching(org)
syori_time = time.time() - start
print('処理時間（ミリ秒）：' + str(syori_time))
print('元の値：' + org)
print('ハッシュ値：' + h_st)
