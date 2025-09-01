# generator2.py

# 상황: 시간이 오래 걸리는 작업을 처리해야 하는데, 모든 결과가 필요하지 않은 경우

import time

def longtime_job():
    print('job start')
    time.sleep(1)
    return "done"

# list_job=[longtime_job() for i in range(5)]
list_job=(longtime_job() for i in range(5)) #제너레이터 표현식
print(next(list_job))
