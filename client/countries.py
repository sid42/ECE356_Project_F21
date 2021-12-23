import mysql.connector
from tabulate import tabulate
import tables

def country(options, cnx):
    if (options[0] == "all"):
        getAllCountries(cnx)
    elif (options[0] == "insert"):
        insertCountry(cnx, options[1:])
    elif (options[0] == "delete"):
        deleteCountry(cnx, options[2])
    elif (options[0] == "update"):
        updateCountry(cnx, options[1:])
    elif (options[0] == "get"):
        getCountry(cnx, options[1:])



def getAllCountries(cnx):
    
    cursor = cnx.cursor()

    query = "SELECT * FROM countries"
    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        print(err) 
        print("Could not query, please check your command and try again or use help")
    result = cursor.fetchall()

    print(tabulate(result, headers=tables.countriesColumns, tablefmt='pretty'))

    cursor.close()

def getCountry(cnx, options):
    cursor = cnx.cursor()

    if options[0] == "-code":
        query_end = " WHERE code = '{}'".format(options[1])
    elif (options[0] == "-name"):
        query_end = " WHERE name = '{}'".format(options[1])
    elif (options[0] == "all"):
        query_end = ""
    
    query = "SELECT * FROM countries" + query_end

    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        print(err) 
        print("Could not query, please check your command and try again or use help")
    result = cursor.fetchall()

    print(tabulate(result, headers=tables.countriesColumns, tablefmt='pretty'))

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

    if len(options) < 4 or len(options) > 6:
        print("Not enough or too many arguements for an update operation. Please check your command and try again")
        return

    query_start = "UPDATE countries SET "
    query_end = " WHERE code = '{0}'".format(options[1])
    substring = []
    for i in range(2, len(options), 2):
        substring.append(str(options[i][1:]) + " = '" + str(options[i+1]) + "'")
    

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
        