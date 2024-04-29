import mysql.connector
import random
import sys
from datetime import datetime


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
    accname = input('Choose a name for your account: ')
    spef = str(random.randrange(111111, 999999))
    fullspef = int(f'479{spef}')
    accounts += 1
    bal = int(input('Enter inital deposit (min of $10): $'))
    if bal < 10:
        print('Please enter $10 or more for intial deposit')
        bal = input('Enter inital deposit (min of $10): $')
         
  elif Account == '2':
    accname = input('Choose a name for your account: ')
    spef = str(random.randrange(111111, 999999))
    fulspef = int(f'409{spef}')
    accounts += 1
    bal = float(input('Enter inital deposit (min of $10.00): $'))
    
    if bal < 10:
        print('Please enter $10 or more for initial deposit')
        bal = float(input('Enter inital deposit (min of $10.00): $'))
  else:
    print('Please enter a correct value')
    Account = input("What kind of account would you like to open?\n1: Checking \n2: Savings \n")
    
def display_userdetails(usernum, Name, pin, Username, Birth, Mail, Phone, accounts):
    print(f"""\nUser details -  \nName: {Name}
DOB: {Birth}
Phone Number: {Phone}
Email: {Mail}
\n
Account Details - \nUsername: {Username}
Account Number: {usernum}
PIN: {pin}
Opened Accounts: {accounts}
""")

def greetings(holder):
    beep = datetime.now()
    curr_hour = int(beep.hour)
    if curr_hour < 5 and curr_hour > 18:
        print(f'Good evening, {holder}')
    elif curr_hour >= 5 and curr_hour <= 12:
        print(f'Good morning, {holder}')
    elif curr_hour > 12 and curr_hour <= 18:
        print(f'Good afternoon, {holder}')   
    else:
        print(f'Hello, {holder}')    
    
    return greetings        

def display_usermenu():
    print("""1: Check Balance
2: Deposit
3: Withdrawl
4: More""")
                     
def landing_page():
    print('Welcome to Nova Bank! \n----------------------------')
    print('1: Sign In \n2: New? Create Account \n3: Exit Program')
    choice = input('Enter a number to continue: ')
    if choice == '1':
        print('----------------------------')
        sign_in()
    elif choice == '2':
        print('----------------------------')
        new_create()
    elif choice == '3':
        print('Thank you for using Nova Bank. See you later!')
        sys.exit()    
    else:
        print('Invalid input, try again')
        landing_page()    
        
    print('Welcome to Nova Bank! \n----------------------------')
    print('1: Sign In \n2: New? Create Account \n3: Exit Program')
    choice = input('Enter a number to continue: ')
    if choice == '1':
        print('----------------------------')
        sign_in()
    elif choice == '2':
        print('----------------------------')
        new_create()
    elif choice == '3':
        print('Thank you for using Nova Bank. See you later!')
        sys.exit()    
    else:
        print('Invalid input, try again')
        choice = input('Enter a number to continue: ')
 
def sign_in():
  connection = mysql.connector.connect(user = 'root', database = 'bankapp_data', password = 'SQL$$17c2c')
  cursor = connection.cursor()

  username = input('Username: ')
  password = input('Password: ')

  cursor.execute("SELECT * FROM usersdata WHERE username = %s AND password = %s", (username, password))
  if (len(cursor.fetchall()) > 0):
      cursor.close()     
      connection.close()
      print('-----------------------')
      user_system(username, password)
      
  else:
      print('Unsuccesful log in')
      cursor.close()     
      connection.close()
      retr = input('1: Try again \n2: Create an account \n3: Return to landing page \n')
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
    uni_num = str(random.randrange(111111, 999999))
    usernum = int((f'479{uni_num}'))
    
    print('**Nova Bank requires you to create a default checking account')
    dfname = "Default Checking"

    bal = float(input("Please enter an intial deposit to activate: $"))
    accounts = 1
    
    option = input("Would you like a credit/debit card? \n1: Yes \n2: No \n")
    if option == '1':
        cspef = str(random.randrange(111111111, 999999999))
        card = (f'417095{cspef}')
        print(f"This is your card number: {card}")
    elif option == '2':
        card = "none"
    else:
        print("Please enter a valid input")
        option = input("Would you like a credit/debit card? \n1: Yes \n2: No \n")

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
    
    print(display_userdetails(usernum, Name, pin, Username, Birth, Mail, Phone, accounts))

    connection = mysql.connector.connect(user = 'root', database = 'bankapp_data', password = 'SQL$$17c2c')
    cursor = connection.cursor()
    
    insert = "INSERT INTO usersdata(UserAccNum, name, PIN, username, password, DOB, email, phone, accounts) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (usernum, Name, pin, Username, Password, Birth, Mail, Phone, accounts)    
    cursor.execute(insert, values)

    insert2 = "INSERT INTO useracc(AccNum, CardNum, Balance, UserAccNum, AccName) VALUES(%s, %s, %s, %s, %s)"
    values2 = (usernum, card, bal, usernum, dfname)
    cursor.execute(insert2, values2)

    connection.commit()
    print('Your account has been finalized!')
    print('Sign in to view your account in more detail. You can change select credential at any time.')
    print('----------------------------------------')
    cursor.close()     
    connection.close()
    sign_in()

def usermenu_choice(choice, usernum, username, password):
    connection = mysql.connector.connect(user = 'root', database = 'bankapp_data', password = 'SQL$$17c2c')
    cursor = connection.cursor()    

    if choice == '1':
        print('Check Balance - ')
        cursor.execute("SELECT AccName, AccNum, Balance FROM useracc WHERE UserAccNum = %s", (usernum))
        for item in cursor:
            print(item)
        user_system(username, password)

    elif choice == '2':
        usernum = usernum[0]
        print('Deposit - ')
        print("Due to the underdevelopement of Nova Bank, users must enter the total amount after the deposit")
        deposit = float(input("What is your total balance after this deposit? $"))
        cursor.execute("UPDATE useracc SET Balance = %s WHERE UserAccNum = %s", (deposit, usernum))
        cursor.close()
        connection.close() 
        print("Deposit finished returning home")
        user_system(username, password)

    elif choice == '3':
        usernum = usernum[0]
        print('Withdrawl - ')
        print("Due to the underdevelopement of Nova Bank, users must enter the total amount after the withdrawl")
        withdrawl = float(input("What is your total balance after this withdrawl? $"))
        cursor.execute("UPDATE useracc SET Balance = %s WHERE UserAccNum = %s", (withdrawl, usernum))
        print("Withdrawl finished returning home")
        user_system(username, password)

    elif choice == '4':
        print('More - ')
        more = input("""5: Open a bank account (x) \n6: Account Details (x)\n7: Sign Out \n""")
        
        if more == '5':
            feed = cursor.execute("SELECT accounts FROM usersdata WHERE UserAccNum = %s", (usernum))
            opening_accounts(feed)

        elif more == '6':
            connection = mysql.connector.connect(user = 'root', database = 'bankapp_data', password = 'SQL$$17c2c')
            cursor = connection.cursor()    
            userinf = ("SELECT * FROM usersdata WHERE UserAccNum = %s", (usernum))
            cursor.execute(userinf)
            for det1 in cursor:
                print(det1)
   
            
            accinf = ("SELECT * FROM useracc WHERE UserAccNum = %s", (usernum))
            cursor.execute(accinf)
            for det2 in cursor:
                print(det2)

        elif more == '7':
            print('Thank you for using Nova Bank! See you later :)')
            sys.exit
       

def user_system(value1, value2):
    connection = mysql.connector.connect(user = 'root', database = 'bankapp_data', password = 'SQL$$17c2c')
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM usersdata WHERE username = %s AND password = %s", (value1, value2))
    name = str(cursor.fetchone())
    cursor.execute("SELECT UserAccNum FROM usersdata WHERE username = %s AND password = %s", (value1, value2))
    usernum = cursor.fetchone()
    cursor.close()
    connection.close()

    greetings(name)
    display_usermenu()
    feed = input('Enter a number to continue: ') 
    print('-------------------------')
    usermenu_choice(feed, usernum, value1, value2)
    



###Testing
landing_page() 
