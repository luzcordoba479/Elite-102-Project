import mysql.connector

  
def landing_page():
    print('Welcome to Nova Bank! \n----------------------------')
    print('1: Sign In \n2: New? Create Account \n3: Bank Admin Log In')
    choice = input('Enter a number to continue: ')
    if choice == '1':
        SignIn()
    elif choice == '2':
        NewCreate()
    elif choice == '3':
        AdminIn()
    else:
        print('Invalid input, try again')

        
def SignIn():
  connection = mysql.connector.connect(user = 'root', database = 'bankapp_data', password = 'SQL$$17c2c')
  cursor = connection.cursor()

  username = input('Username:')
  password = input('Password: ')

  cursor.execute("SELECT * FROM usersdata WHERE username = %s AND password = %s", (username, password))
  if (len(cursor.fetchall()) > 0):
      print('Succesful log in')
      pass #Enter system things here
  else:
      print('Unsuccesful log in')
      cursor.close()     
      connection.close()
      retr = input('1: Try again \n2: Create an account \n')
      if retr == '1':
          return SignIn()
      elif retr == '2':
          print('-----------------------')
          NewCreate()
  
  
  
      
      


def NewCreate():
    print('Thank you for choosing Nova Bank! \nLet\'s get you started')

def AdminIn():
    print('This is option 3')





landing_page() 
pass   