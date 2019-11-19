import hashlib
import time
import sys

##CONSTANT
STR_COUNT = 10000

org = sys.argv[1]

def syoritime(func):
    """
    処理時間計測用のデコレータ
    """
    def wrapper(*args, **kargs):
        start = time.time()
        func(*args, **kargs)
        syori_time = str(time.time() - start)
        print(f'処理時間（ミリ秒）：{syori_time}')
    return wrapper

def randomsalt():
    """
    英字大文字小文字10桁をランダムに返す
    """
    import string, random
    at = string.ascii_lowercase + string.ascii_uppercase
    return ''.join([random.choice(at) for i in range(10)])

def salthash(s):
    return hashlib.sha256((randomsalt() + s).encode('utf-8')).hexdigest()

def stretching(s):
    for x in range(STR_COUNT):
        s = salthash(s)
    return s

@syoritime
def main():
    h_st = stretching(org)
    print(f'元の値：{org}')
    print(f'ハッシュ値：{h_st}')

main()