import mysql.connector
import cmd_parser
import tables
from tabulate import tabulate

def operation(options, cnx):
    if (options[0] == "all"):
        get_all_populations(cnx)
    elif (options[0] == "get"):
        get_population_by_options(cnx, options[1:])
    elif (options[0] == "get-range"):
        get_population_in_range_by_options(cnx, options[1:])
    elif (options[0] == "add"):
        upsert_population(cnx, options[1:])
    elif (options[0] == "delete"):
        delete_population(cnx, options[1:])


def get_all_populations(cnx): 
    cursor = cnx.cursor()

    query = "SELECT * FROM population"
    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        print(err) 
        print("Could not query, please check your command and try again or use help")
    result = cursor.fetchall()

    print(tabulate(result, headers=tables.populationColumns, tablefmt='pretty'))

    cursor.close()

# population get -country_code CA -year 2000
# population get -country_name Canada -year 2000
# population get -country_name CA 
def get_population_by_options(cnx, options): 
    cursor = cnx.cursor()
    options = cmd_parser.parse(options)

    query = "SELECT * FROM population"
    if 'code' in options: 
        query += " WHERE country_code = '" + options['code'] + "'"
    elif 'name' in options: 
        query += " WHERE country_name = '" + options['name'] + "'"
    else: 
        print('invalid input')
        return

    if 'year' in options: 
        query += " AND year = " + options['year'] + " ORDER BY year DESC"

    print(query)
    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        print(err) 
        print("Could not query, please check your command and try again or use help")
    result = cursor.fetchall()

    print(tabulate(result, headers=tables.populationColumns, tablefmt='pretty'))

    cursor.close()

# population get-range -country_code CA -start_year 2000 -end_year 2005
def get_population_in_range_by_options(cnx, options): 
    cursor = cnx.cursor()
    options = cmd_parser.parse(options)

    query = "SELECT * FROM population"
    if 'code' in options: 
        query += " WHERE country_code = '" + options['code'] + "'"
    elif 'name' in options: 
        query += " WHERE country_name = '" + options['name'] + "'"

    query += " AND year > " + options['start_year'] + " AND year < " + options['end_year'] + " ORDER BY year DESC"

    print(query)
    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        print(err) 
        print("Could not query, please check your command and try again or use help")
    result = cursor.fetchall()

    print(tabulate(result, headers=tables.populationColumns, tablefmt='pretty'))

    cursor.close()

def upsert_population(cnx, options):
    cursor = cnx.cursor()
    options = cmd_parser.parse(options)

    pre_query = "SELECT * FROM population"
    if 'code' in options: 
        pre_query += " WHERE country_code = '" + options['code'] + "'"
    elif 'name' in options: 
        pre_query += " WHERE country_name = '" + options['name'] + "'"
    
    pre_query += " AND year = " + options['year'] + " AND gender = '" options['gender']

    try:
        cursor.execute(pre_query)
    except mysql.connector.Error as err:
        print(err) 
        print("Could not query, please check your command and try again or use help")
    result = cursor.fetchall()
    # check if we need to insert or update
    empty = len(result) == 0

    qry = ""
    if empty: 
        print('inserting new data')
        if len(options) != len(tables.populationColumns):
            print('Invalid number of arguments, try again')
            return
        
        qry = "INSERT INTO population("
        for i, table in enumerate(tables.populationColumns):
            if i != len(tables.populationColumns) - 1: 
                qry += table + ','
            else: 
                qry += table + ')'
        
        qry += "VALUES('" + options['code'] + "','" + options['name'] + "'," + options['year'] + ",'" + options['gender'] + "'," + options['total_midyear_population'] + "," + options['population_between_0_10'] + "," + options['population_between_11_20'] + "," + options['population_between_21_30'] + "," + options['population_between_31_40'] + "," + options['population_between_41_50'] + "," + options['population_between_51_60'] + "," + options['population_between_61_70'] + "," + options['population_between_71_80'] + "," + options['population_between_81_90'] + "," + options['population_between_91_100'] + ")" 
                
                 
    else: 
        # update
        print('updating data')
        qry = "UPDATE population SET "
        for i in options: 
            if i in ['code', 'name', 'year', 'gender']: 
                continue

            qry += i + "=" + options[i] + ","
        # hacky way to get rid of last comma
        qry = qry[0:len(qry)-1]
        qry += " WHERE country_code = '" + options['code'] + "'" + " AND country_name = '" + options['name'] + "'" + " AND year = " + options['year'] + " AND gender = '" + options['gender'] + "'"

    try:
        cursor.execute(qry)
    except mysql.connector.Error as err:
        print(err) 
        print("Could not query, please check your command and try again or use help")

    print("data successfully added")
    cnx.commit()
    cursor.close()

def delete_population(cnx, options): 
    cursor = cnx.cursor()
    options = cmd_parser.parse(options)

    qry = "DELETE FROM population"
    if 'code' in options: 
        qry += " WHERE country_code = '" + options['code'] + "'"
    elif 'name' in options: 
        qry += " WHERE country_name = '" + options['name'] + "'"
    
    qry += " AND year = " + options['year'] + " AND gender = '" + options['gender'] + "'"

    try:
        cursor.execute(qry)
    except mysql.connector.Error as err:
        print(err) 
        print("Could not query, please check your command and try again or use help")

    print("data successfully deleted")
    cnx.commit()
    cursor.close()


