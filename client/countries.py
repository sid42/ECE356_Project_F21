import mysql.connector
import getpass
from tabulate import tabulate
import getpass

def country(options, usr, pwd, host, db):
    for i in range(len(options)): 
        if (options[i] == "-code"):
            getCountryByCode(usr, pwd, host, db, options[1])
        elif (options[i] == "-name"):
            getCountryByName(usr, pwd, host, db, options[1])
        elif (options[i] == "-all"):
            getAllCountries(usr, pwd, host, db)
        elif (options[i] == "-insert"):
            insertCountry(usr, pwd, host, db, options[1:])
        elif (options[i] == "-delete"):
            deleteCountry(usr, pwd, host, db, options[1])
        elif (options[i] == "-update"):
            updateCountry(usr, pwd, host, db, options[1:])


def getCountryByCode(usr, pwd, host, db, code):
    cnx = mysql.connector.connect(user = usr, password = pwd, host = host, database = db)
    cursor = cnx.cursor()

    query = "SELECT * FROM countries WHERE code = '{}'".format(code)
    cursor.execute(query)
    result = cursor.fetchall()

    print(tabulate(result, headers=['code', 'name', 'area'], tablefmt='pretty'))

    cursor.close()
    cnx.close()

def getCountryByName(usr, pwd, host, db, name):
    cnx = mysql.connector.connect(user = usr, password = pwd, host = host, database = db)
    cursor = cnx.cursor()

    query = "SELECT * FROM countries WHERE name = '{}'".format(name)
    cursor.execute(query)
    result = cursor.fetchall()

    print(tabulate(result, headers=['code', 'name', 'area'], tablefmt='pretty'))

    cursor.close()
    cnx.close()

def getAllCountries(usr, pwd, host, db):
    cnx = mysql.connector.connect(user = usr, password = pwd, host = host, database = db)
    cursor = cnx.cursor()

    query = "SELECT * FROM countries"
    cursor.execute(query)
    result = cursor.fetchall()

    print(tabulate(result, headers=['code', 'name', 'area'], tablefmt='pretty'))

    cursor.close()
    cnx.close()

def insertCountry(usr, pwd, host, db, options):
    cnx = mysql.connector.connect(user = usr, password = pwd, host = host, database = db)
    cursor = cnx.cursor()

    query = "INSERT INTO countries(code, name, area) VALUES ('{0}', '{1}', '{2}')".format(options[0], options[1], options[2])
    cursor.execute(query)

    cnx.commit()
    cursor.close()
    cnx.close()

def deleteCountry(usr, pwd, host, db, code):
    cnx = mysql.connector.connect(user = usr, password = pwd, host = host, database = db)
    cursor = cnx.cursor()

    query = "DELETE FROM countries WHERE code = '{}'".format(code)
    cursor.execute(query)

    cnx.commit()
    cursor.close()
    cnx.close()

# def updateCountry(usr, pwd, host, db, options):
#     cnx = mysql.connector.connect(user = usr, password = pwd, host = host, database = db)
#     cursor = cnx.cursor()

#     code = options[0]
#     options.pop(0)
#     for i in range(len(options), 2):
#         query = "UPDATE countries SET" + str(options[i]) + "=" + str(options[i+1]) + \
#         "WHERE code = '{0}'".format(code)