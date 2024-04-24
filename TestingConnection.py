import mysql.connector
import random

connection = mysql.connector.connect(user = 'root', database = 'bankapp_data', password = 'SQL$$17c2c')
cursor = connection.cursor()

def signing_up():
  print('3) Bank account set up - \n')
  accnum = random.randrange(111111, 999999)
  accounts = 0
  rask = '1'
    
  while rask == '1':
    opening_accounts(accounts)
    print('---------------------------')
    rask = input('Would you like to open another account? \n1: Yes \n2: No \n')
    if rask == '2':
      break


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


def FindUser(Username, found):
    #Password = input('Password: ')
    cursor.execute("SELECT * FROM usersdata WHERE username = %s", (Username))
    print('Test connected')
    if (len(cursor.fetchall()) > 0):
      print("User exists")
      found = True
    else: 
      print("User not found")
      found = False
    
    return found

def cleanup():     
    cursor.close()     
    connection.close()

       
signing_up()
#FindUser()
cleanup()    