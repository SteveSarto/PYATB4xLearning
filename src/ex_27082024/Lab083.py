import time


def time_decor(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print("time taken is", {end_time - start_time})

    return wrapper()


@time_decor
def test_ui1():
    print("time taken")
    time.sleep(2)


@time_decor
def test_ui2():
    print("time taken")
    time.sleep(5)
