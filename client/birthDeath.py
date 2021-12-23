import mysql.connector
from tabulate import tabulate
import tables

def bd(options, cnx):
    for i in range(len(options)):
        if (i%2 == 0):
            options[i] = options[i].replace("_", " ")
            
    if (options[0] == "all"):
        return getAllBD(cnx)
    elif (options[0] == "insert"):
        return insertCountryBD(cnx, options[1:])
    elif (options[0] == "delete"):
        return deleteCountryBD(cnx, options[1:])
    elif (options[0] == "update"):
        return updateCountryBD(cnx, options[1:])
    elif (options[0] == "get"):
        return getCountryBD(cnx, options[1:])


def getAllBD(cnx):
    cursor = cnx.cursor()

    query = "SELECT * FROM birth_death_rates"
    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        print(err) 
        print("Could not query, please check your command and try again or use help")
        return False

    result = cursor.fetchall()
    if len(result) == 0: 
        return False

    print(tabulate(result, headers=tables.birthDeathRatesColumns, tablefmt='pretty'))

    cursor.close()
    return True

def getCountryBD(cnx, options):
    cursor = cnx.cursor()

    if len(options) < 2 or len(options) > 16 :
        print("Not enough or too many arguements for a get operation. Please check your command and try again")
        return

    query_start = "SELECT * FROM birth_death_rates WHERE "
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
        return False
    
    result = cursor.fetchall()
    if len(result) == 0: 
        return False

    print(tabulate(result, headers=tables.birthDeathRatesColumns, tablefmt='pretty'))

    cursor.close()
    return True

def insertCountryBD(cnx, options):
    cursor = cnx.cursor()

    if len(options) != 8:
        print("Not enough or too many arguements for an insert operation. Please check your command and try again")
        return

    query = "INSERT INTO birth_death_rates(country_code, country_name, year, crude_birth_rate, crude_death_rate, net_migration, rate_natural_increase, growth_rate) \
        VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')".format(options[0], options[1], options[2], options[3], options[4], options[5], options[6], options[7])
    try:
        cursor.execute(query)
        print("Insertion query executed successfully")
    except mysql.connector.Error as err:
        print(err) 
        print("Could not insert, please check your command and try again or use help")
        return False

    cnx.commit()
    cursor.close()
    return True

def updateCountryBD(cnx, options):
    cursor = cnx.cursor()

    if len(options) < 6 or len(options) > 16:
        print("Not enough or too many arguements for an update operation. Please check your command and try again")
        return

    query_start = "UPDATE birth_death_rates SET "
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
        return False

    cnx.commit()
    cursor.close()
    return True

def deleteCountryBD(cnx, options):
    cursor = cnx.cursor()

    if len(options) != 4:
        print("Not enough arguements for an delete operation. Please check your command and try again")
        return

    query_start = "DELETE FROM birth_death_rates WHERE "
    
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
        return False

    cnx.commit()
    cursor.close()
    return True