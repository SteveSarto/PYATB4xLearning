#match statement

browser=input("enter browser name")
browser=browser.lower()
match browser:
    case "chrome":
        print("Open chrome")
    case "safari":
        print("open safari")
    case"firefox":
        print("open firefox")
    case _:
        print("not found")