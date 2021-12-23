import os
import mysql.connector
import getpass
from tabulate import tabulate
import countries, education
import population

print ("Welcome to Group 35's Demographics App!")
usr = input("Username: ")
pwd = getpass.getpass()
host = 'marmoset04.shoshin.uwaterloo.ca'
db = f'db356_{usr}'
global cnx 

try:
    cnx = mysql.connector.connect(user = usr, password = pwd, host = host, database = db)
    print (f'Connected to {db}')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print('Something is wrong with your user name or password')
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print('Database does not exist')
  else:
    print(err)

while True:
  print("Demographics> ", end = "") 
  userinput = input()
  flags = userinput.split()
  
  if len(flags) == 1: 
    print('invalid input')
    continue

  if (flags[0] == "country"):
    countries.country(flags[1:], cnx)
  elif (flags[0] == "education"):
    education.education(flags[1:], cnx)
  elif (flags[0] == "population"): 
    population.operation(flags[1:], cnx)
  elif (flags[0] == "fertility_rates"): 
    population.operation(flags[1:], cnx)
  elif (flags[0] == "exit"):
    print("Thanks for using our application! ;)")
    break
  else:
    print('Not a valid command name. Please use a valid table name or use help for more information')




