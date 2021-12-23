import mysql.connector
import cmd_parser
import tables
from tabulate import tabulate

def operation(options, cnx):
    if (options[0] == "all"):
        get_all_feritility_rates(cnx)
    elif (options[0] == "get"):
        get_feritility_rates_by_options(cnx, options[1:])
    elif (options[0] == "get-range"):
        get_ferility_rates_in_range_by_options(cnx, options[1:])
    elif (options[0] == "add"):
        upsert_ferility_rates(cnx, options[1:])
    elif (options[0] == "delete"):
        delete_ferility_rates(cnx, options[1:])


def get_all_feritility_rates(cnx): 
    cursor = cnx.cursor()

    query = "SELECT * FROM fertility_rates"
    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        print(err) 
        print("Could not query, please check your command and try again or use help")
    result = cursor.fetchall()

    print(tabulate(result, headers=tables.fertilityRatesColumns, tablefmt='pretty'))

    cursor.close()

def get_feritility_rates_by_options(cnx, options): 
    cursor = cnx.cursor()
    options = cmd_parser.parse(options)

    query = "SELECT * FROM fertility_rates"
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

    print(tabulate(result, headers=tables.fertilityRatesColumns, tablefmt='pretty'))

    cursor.close()

def get_ferility_rates_in_range_by_options(cnx, options): 
    cursor = cnx.cursor()
    options = cmd_parser.parse(options)

    query = "SELECT * FROM fertility_rates"
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

    print(tabulate(result, headers=tables.fertilityRatesColumns, tablefmt='pretty'))

    cursor.close()

def upsert_ferility_rates(cnx, options):
    cursor = cnx.cursor()
    options = cmd_parser.parse(options)

    pre_query = "SELECT * FROM fertility_rates"
    if 'code' in options: 
        pre_query += " WHERE country_code = '" + options['code'] + "'"
    elif 'name' in options: 
        pre_query += " WHERE country_name = '" + options['name'] + "'"
    
    pre_query += " AND year = " + options['year']

    try:
        cursor.execute(pre_query)
    except mysql.connector.Error as err:
        print(err) 
        print("Could not query, please check your command and try again or use help")
    result = cursor.fetchall()
    empty = len(result) == 0

    qry = ""
    if empty: 
        print('inserting new data')
        if len(options) != len(tables.fertilityRatesColumns):
            print('Invalid number of arguments, try again')
            return
        
        qry = "INSERT INTO fertility_rates("
        for i, table in enumerate(tables.fertilityRatesColumns):
            if i != len(tables.fertilityRatesColumns) - 1: 
                qry += table + ','
            else: 
                qry += table + ')'
        
        qry += "VALUES('" + options['code'] + "','" + options['name'] + "'," + options['year'] + ",'" + options['gender'] + "'," + options['fertility_rate_15_19'] + "," + options['fertility_rate_15_19'] + "," + options['fertility_rate_15_19'] + "," + options['fertility_rate_15_19'] + "," + options['fertility_rate_15_19'] + "," + options['fertility_rate_15_19'] + "," + options['fertility_rate_15_19'] + "," + options['total_fertility_rate'] + "," + options['gross_reproduction_rate'] + "," + options['sex_ratio_at_birth'] + ")" 
                
                 
    else: 
        # update
        print('updating data')
        qry = "UPDATE fertility_rates SET "
        for i in options: 
            if i in ['code', 'name', 'year']: 
                continue

            qry += i + "=" + options[i] + ","
        # hacky way to get rid of last comma
        qry = qry[0:len(qry)-1]
        qry += " WHERE country_code = '" + options['code'] + "'" + " AND country_name = '" + options['name'] + "'" + " AND year = " + options['year']

    try:
        cursor.execute(qry)
    except mysql.connector.Error as err:
        print(err) 
        print("Could not query, please check your command and try again or use help")

    print("data successfully added")
    cnx.commit()
    cursor.close()

def delete_ferility_rates(cnx, options): 
    cursor = cnx.cursor()
    options = cmd_parser.parse(options)

    qry = "DELETE FROM fertility_rates"
    if 'code' in options: 
        qry += " WHERE country_code = '" + options['code'] + "'"
    elif 'name' in options: 
        qry += " WHERE country_name = '" + options['name'] + "'"
    
    qry += " AND year = " + options['year']  

    try:
        cursor.execute(qry)
    except mysql.connector.Error as err:
        print(err) 
        print("Could not query, please check your command and try again or use help")

    print("data successfully deleted")
    cnx.commit()
    cursor.close()


