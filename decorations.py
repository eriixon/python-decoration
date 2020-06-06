from datetime import datetime


def time_it(name):
    print(name)
    def outer(method):

        def wrapper(*args):
            start = datetime.now()
            result = method(*args)
            print(datetime.now() - start)
            return result

        return wrapper
    return outer


@time_it("banana")
def one(n):
    arr = []
    for i in n:
        if i % 2 == 0:
            arr.append(i)
    return arr


@time_it("apple")
def two(n):
    return [e for e in n if e % 2 == 0]


nums = range(10 ** 4)
a1 = one(nums)
a2 = two(nums)
print(a1 == a2)
