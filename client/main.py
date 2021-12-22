import os
import mysql.connector
import getpass
from tabulate import tabulate
import countries

print ("Welcome to Group 35's Demographics App!")
usr = input("Username: ")
pwd = getpass.getpass()
host = 'marmoset04.shoshin.uwaterloo.ca'
db = f'db356_{usr}'

while True:
  try:
      cnx = mysql.connector.connect(user = usr, password = pwd, host = host, database = db)
      print (f'Connected to {db}')
      break
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print('Something is wrong with your user name or password')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print('Database does not exist')
    else:
      print(err)

while True:
  print("Demographics>") 
  userinput = input()
  flags = userinput.split()
  if (flags[0] == "country"):
    if len(flags) > 1:
      countries.country(flags[1:], usr, pwd, host, db)
    else:
      print("invalid input")
  else:
    print('error')


#update countries set area = "" where code = ""
#country -update {code} --name "India" --area "893475.0"