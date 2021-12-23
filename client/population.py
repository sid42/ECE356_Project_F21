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

def get_population_by_options(cnx, options): 

def get_population_in_range_by_options(cnx, options): 

def upsert_population(cnx, options):

def delete_population(cnx, options): 
