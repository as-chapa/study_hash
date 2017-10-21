import hashlib
import time
import sys

##CONSTANT
SALT = b'secret'
STR_COUNT = 10000

org = sys.argv[1]

def salthash(s):
    return hashlib.sha256(SALT + s.encode('utf-8')).hexdigest()

def stretching(s):
    for x in range(0, STR_COUNT):
        s = salthash(s)
    return s

start = time.time()
h_st = stretching(org)
syori_time = time.time() - start
print('処理時間（ミリ秒）：' + str(syori_time))
print('元の値：' + org)
print('ハッシュ値：' + h_st)
