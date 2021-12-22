import mysql.connector
from tabulate import tabulate

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
    cursor = cnx.cursor()

    query = "SELECT * FROM countries WHERE code = '{}'".format(code)
    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        print(err) 
        print("Could not query, please check your command and try again or use help")
    result = cursor.fetchall()

    print(tabulate(result, headers=['code', 'name', 'area'], tablefmt='pretty'))

    cursor.close()

def getCountryByName(cnx, name):
    cursor = cnx.cursor()

    query = "SELECT * FROM countries WHERE name = '{}'".format(name)
    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        print(err) 
        print("Could not query, please check your command and try again or use help")
    result = cursor.fetchall()

    print(tabulate(result, headers=['code', 'name', 'area'], tablefmt='pretty'))

    cursor.close()

def getAllCountries(cnx):
    
    cursor = cnx.cursor()

    query = "SELECT * FROM countries"
    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        print(err) 
        print("Could not query, please check your command and try again or use help")
    result = cursor.fetchall()

    print(tabulate(result, headers=['code', 'name', 'area'], tablefmt='pretty'))

    cursor.close()

def insertCountry(cnx, options):
    cursor = cnx.cursor()

    query = "INSERT INTO countries(code, name, area) VALUES ('{0}', '{1}', '{2}')".format(options[0], options[1], options[2])
    try:
        cursor.execute(query)
        print("Insertion query executed successfully")
    except mysql.connector.Error as err:
        print(err) 
        print("Could not insert, please check your command and try again or use help")

    cnx.commit()
    cursor.close()

def deleteCountry(cnx, code):
    cursor = cnx.cursor()

    query = "DELETE FROM countries WHERE code = '{}'".format(code)
    try:
        cursor.execute(query)
        print("Deletion query executed successfully")
    except mysql.connector.Error as err:
        print(err) 
        print("Could not delete, please check your command and try again or use help")

    cnx.commit()
    cursor.close()

def updateCountry(cnx, options):
    cursor = cnx.cursor()

    code = options.pop(0)
    query_start = "UPDATE countries SET "
    query_end = " WHERE code = '{0}'".format(code)
    substring = []
    for i in range(0, len(options), 2):
        substring.append(str(options[i][2:]) + " = '" + str(options[i+1]) + "'")
    

    if len(substring) == 1:
        query = query_start + substring[0] + query_end
    else:
        query = query_start
        for i in range(len(substring)-1):
            substring[i] += ", "
        for j in range(len(substring)):
            query += substring[j]
        query += query_end
        
    try:
        cursor.execute(query)
        print("Updation query executed successfully")
    except mysql.connector.Error as err:
        print(err) 
        print("Could not update, please check your command and try again or use help")

    cnx.commit()
    cursor.close()
        