#decorator2.py

import time
def elapsed(original_func):
    def wrapper():
        start = time.time()
        result = original_func()
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))
        return result  # 기존 함수의 수행 결과를 반환
    return wrapper
@elapsed
def myfunc():
    print("함수가 실행됩니다.")

myfunc()