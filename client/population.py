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
    if 'country_code' in options: 
        query += " WHERE country_code = '" + options['country_code'] + "'"
    elif 'country_name' in options: 
        query += " WHERE country_name = '" + options['country_name'] + "'"
    else: 
        print('invalid input')
        return

    if 'year' in options: 
        query += " AND year = " + options['year']

    print(query)
    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        print(err) 
        print("Could not query, please check your command and try again or use help")
    result = cursor.fetchall()

    print(tabulate(result, headers=tables.populationColumns, tablefmt='pretty'))

    cursor.close()

def get_population_in_range_by_options(cnx, options): 
    print()

def upsert_population(cnx, options):
    print()

def delete_population(cnx, options): 
    print()
