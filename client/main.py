import os
from mysql.connector import errorcode
import mysql.connector
import getpass
from tabulate import tabulate
import countries, education, lifeExpectancy, infantMortality, birthDeath, gni, hdi, gii, population, fertility_rates, help_guide
import test
import sys

print ("Welcome to Group 35's Demographics App!")
usr = input("Username: ")
pwd = getpass.getpass()
host = sys.argv[1]
db = sys.argv[2]
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
  
  if len(flags) == 1 and flags[0] != "exit" and flags[0] != "help": 
    print('invalid input')
    continue

  if (flags[0] == "country"):
    countries.country(flags[1:], cnx)
  elif (flags[0] == "education"):
    education.education(flags[1:], cnx)
  elif (flags[0] == "population"): 
    population.operation(flags[1:], cnx)
  elif (flags[0] == "fertility_rates"): 
    fertility_rates.operation(flags[1:], cnx)
  elif (flags[0] == "life_expectancy"): 
    lifeExpectancy.le(flags[1:], cnx)
  elif (flags[0] == "infant_mortality"): 
    infantMortality.im(flags[1:], cnx)
  elif (flags[0] == "birth_death"): 
    birthDeath.bd(flags[1:], cnx)
  elif (flags[0] == "gni"): 
    gni.gni(flags[1:], cnx)
  elif (flags[0] == "hdi"): 
    hdi.hdi(flags[1:], cnx)
  elif (flags[0] == "gii"): 
    gii.gii(flags[1:], cnx)
  elif (flags[0] == "help"): 
    help_guide.help()
  elif (flags[0] == "test"): 
    test.run_tests(cnx, flags[1])
  elif (flags[0] == "exit"):
    print("Thanks for using our application! ;)")
    break
  else:
    print('Not a valid command name. Please use a valid table name or use help for more information')




