def add_before_ui(func):
    def wrapper():
        print("before running ui tc")
        print("start browser")
        func()
        print("ending running ui tc")
        print("browser  close")
    return wrapper()
@add_before_ui
def test_ui():
    print("test ui")