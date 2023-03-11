import db_operations as db
import quotes_logic as ql

db.create_tables()


print('''WELCOME TO QUOTE-MUSE!!!''')

print('''
Press:
1. Login
2. Signup
''')
user_op = int(input('> '))

if user_op == 1:
    ql.user_sign_in(input('Enter your username: '))

elif user_op == 2:
    ql.user_sign_up(input('Enter your username: '))