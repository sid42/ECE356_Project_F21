import population

def population_tests(cnx):
    total_population_tests = 11
    tests_passed = 0

    # ----------------------------------------------------------------------
    # Tests for: population get
    # ----------------------------------------------------------------------
    # Test 1 : Get all entries in the population table
    if population.get_all_populations(cnx): 
        tests_passed += 1

    # Test 2 : Query population data for Canada by country code
    # We know that the dataset contains population information for Canada, so we expect this test to pass
    # The operation returns True if any rows are found
    test_cmd = "population get -code CA" 
    if population.operation(test_cmd.split(" ")[1:], cnx): 
        tests_passed += 1

    # Test 3 : Query population data for United States by country name, year and gender
    # This tests if we obtain data for multiple input flags
    # The operation returns True if any rows are found
    test_cmd = "population get -name United_States -year 2000 -gender F" 
    if population.operation(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # Test 4 : Query population for a country that does not exist 
    # The operation returns False, if no rows are found, so we should expect a False return below
    test_cmd = "population get -name University_of_Waterloo"
    if population.operation(test_cmd.split(" ")[1:], cnx) == False:
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: population get-range
    # ----------------------------------------------------------------------
    # Test 5 : Query population data for a given range of years
    # The data for Canada exists in the table, so we expect this to be true
    test_cmd = "population get-range -name Canada -start_year 2000 -end_year 2005" 
    if population.operation(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # Test 6 : Query population data for range of years that don't exist
    # There is no data for Canada's population between the years 2030 and 2040, so we should expect a False return from the operation
    test_cmd = "population get-range -name Canada -start_year 2030 -end_year 2040" 
    if population.operation(test_cmd.split(" ")[1:], cnx) == False:
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: population add
    # ----------------------------------------------------------------------
    # Test 7 : Update the female population_between_0_10 for Canada in the year 2000 
    # We can update the value of a single row by providing all the primary key values (country_code, country_name, year, gender) to locate the row to be updated followed the value we want to update
    # In this case, it would be the total_midyear_population value
    # The operation returns True if the update was successful
    test_cmd = "population add -code CA -name Canada -year 2000 -gender F -population_between_0_10 100"
    if population.operation(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # Test 8 : Insert population data for Canada for the year 2030
    # We can use the 'add' command to also insert to new data into the table, as it essentially functions as an upsert
    # This operation returns True if the insertion was successful
    test_cmd = "population add -code CA -name Canada -year 2030 -gender M -total_midyear_population 30 -population_between_0_10 30 -population_between_11_20 30 -population_between_21_30 30 -population_between_31_40 30 -population_between_41_50 30 -population_between_51_60 30 -population_between_61_70 30 -population_between_71_80 30 -population_between_81_90 30 -population_between_91_100 30"
    if population.operation(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # Test 9 : A continuation of Test 8 to see if the new entry was actually inserted
    # We query the population data for Canada in 2030 which should have been created in the previous test
    test_cmd = "population get -code CA -year 2030"
    if population.operation(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # Test 10 : Inserting a new row which violates the foreign key constaint
    # If we try to add a country with a code that does not exist in the countries table, we should encounter an error
    # This is because the country code in the population table is a foreign key referencing the country code in the countries table
    # The country code ZZ does not exist in the country table 
    test_cmd = "population add -code ZZ -name Canada -year 2030 -gender M -total_midyear_population 30 -population_between_0_10 30 -population_between_11_20 30 -population_between_21_30 30 -population_between_31_40 30 -population_between_41_50 30 -population_between_51_60 30 -population_between_61_70 30 -population_between_71_80 30 -population_between_81_90 30 -population_between_91_100 30"
    if population.operation(test_cmd.split(" ")[1:], cnx) == False:
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: population add
    # ----------------------------------------------------------------------
    # Test 11 : Deleting the entry created in Test 8 
    # The delete operation will return True if the deletion was successful
    test_cmd = "population delete -name Canada -year 2030 -gender M"
    if population.operation(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    print(str(tests_passed) + "/" + str(total_population_tests) + " population tests passed")

def run_tests(cnx, suite):
    if suite == "population": 
        population_tests(cnx)
