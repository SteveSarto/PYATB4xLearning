#decorators

def my_decorator(func):
    def wrapper():
        print("something happening before decr")
        print("helmet","go pro")
        func()
        print("something happen after func is called")
        print("safe rive")
    return wrapper()
@my_decorator
def drive_bike():
    print("im driving")
