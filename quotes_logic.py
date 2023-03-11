import db_operations as db

def user_sign_in(username):
    while True:
        user = db.get_user(username)
        if user:
            id, username, first_name, last_name, phone, email = user[0]
            communication = input(f'Hi {username}. Please verify your email or phone number: ')
            if communication == phone or email:
                print(f"Welcome {username}! You've successfully logged in")
                break
        else:
            print("User doesn't exist. Try again!")
            username = input("Enter username or press 0 to exit: ")
        if username == '0': 
            print('Thankyou!')
            break

def user_sign_up(username):
    user = db.get_user(username)
    while True:
        if user:
            print('User already exists. Please select a different username!')
            username = input("Enter username or press 0 to exit: ")
        else: 
            print('Press enter to leave blank\nusername is mandatory. And user needs to enter either phone or email')
            first_name = input('Enter your First Name (optional): ')
            last_name = input('Enter your Last Name (optional): ')
            phone = input('Enter your phone: ')
            email = input('Enter your email: ')
            # phone number checking while signing up

            user = db.add_user(username, first_name, last_name, phone, email)
            break
        if username == '0':
            print('Thankyou!')
            break
