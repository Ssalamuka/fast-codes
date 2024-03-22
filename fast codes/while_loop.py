# ma code
from os import system

login_attempts = 0
secret_name ="ronnie"
secret_password = "1234"

while login_attempts < 3:
    username = input("username:")
    password =input("password")

    if username == secret_name and password == secret_password:
        print("\t welcome bit")
        break
    else:
        system("cls")
        print("invalid username or password")
    login_attempts += 1    
else:
    print("you have exceeded number of attempts\n\t\t program ENDED")
