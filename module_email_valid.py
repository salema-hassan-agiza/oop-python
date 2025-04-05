name = input("enter your name : ")
email = input("enter your email : ")
def valid_name(name):
    if not name.replace(" ","").isalpha():
        raise ValueError("invalid name!")
def valid_email(email):
    
    if "@" not in email or "." not in email or email.index("@") > email.index("."):
        raise ValueError("invalid email adress!")
def valid_user(name,email):
    try:
        valid_name(name)
        valid_email(email)
        accept = ("welcome to your account!")
    except ValueError as e:
        print(e)
    else:
        print(accept)
    finally:
        print("end")
valid_user(name,email)