import mysql.connector
import random
import sys


def find_user(Username, found):
    connection = mysql.connector.connect(user = 'root', database = 'bankapp_data', password = 'SQL$$17c2c')
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM usersdata WHERE username = %s", (Username))
    if (len(cursor.fetchall()) > 0):
      print("User exists")
      found = True
    else: 
      cursor.close()
      connection.close() 
    
    return found 

def opening_accounts(accounts):
  Account = input("What kind of account would you like to open?\n1: Checking \n2: Savings \n")
    
  if Account == '1':
    accounts += 1
    input('Enter inital deposit (min of $10): $')
            
  elif Account == '2':
    accounts += 1
    input('Enter inital deposit (min of $10): $')
  else:
    print('Please enter a correct value')
    Account = input("What kind of account would you like to open?\n1: Checking \n2: Savings \n")
  
  
  return accounts   

def display_userdetails(accnum, Name, pin, Username, Birth, Mail, Phone, accounts):
    print(f"""\nUser details -  \nName: {Name}
DOB: {Birth}
Phone Number: {Phone}
Email: {Mail}
\n
Account Details - \nUsername: {Username}
Account Number: {accnum}
PIN: {pin}
Opened Accounts: {accounts}
""")

def landing_page():
    print('Welcome to Nova Bank! \n----------------------------')
    print('1: Sign In \n2: New? Create Account \n3: Bank Admin Log In \n4: Exit Program')
    choice = input('Enter a number to continue: ')
    if choice == '1':
        sign_in()
    elif choice == '2':
        new_create()
    elif choice == '3':
        admin_in()
    elif choice == '4':
        print('Thank you for using Nova Bank. See you later!')
        sys.exit()    
    else:
        print('Invalid input, try again')

        
def sign_in():
  connection = mysql.connector.connect(user = 'root', database = 'bankapp_data', password = 'SQL$$17c2c')
  cursor = connection.cursor()

  username = input('Username: ')
  password = input('Password: ')

  cursor.execute("SELECT * FROM usersdata WHERE username = %s AND password = %s", (username, password))
  if (len(cursor.fetchall()) > 0):
      print('Succesful log in')
      pass #Enter system things here
  else:
      print('Unsuccesful log in')
      cursor.close()     
      connection.close()
      retr = input('1: Try again \n2: Create an account \n3: Return to landing page')
      if retr == '1':
          return sign_in()
      elif retr == '2':
          print('-----------------------')
          new_create()
      elif retr == '3':
          print('-----------------------')   
          landing_page()
      else:
          print('Invalid input, try again') 
          retr = input('1: Try again \n2: Create an account \n3: Return to landing page')
  
  

def new_create():
    connection = mysql.connector.connect(user = 'root', database = 'bankapp_data', password = 'SQL$$17c2c')
    cursor = connection.cursor()
    
    print('Thank you for choosing Nova Bank! \nLet\'s get you started \n')
    print('1) Personal Information - \n')
    Name = input('First and last name: ')
    Birth = input('Date of birth [YYYY-MM-DD]: ')
    
    Phone = input('Phone number [123-456-7890]: ')
    while True:
        if len(Phone) != 12:
            print('Please enter a valid 10 digit phone number with the designated format')
            Phone = input('Phone number [123-456-7890]: ')
        else:
            break    
    Mail = input('Email: ')
    while True:
        if '@' and '.' not in Mail:
            print('Valid email must contain \'@\' and domain name (user@gmail.com)')
            Mail = input('Email: ')
        else:
            break
    print('-------------------------------------')
    print('Please ensure all the information you\'ve entered is correct:')
    print(f'Name: {Name} \nDOB: {Birth} \nPhone Number: {Phone} \nEmail: {Mail}')
    fcon = input('1: This is correct \n2: This is not correct \n') 
    while True:
        if fcon != '1' and fcon != '2':
            print('Please enter a valid input')
            fcon = input('1: This is correct \n 2: This is not correct \n')
        else: 
            if fcon == '1':
                cursor.close()     
                connection.close()
                print('------------------------')
                break
            elif fcon == '2':
                new_create()    

    print('2) Account set up - \n')
    found = False
    Username = [input('Username: ')]
    while find_user(Username, found) is True:
      print('Please choose another username')
      found = False
      Username = [input('Username: ')]
    
    Password = input('Password: ')
    while True:
        if len(Password) < 8:
            print('Password must be at least 8 characters long')
            Password = input('Password: ')
        else: 
            confirm = input('Confirm password: ')   
            if Password != confirm:
                print('Passwords do not match')
                confirm = ('Confirm password: ')
            else:
                print('----------------------')
                break
    print('3) Bank account set up - \n')
    accnum = random.randrange(111111, 999999)
    accounts = 0
    rask = '1'
    
    while rask == '1':
        accounts = opening_accounts(accounts)
        print('---------------------------')
        rask = input('Would you like to open another account? \n1: Yes \n2: No \n')
        if rask == '2':
            break

    print('-----------------------')
    print('4) Finalize - \n')
    pin = input('Create a PIN number for your account: ')
    while True:
        if len(pin) < 4 or len(pin) > 12:
            print('PIN must be 4-12 numbers long')  
            pin = input('Create a PIN number for your account: ')
        else:
            break

    print('\nPlease review the following information: ')  
    Username = Username[0] 
    
    print(display_userdetails(accnum, Name, pin, Username, Password, Birth, Mail, Phone, accounts))

    connection = mysql.connector.connect(user = 'root', database = 'bankapp_data', password = 'SQL$$17c2c')
    cursor = connection.cursor()
    
    insert = "INSERT INTO usersdata(AccNum, name, PIN, username, password, DOB, email, phone, accounts) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (accnum, Name, pin, Username, Password, Birth, Mail, Phone, accounts)    
    cursor.execute(insert, values)
    connection.commit()
    print('Your account has been finalized!')
    print('You can change these details at any time')
    print('----------------------')
    cursor.close()     
    connection.close()
    sign_in()




def admin_in():
    connection = mysql.connector.connect(user = 'root', database = 'bankapp_data', password = 'SQL$$17c2c')
    cursor = connection.cursor()

    print("""For demo reasons enter the following values - 
User: a.christinam
Password: chris879 \n""")
    
    user = input('User: ')
    password = input('Password: ')

    cursor.execute("SELECT * FROM adminusers WHERE User = %s AND Password = %s", (user, password))
    if (len(cursor.fetchall()) > 0):
      print('Succesful log in')
      pass #Enter system things here
    else:
      print('Unsuccesful log in')
      cursor.close()     
      connection.close()
      retr = input('1: Try again \n2: Return to landing page \n')
      if retr == '1':
          return admin_in()
      elif retr == '2':
          landing_page()
      else:
          print('Invalid input, try again.')
          retr = input('1: Try again \n2: Return to landing page \n')   

def user_system():
    pass



def admin_system():
    pass



landing_page() 
