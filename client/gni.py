import mysql.connector
from tabulate import tabulate
import tables

def gni(options, cnx):
    if (options[0] == "all"):
        getAllGNI(cnx)
    elif (options[0] == "insert"):
        insertCountryGNI(cnx, options[1:])
    elif (options[0] == "delete"):
        deleteCountryGNI(cnx, options[1:])
    elif (options[0] == "update"):
        updateCountryGNI(cnx, options[1:])
    elif options[0] == "get":
        getCountryGNI(cnx, options[1:])

def getAllGNI(cnx):
    cursor = cnx.cursor()

    query = "SELECT * FROM gross_national_income_by_gender"
    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        print(err) 
        print("Could not query, please check your command and try again or use help")
    result = cursor.fetchall()

    print(tabulate(result, headers=tables.GNIColumns, tablefmt='pretty'))

    cursor.close()

def getCountryGNI(cnx, options):
    cursor = cnx.cursor()

    if len(options) < 2 or len(options) > 10 :
        print("Not enough or too many arguements for a get operation. Please check your command and try again")
        return

    query_start = "SELECT * FROM gross_national_income_by_gender WHERE "
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

    print(tabulate(result, headers=tables.GNIColumns, tablefmt='pretty'))

    cursor.close()


def insertCountryGNI(cnx, options):
    cursor = cnx.cursor()

    if len(options) != 5:
        print("Not enough or too many arguements for an insert operation. Please check your command and try again")
        return

    query = "INSERT INTO gross_national_income_by_gender(country_code, country_name, year, gender, gni) \
        VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')".format(options[0], options[1], options[2], options[3], options[4])
    try:
        cursor.execute(query)
        print("Insertion query executed successfully")
    except mysql.connector.Error as err:
        print(err) 
        print("Could not insert, please check your command and try again or use help")

    cnx.commit()
    cursor.close()


def updateCountryGNI(cnx, options):
    cursor = cnx.cursor()

    if len(options) < 6 or len(options) > 10:
        print("Not enough or too many arguements for an update operation. Please check your command and try again")
        return

    query_start = "UPDATE gross_national_income_by_gender SET "
    pre_substring = []
    for i in range(6, len(options), 2):
        if options[i][1:] == "name":
            pre_substring.append("country_name" + " = '" + str(options[i+1]) + "'")
        else:
            pre_substring.append(str(options[i][1:]) + " = '" + str(options[i+1]) + "'")
    
    post_substring = []
    for i in range(0, 6, 2):
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

def deleteCountryGNI(cnx, options):
    cursor = cnx.cursor()

    if len(options) != 6:
        print("Not enough arguements for an delete operation. Please check your command and try again")
        return

    query_start = "DELETE FROM gross_national_income_by_gender WHERE "
    
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

