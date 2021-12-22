import mysql.connector
import getpass
from tabulate import tabulate
import getpass

def country(options, cnx):
    for i in range(len(options)): 
        if (options[i] == "-code"):
            getCountryByCode(cnx, options[1])
        elif (options[i] == "-name"):
            getCountryByName(cnx, options[1])
        elif (options[i] == "-all"):
            getAllCountries(cnx)
        elif (options[i] == "-insert"):
            insertCountry(cnx, options[1:])
        elif (options[i] == "-delete"):
            deleteCountry(cnx, options[1])
        elif (options[i] == "-update"):
            updateCountry(cnx, options[1:])


def getCountryByCode(cnx, code):
    # cnx = mysql.connector.connect(user = usr, password = pwd, host = host, database = db)
    cursor = cnx.cursor()

    query = "SELECT * FROM countries WHERE code = '{}'".format(code)
    cursor.execute(query)
    result = cursor.fetchall()

    print(tabulate(result, headers=['code', 'name', 'area'], tablefmt='pretty'))

    cursor.close()

def getCountryByName(cnx, name):
    # cnx = mysql.connector.connect(user = usr, password = pwd, host = host, database = db)
    cursor = cnx.cursor()

    query = "SELECT * FROM countries WHERE name = '{}'".format(name)
    cursor.execute(query)
    result = cursor.fetchall()

    print(tabulate(result, headers=['code', 'name', 'area'], tablefmt='pretty'))

    cursor.close()

def getAllCountries(cnx):
    # cnx = mysql.connector.connect(user = usr, password = pwd, host = host, database = db)
    cursor = cnx.cursor()

    query = "SELECT * FROM countries"
    cursor.execute(query)
    result = cursor.fetchall()

    print(tabulate(result, headers=['code', 'name', 'area'], tablefmt='pretty'))

    cursor.close()

def insertCountry(cnx, options):
    # cnx = mysql.connector.connect(user = usr, password = pwd, host = host, database = db)
    cursor = cnx.cursor()

    query = "INSERT INTO countries(code, name, area) VALUES ('{0}', '{1}', '{2}')".format(options[0], options[1], options[2])
    cursor.execute(query)

    cnx.commit()
    cursor.close()

def deleteCountry(cnx, code):
    # cnx = mysql.connector.connect(user = usr, password = pwd, host = host, database = db)
    cursor = cnx.cursor()

    query = "DELETE FROM countries WHERE code = '{}'".format(code)
    cursor.execute(query)

    cnx.commit()
    cursor.close()

# def updateCountry(usr, pwd, host, db, options):
#     cnx = mysql.connector.connect(user = usr, password = pwd, host = host, database = db)
#     cursor = cnx.cursor()

#     code = options[0]
#     options.pop(0)
#     for i in range(len(options), 2):
#         query = "UPDATE countries SET" + str(options[i]) + "=" + str(options[i+1]) + \
#         "WHERE code = '{0}'".format(code)