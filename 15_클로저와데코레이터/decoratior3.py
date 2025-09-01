#decorator3.py

import time
def elapsed(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("함수 수행시간: {end=start}초")
        return result  # 기존 함수의 수행 결과를 반환
    return wrapper
@elapsed
def myfunc(msg):
    print(f'{msg},{dict}를 출력합니다.')

myfunc("you need python",{1:'python',2:'js'})
myfunc("Error",{1:'python',2:'js'})