#correct email = abc@gmail.com
#correct password = abc@123
email = input("Kindly enter your email:")
if "@" in email:
    password = input("Kindly enter your password:")
    email=  input("Kindly enter your email:")
    if email == "abc@gmail.com" and password == "abc@123":
        print("Login successful!")
    elif email == "abc@gmail.com" and password != "abc@123":
        print("Invalid password")
        password = input("Kindly re-enter your password:")
        if password == "abc@123":
            print("Login successful!")

        else:
            print ("Still invalid password. Please try again later")
    else:
        print("Invalid email or password")
else:
    print("Invalid email format. Please enter a valid email address.")