import mysql.connector
import getpass
from tabulate import tabulate
import getpass

def country(options, usr, pwd, host, db):
    for i in range(len(options)): 
        if (options[i] == "-all"):
            getAllCountries(usr, pwd, host, db)
        elif (options[i] == "-code"):
            getCountry(usr, pwd, host, db, options[1])


def getAllCountries(usr, pwd, host, db):
    cnx = mysql.connector.connect(user = usr, password = pwd, host = host, database = db)
    cursor = cnx.cursor()

    query = ("SELECT * FROM countries")

    cursor.execute(query)
    result = cursor.fetchall()

    print(tabulate(result, headers=['code', 'name', 'area'], tablefmt='pretty'))

    cursor.close()
    cnx.close()

def getCountry(usr, pwd, host, db, code):
    cnx = mysql.connector.connect(user = usr, password = pwd, host = host, database = db)
    cursor = cnx.cursor()

    query = "SELECT * FROM countries WHERE code = '{}'".format(code)
    cursor.execute(query)
    result = cursor.fetchall()

    print(tabulate(result, headers=['code', 'name', 'area'], tablefmt='pretty'))

    cursor.close()
    cnx.close()