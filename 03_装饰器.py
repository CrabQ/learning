import time
from functools import wraps

# 无参装饰器

def timer(func):
    # 将原函数的属性赋值给wrap函数
    @wraps(func)
    def wrap(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print(f'time:{time.time()-start}')
        return res
    return wrap

@timer
def run():
    time.sleep(1)
    print('running')

run()
print(run.__name__)

# 有参装饰器
def outer(name):
    def timer(func):
        # 将原函数的属性赋值给wrap函数
        @wraps(func)
        def wrap(*args, **kwargs):
            start = time.time()
            res = func(*args, **kwargs)
            print(f'{name}, time:{time.time()-start}')
            return res
        return wrap
    return timer

@outer('first')
def run():
    time.sleep(1)
    print('running')

run()