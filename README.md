Repo for group 35's ECE 356 final project

# Setup 

Please run `server/load.up.sql` in your preferred database and on your preferred host (preferably marmoset4) before attempting to run the client application. 
This will load all relevant tables along with their data, primary keys, foreign keys, constraints and indexes into the database. 

# Running the client app

To run the client application, please type: 
```
python3 main.py <your_host> <your_db>
```
For example, if the hose is marmoset04 and the data was loaded onto the database called db356_s34bhatt: 
```
python3 main.py marmoset04.shoshin.uwaterloo.ca db356_s34bhatt
```

# Commands and operations 
Please look at the test cases (test.py) if there is confusion on how to run the commands

Welcome to Group 35 Demographics Application!

These are the basic commands that you can use:

help
    Use this command for more information on other commands

NOTE: For all commands below, use "_" in place of " " when providing a value for the -name flag/attribute
E.g. : United States -> United_States, Saint Lucia -> Saint_Lucia
        : country get -name Virgin_Islands_U.S.

### test

To test the functionality of the commands, type in 'test' followed by one of the following operations (eg. test population)

    population 
    gni 
    hdi
    infant_mortality
    life_expectancy
    education 
    birth_death
    gii 
    fertility_rates
    country 


### country 
The following commands allow the user to query and update all the country information
Attributes: code, name, area
NOTE: PK for country: code

    country all -> To show all data present in the country table
    country get -<attribute> <value> ... -> To show specific information from country table by filtering on given attribute values
        NOTE: There can be multiple attribute-value pairs e.g. : country get -code ZZ -name Sample
    country insert <value> <value> ... -> To insert a row in the table using the values specified
        NOTE: The values should be in the order of the table's attributes  e.g. : country insert ZZ Sample 9999.0
    country update -<attribute> <value> ... -> To update the attributes of a specific row identified by Primary Key
        e.g. : country update -code ZZ -name New_Sample
    country delete -<attribute> <value> ... -> To delete a row in the table using the values specified identified by Primary Key
        e.g. : country delete -code ZZ             

### education
The following commands allow the user to query and update all the education information by country, namely years of schooling
Attributes: country_code, country_name, year, gender, years_of_schooling
NOTE: PK for education: country_code, year, gender

    education all -> To show all data present in the education table
    education get -<attribute> <value> ... -> To show specific information from education table by filtering on given attribute values
        NOTE: There can be multiple attribute-value pairs e.g. : education get -code ZZ -year 1990 -gender M
    education insert <value> <value> ... -> To insert a row in the table using the values specified
        NOTE: The values should be in the order of the table's attributes e.g. : education insert ZZ Sample 1999 F 7.9
    education update -<attribute> <value> ... -> To update the attributes of a specific row identified by Primary Key
        e.g. : education update -code ZZ -year 2015 -gender M -years_of_schooling 6.9
    education delete -<attribute> <value> ... -> To delete a row in the table using the values specified identified by Primary Key
        e.g. : education delete -code  -year 2015 -gender M

### population
The following commands allow the user to query and update all the population information for a country
Attributes: country_code, country_name, year, gender, total_midyear_population, population_between_0_10, population_between_11_20, population_between_21_30, population_between_31_40
population_between_41_50, population_between_51_60, population_between_61_70, population_between_71_80, population_between_81_90, population_between_91_100
NOTE: PK for population: country_code, year, gender

    population all -> get all data in the population table
    population get -<attribute> <value> ... -> get population value by attribute, must include either code or name 
        eg. population get -code CA 
            population get -name Canada -year 2000 
            population get -name Canada -year 2000 -gender F
    population get-range -<attribute> <value> ... -start_year <start_year_value> -end_year <end_year_value> -> get population for a specific range of years
        eg. population get-range -code CA -start_year 2000 -end_year 2005
            population get-range -name Canada -gender F -start_year 2000 -end_year 2005
    population add: (please look at test.py for example) -> add or insert population data, functions like an upsert, all PK values need to be specified in the command 
        eg. population add -code CA -year  2000 -gender F -total_midyear_population 1000
    population delete: delete population data by PKs
        eg. population delete -code CA -year 2000 -gender F

### fertility_rates
The following commands allow the user to query and update all relevant information about fertility rates for a country
Attributes: country_code, country_name, year, gender, total_fertility_rates, gross_reproduction_rate, sex_ratio_at_birth, fertility_rate_15_19, fertility_rate_20_24,
fertility_rate_25_29, fertility_rate_30_34, fertility_rate_35_39, fertility_rate_40_44, fertility_rate_45_49
NOTE: PK for fertility_rates: country_code, year

    fertility_rates all -> get all data in the fertility table
    fertility_rates get -<attribute> <value> ... -> get fertility value by attribute, must include either code or name 
        eg. fertility_rates get -code CA 
            fertility_rates get -name Canada -year 2000 
    fertility_rates get-range -<attribute> <value> ... -start_year <start_year_value> -end_year <end_year_value> -> get fertility_rates for a specific range of years
        eg. fertility_rates get-range -code CA -start_year 2000 -end_year 2005
    fertility_rates add: (please look at test.py for example) -> add or insert fertility_rates data, functions like an upsert, all PK values need to be specified in the command 
        eg. fertility_rates add -code CA -year  2000 -total_fertility_rate 10
    fertility_rates delete: delete fertility_rates data by PKs
        eg. fertility_rates delete -code CA -year 2000 

### life_expectancy
The following commands allow the user to query and update all the relevant life expectancy details based on country
Attributes: country_code, country_name, year, life_expectancy, life_expectancy_male, life_expectancy_female
NOTE: PK for life_expectancy: country_code, year

    life_expectancy all -> To show all data present in the life_expectancy table
    life_expectancy get -<attribute> <value> ... -> To show specific information from life_expectancy table by filtering on given attribute values
        NOTE: There can be multiple attribute-value pairs e.g. : life_expectancy get -code ZZ -year 1990 
    life_expectancy insert <value> <value> ... -> To insert a row in the table using the values specified
        NOTE: The values should be in the order of the table's attributes e.g. : life_expectancy insert ZZ Sample 1999 F 79 80 81
    life_expectancy update -<attribute> <value> ... -> To update the attributes of a specific row identified by Primary Key
        e.g. : life_expectancy update -code ZZ -year 2015 -gender M -life_expecatancy 69
    life_expectancy delete -<attribute> <value> ... -> To delete a row in the table using the values specified identified by Primary Key
        e.g. : life_expectancy delete -code  -year 2015

### infant_mortality
The following commands allow the user to query and update all the infant mortality data of the country
Attributes: country_code, country_name, year, gender, infant_mortality, infant_mortality_male, infant_mortality_female
NOTE: PK for infant_mortality: country_code, year

    infant_mortality all -> To show all data present in the infant_mortality table
    infant_mortality get -<attribute> <value> ... -> To show specific information from infant_mortality table by filtering on given attribute values
        NOTE: There can be multiple attribute-value pairs e.g. : infant_mortality get -code ZZ -year 1990 
    infant_mortality insert <value> <value> ... -> To insert a row in the table using the values specified
        NOTE: The values should be in the order of the table's attributes e.g. : infant_mortality insert ZZ Sample 1999 F 79 80 81
    infant_mortality update -<attribute> <value> ... -> To update the attributes of a specific row identified by Primary Key
        e.g. : life_expectancy update -code ZZ -year 2015 -gender M -infant_mortality 0.9
    infant_mortality delete -<attribute> <value> ... -> To delete a row in the table using the values specified identified by Primary Key
        e.g. : infant_mortality delete -code  -year 2015

### birth_death
The following commands allow the user to query and update all the relevant birth and death rate information of a country
Attributes: country_code, country_name, year, crude_birth_rate, crude_death_rate, net_migration, rate_natural_increase, growth_rate
NOTE: PK for birth_death: country_code, year

    birth_death all -> To show all data present in the birth_death table
    birth_death get -<attribute> <value> ... -> To show specific information from birth_death table by filtering on given attribute values
        NOTE: There can be multiple attribute-value pairs e.g. : birth_death get -code ZZ -year 1990 
    birth_death insert <value> <value> ... -> To insert a row in the table using the values specified
        NOTE: The values should be in the order of the table's attributes e.g. : birth_death insert ZZ Sample 1999 F 51.88 26.84 -1.45 3.15 3.22
    birth_death update -<attribute> <value> ... -> To update the attributes of a specific row identified by Primary Key
        e.g. : birth_death update -code ZZ -year 2015 -crude_birth_rate 52.56
    birth_death delete -<attribute> <value> ... -> To delete a row in the table using the values specified identified by Primary Key
        e.g. : birth_death delete -code ZZ -year 2015

### gni
The following commands allow the user to query and update all the gross national income data of the country
Attributes: country_code, country_name, year, gender, gni
NOTE: PK for gni: country_code, year, gender

    gni all -> To show all data present in the gni table
    gni get -<attribute> <value> ... -> To show specific information from gni table by filtering on given attribute values
        NOTE: There can be multiple attribute-value pairs e.g. : gni get -code ZZ -year 1990
    gni insert <value> <value> ... -> To insert a row in the table using the values specified
        NOTE: The values should be in the order of the table's attributes e.g. : gni insert ZZ Sample 1999 F 1000.0
    gni update -<attribute> <value> ... -> To update the attributes of a specific row identified by Primary Key
        e.g. : gni update -code ZZ -year 2015 -gender M -gni 1000.0
    gni delete -<attribute> <value> ... -> To delete a row in the table using the values specified identified by Primary Key
        e.g. : gni delete -code ZZ -year 2015 -gender M

### hdi
The following commands allow the user to query and update all the human development index of the country
Attributes: country_code, country_name, year, hdi
NOTE: PK for hdi: country_code, year

    hdi all -> To show all data present in the hdi table
    hdi get -<attribute> <value> ... -> To show specific information from hdi table by filtering on given attribute values
        NOTE: There can be multiple attribute-value pairs e.g. : hdi get -code ZZ -year 1990
    hdi insert <value> <value> ... -> To insert a row in the table using the values specified
        NOTE: The values should be in the order of the table's attributes e.g. : hdi insert ZZ Sample 1999 0.58
    hdi update -<attribute> <value> ... -> To update the attributes of a specific row identified by Primary Key
        e.g. : hdi update -code ZZ -year 2015 -hdi 0.43
    hdi delete -<attribute> <value> ... -> To delete a row in the table using the values specified identified by Primary Key
        e.g. : hdi delete -code ZZ -year 2015 


### gii
The following commands allow the user to query and update all the gender inequality index data of the country
Attributes: country_code, country_name, year, gii
NOTE: PK for gii: country_code, year

    gii all -> To show all data present in the gii table
    gii get -<attribute> <value> ... -> To show specific information from gii table by filtering on given attribute values
        NOTE: There can be multiple attribute-value pairs e.g. : gii get -code ZZ -year 1995
    gii insert <value> <value> ... -> To insert a row in the table using the values specified
        NOTE: The values should be in the order of the table's attributes e.g. : gii insert ZZ Sample 1999 0.58 
    gii update -<attribute> <value> ... -> To update the attributes of a specific row identified by Primary Key
        e.g. : gii update -code ZZ -year 2015 -gii 0.43
    
### exit
To exit/quit the final command line interface 
