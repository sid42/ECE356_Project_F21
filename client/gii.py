import mysql.connector
from tabulate import tabulate
import tables

def gii(options, cnx):
    if (options[0] == "all"):
        getAllGII(cnx)
    elif (options[0] == "insert"):
        insertCountryGII(cnx, options[1:])
    elif (options[0] == "delete"):
        deleteCountryGII(cnx, options[1:])
    elif (options[0] == "update"):
        updateCountryGII(cnx, options[1:])
    elif options[0] == "get":
        getCountryGII(cnx, options[1:])

def getAllGII(cnx):
    cursor = cnx.cursor()

    query = "SELECT * FROM gender_inequality_index"
    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        print(err) 
        print("Could not query, please check your command and try again or use help")
    result = cursor.fetchall()

    print(tabulate(result, headers=tables.GIIColumns, tablefmt='pretty'))

    cursor.close()

def getCountryGII(cnx, options):
    cursor = cnx.cursor()

    if len(options) < 2 or len(options) > 8:
        print("Not enough or too many arguements for a get operation. Please check your command and try again")
        return

    query_start = "SELECT * FROM gender_inequality_index WHERE "
    substring = []
    for i in range(0, len(options), 2):
        if options[i][1:] == "name":
            substring.append("country_name" + " = '" + str(options[i+1]) + "'")
        elif options[i][1:] == "code":
            substring.append("country_code" + " = '" + str(options[i+1]) + "'")
        else:
            substring.append(options[i][1:] + " = '" + str(options[i+1]) + "'")
        
    
    if len(substring) == 1:
        query = query_start + substring[0]
    else:
        query = query_start
        for i in range(len(substring)-1):
            substring[i] += "AND "
        for j in range(len(substring)):
            query += substring[j]

    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        print(err) 
        print("Could not query, please check your command and try again or use help")
    result = cursor.fetchall()

    print(tabulate(result, headers=tables.GIIColumns, tablefmt='pretty'))

    cursor.close()


def insertCountryGII(cnx, options):
    cursor = cnx.cursor()

    if len(options) != 4:
        print("Not enough or too many arguements for an insert operation. Please check your command and try again")
        return

    query = "INSERT INTO gender_inequality_index(country_code, country_name, year, gii) \
        VALUES ('{0}', '{1}', '{2}', '{3}')".format(options[0], options[1], options[2], options[3])
    try:
        cursor.execute(query)
        print("Insertion query executed successfully")
    except mysql.connector.Error as err:
        print(err) 
        print("Could not insert, please check your command and try again or use help")

    cnx.commit()
    cursor.close()


def updateCountryGII(cnx, options):
    cursor = cnx.cursor()

    if len(options) < 5 or len(options) > 8:
        print("Not enough or too many arguements for an update operation. Please check your command and try again")
        return

    query_start = "UPDATE gender_inequality_index SET "
    pre_substring = []
    for i in range(4, len(options), 2):
        if options[i][1:] == "name":
            pre_substring.append("country_name" + " = '" + str(options[i+1]) + "'")
        else:
            pre_substring.append(str(options[i][1:]) + " = '" + str(options[i+1]) + "'")
    
    post_substring = []
    for i in range(0, 4, 2):
        if options[i][1:] == "code":
            post_substring.append("country_code" + " = '" + str(options[i+1]) + "'")
        else:
            post_substring.append(options[i][1:] + " = '" + str(options[i+1]) + "'")
    

    if len(pre_substring) == 1:
        query = query_start + pre_substring[0]
    else:
        query = query_start
        for i in range(len(pre_substring)-1):
            pre_substring[i] += ", "
        for j in range(len(pre_substring)):
            query += pre_substring[j]
    
    
    query += " WHERE "
    for i in range(len(post_substring)-1):
        post_substring[i] += " AND "
    for j in range(len(post_substring)):
        query += post_substring[j]

    try:
        cursor.execute(query)
        print("Updation query executed successfully")
    except mysql.connector.Error as err:
        print(err) 
        print("Could not update, please check your command and try again or use help")

    cnx.commit()
    cursor.close()

def deleteCountryGII(cnx, options):
    cursor = cnx.cursor()

    if len(options) != 4:
        print("Not enough arguements for an delete operation. Please check your command and try again")
        return

    query_start = "DELETE FROM gender_inequality_index WHERE "
    
    substring = []
    for i in range(0, len(options), 2):
        if options[i][1:] == "code":
            substring.append("country_code" + " = '" + str(options[i+1]) + "'")
        else:
            substring.append(options[i][1:] + " = '" + str(options[i+1]) + "'")
    

    if len(substring) == 1:
        query = query_start + substring[0]
    else:
   
        query = query_start 
        for i in range(len(substring)-1):
            substring[i] += " AND "
        for j in range(len(substring)):
            query += substring[j]

    try:
        cursor.execute(query)
        print("Deletion query executed successfully")
    except mysql.connector.Error as err:
        print(err) 
        print("Could not delete, please check your command and try again or use help")

    cnx.commit()
    cursor.close()
