#login_system 

username = 'kiana'
password = 1383
for x in range(3) :
    user = input('Enter your username :')
    pss = input('Enter your password :')
    if user == username and pss == password :
        print(loginsuccessful)
        break
    else :
        print(Usernameandpasswordareincorrect,pleaseloginagain) 
else :
        print(Accountislocked)   
        