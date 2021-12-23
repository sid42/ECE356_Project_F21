import os

def help():
    print(
        '''
        Welcome to Group 35 Demographics Application!

        These are the basic commands that you can use:

        help
            Use this command for more information on other commands
        
        NOTE: For all commands below, use "_" in place of " " when providing a value for the -name flag/attribute
        E.g. : United States -> United_States, Saint Lucia -> Saint_Lucia
             : country get -name Virgin_Islands_U.S.

        country
            NOTE: PK for country: code

            country all -> To show all data present in the country table
            country get -<attribute> <value> ... -> To show specific information from country table by filtering on given attribute values
                NOTE: There can be multiple attribute-value pairs e.g. : country get -code ZZ -name Sample
            country insert <value> <value> ... -> To insert a row in the table using the values specified
                NOTE: The values should be in the order of the table's attributes (code, name, area) e.g. : country insert ZZ Sample 9999.0
            country update -<attribute> <value> ... -> To update the attributes of a specific row identified by Primary Key
                e.g. : country update -code ZZ -name New_Sample
            country delete -<attribute> <value> ... -> To delete a row in the table using the values specified identified by Primary Key
                e.g. : country delete -code ZZ
                

        education
        population
        fertility_rates
        life_expectancy
        infant_mortality
        birth_death
        gni
        hdi
        gii
        exit

        To find further details about each command, use help -<command>

        '''
    )