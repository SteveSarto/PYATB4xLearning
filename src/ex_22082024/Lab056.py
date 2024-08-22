user_input=input("who are u, manager. admin, guest")
match user_input:
    case "manager":
        print("hello manager")
    case "admin":
        print("hello, admin")
    case "guest":
        print("hello,guest")
    case _:
        print("not allowed")
