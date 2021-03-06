# 迭代器
def my_iter(obj):
    iter_obj = obj.__iter__()
    while True:
        try:
            print(iter_obj.__next__())
        except StopIteration:
            break

my_iter((1,2,3,4))

# 自定义迭代器:生成器
def my_range(start, stop, step):
    while start<stop:
        yield start
        start += step

print(list(my_range(1, 10, 2)))

# send
def f1():
    l = []
    while True:
        k = yield 'aa'
        l.append(k)
        print(l)
        k = yield 'bb'
        l.append(k)
        print(l)

g = f1()
g.send(None)
print(g.send('1'))
print(g.send('2'))



