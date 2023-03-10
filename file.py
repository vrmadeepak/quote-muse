import db_operations as db

db.create_tables()


print('''WELCOME TO QUOTE-MUSE!!!''')

print('''
Press:
1. Login
2. Signup
''')

user_op = int(input('> '))

if user_op == 1:
    username = input('Enter your username: ')
    user = db.get_user(username)
    if user:
        id, username, first_name, last_name, phone, email = user[0]
        communication = input(f'Hi {username}. Please verify your email or phone number: ')
        if communication == phone or email:
            print(f"Welcome {username}! You've successfully logged in")
    
elif user_op == 2:
    print('Press enter to leave blank:')
    username = input('Enter your username: ')
    
    user = db.get_user(username)
    if user:
        print('User already exists. Please select a different username!')
    else:    
        first_name = input('Enter your First Name: ')
        last_name = input('Enter your Last Name: ')
        phone = input('Enter your phone: ')
        email = input('Enter your email: ')
        # phone number checking while signing up

        user = db.add_user(username, first_name, last_name, phone, email)

