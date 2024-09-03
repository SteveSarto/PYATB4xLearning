class VWOlogin:
    def __init__(self,email_arg,password_arg):
        self.email=email_arg
        self.password=password_arg
    def login(self):
        if self.email == "stevesarto0715@gmail.com" and  self.password=="Pass123":
            print("approved")
        else:
            print("rejected")
email=input("enter email")
Password=input("enter password")
log=VWOlogin(email,Password)
log.login()