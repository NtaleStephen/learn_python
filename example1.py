# write a program that  keeps asking the user user for a paswword untill they enter the correct one
correct_password = "secret"
while True:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted.")
        break
    else:
        print("Incorrect password. Try again.")