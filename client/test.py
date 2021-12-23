import population, birthDeath, infantMortality, lifeExpectancy, education, gni, hdi, gii, countries, fertility_rates

def population_tests(cnx):
    total_population_tests = 11
    tests_passed = 0

    # ----------------------------------------------------------------------
    # Tests for: population get
    # ----------------------------------------------------------------------
    # Test 1 : Get all entries in the population tables
    test_cmd = "population all"
    if population.operation(test_cmd.split(" ")[1:], cnx): 
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
    # Tests for: population delete
    # ----------------------------------------------------------------------
    # Test 11 : Deleting the entry created in Test 8 
    # The delete operation will return True if the deletion was successful
    test_cmd = "population delete -name Canada -year 2030 -gender M"
    if population.operation(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    print(str(tests_passed) + "/" + str(total_population_tests) + " population tests passed")

def birth_death_tests(cnx):
    total_birth_death_tests = 8
    tests_passed = 0

    # ----------------------------------------------------------------------
    # Tests for: birth_death all
    # ----------------------------------------------------------------------
    # Test 1 : Get all entries in the birth_death table
    test_cmd = "birth_death all"
    if birthDeath.bd(test_cmd.split(" ")[1:], cnx): 
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: birth_death get
    # ----------------------------------------------------------------------

    # Test 2 : Query birth_death data for Canada by country code
    # We know that the dataset contains birth_death information for Canada, so we expect this test to pass
    # The operation returns True if any rows are found
    test_cmd = "birth_death get -code CA" 
    if birthDeath.bd(test_cmd.split(" ")[1:], cnx): 
        tests_passed += 1

    # Test 3 : Query birth_death data for United States by country name, year 
    # This tests if we obtain data for multiple input flags
    # The operation returns True if any rows are found
    test_cmd = "birth_death get -name United_States -year 2011" 
    if birthDeath.bd(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # Test 4 : Query birth_death for a country that does not exist 
    # The operation returns False, if no rows are found, so we should expect a False return below
    test_cmd = "birth_death get -name University_of_Waterloo"
    if birthDeath.bd(test_cmd.split(" ")[1:], cnx) == False:
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: birth_death insert 
    # ----------------------------------------------------------------------
    
    # Test 5 : Insert birth_death data for Canada for the year 2030
    # This operation returns True if the insertion was successful
    test_cmd = "birth_death insert CA Canada 2030 53.6 76.8 4.6 0.25 4.36"
    if birthDeath.bd(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # Test 6 : A continuation of Test 5 to see if the new entry was actually inserted
    # We query the birth_death data for Canada in 2030 which should have been created in the previous test
    test_cmd = "birth_death get -code CA -year 2030"
    if birthDeath.bd(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1
    # ----------------------------------------------------------------------
    # Tests for: birth_death update
    # ----------------------------------------------------------------------
    # Test 7 : Update the growth_rate for Canada in the year 2030 
    # In this case, it would be the growth_rate value
    # The operation returns True if the update was successful
    test_cmd = "birth_death update -code CA -year 2030 -growth_rate 0.7"
    if birthDeath.bd(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: birth_death delete
    # ----------------------------------------------------------------------
    # Test 8 : Deleting the entry created in Test 5
    # The delete operation will return True if the deletion was successful
    test_cmd = "birth_death delete -code CA -year 2030"
    if birthDeath.bd(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    print(str(tests_passed) + "/" + str(total_birth_death_tests) + " birth_death tests passed")

def infant_mortality_tests(cnx):
    total_infant_mortality_tests = 8
    tests_passed = 0

    # ----------------------------------------------------------------------
    # Tests for: infant_mortality all
    # ----------------------------------------------------------------------
    # Test 1 : Get all entries in the infant_mortality table
    test_cmd = "infant_mortality all"
    if infantMortality.im(test_cmd.split(" ")[1:], cnx): 
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: infant_mortality get
    # ----------------------------------------------------------------------

    # Test 2 : Query infant_mortality data for Canada by country code
    # We know that the dataset contains infant_mortality information for Canada, so we expect this test to pass
    # The operation returns True if any rows are found
    test_cmd = "infant_mortality get -code CA" 
    if infantMortality.im(test_cmd.split(" ")[1:], cnx): 
        tests_passed += 1

    # Test 3 : Query infant_mortality data for United States by country name, year 
    # This tests if we obtain data for multiple input flags
    # The operation returns True if any rows are found
    test_cmd = "infant_mortality get -name United_States -year 2014" 
    if infantMortality.im(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # Test 4 : Query infant_mortality for a country that does not exist 
    # The operation returns False, if no rows are found, so we should expect a False return below
    test_cmd = "infant_mortality get -name University_of_Waterloo"
    if infantMortality.im(test_cmd.split(" ")[1:], cnx) == False:
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: infant_mortality insert 
    # ----------------------------------------------------------------------
    
    # Test 5 : Insert infant_mortality data for Canada for the year 2030
    # This operation returns True if the insertion was successful
    test_cmd = "infant_mortality insert CA Canada 2030 53.6 76.8 4.6"
    if infantMortality.im(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # Test 6 : A continuation of Test 5 to see if the new entry was actually inserted
    # We query the infant_mortality data for Canada in 2030 which should have been created in the previous test
    test_cmd = "infant_mortality get -code CA -year 2030"
    if infantMortality.im(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1
    # ----------------------------------------------------------------------
    # Tests for: infant_mortality update
    # ----------------------------------------------------------------------
    # Test 7 : Update the infant_mortality for Canada in the year 2030 
    # In this case, it would be the infant_mortality value
    # The operation returns True if the update was successful
    test_cmd = "infant_mortality update -code CA -year 2030 -infant_mortality 0.7"
    if infantMortality.im(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: infant_mortality delete
    # ----------------------------------------------------------------------
    # Test 8 : Deleting the entry created in Test 5
    # The delete operation will return True if the deletion was successful
    test_cmd = "infant_mortality delete -code CA -year 2030"
    if infantMortality.im(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    print(str(tests_passed) + "/" + str(total_infant_mortality_tests) + " infant_mortality tests passed")
    
def life_expectancy_tests(cnx):
    total_life_expectancy_tests = 8
    tests_passed = 0

    # ----------------------------------------------------------------------
    # Tests for: life_expectancy all
    # ----------------------------------------------------------------------
    # Test 1 : Get all entries in the life_expectancy table
    test_cmd = "life_expectancy all"
    if lifeExpectancy.le(test_cmd.split(" ")[1:], cnx): 
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: life_expectancy get
    # ----------------------------------------------------------------------

    # Test 2 : Query life_expectancy data for Canada by country code
    # We know that the dataset contains life_expectancy information for Canada, so we expect this test to pass
    # The operation returns True if any rows are found
    test_cmd = "life_expectancy get -code CA" 
    if lifeExpectancy.le(test_cmd.split(" ")[1:], cnx): 
        tests_passed += 1

    # Test 3 : Query life_expectancy data for United States by country name, year 
    # This tests if we obtain data for multiple input flags
    # The operation returns True if any rows are found
    test_cmd = "life_expectancy get -name United_States -year 2014" 
    if lifeExpectancy.le(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # Test 4 : Query life_expectancy for a country that does not exist 
    # The operation returns False, if no rows are found, so we should expect a False return below
    test_cmd = "life_expectancy get -name University_of_Waterloo"
    if lifeExpectancy.le(test_cmd.split(" ")[1:], cnx) == False:
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: life_expectancy insert 
    # ----------------------------------------------------------------------
    
    # Test 5 : Insert life_expectancy data for Canada for the year 2030
    # This operation returns True if the insertion was successful
    test_cmd = "life_expectancy insert CA Canada 2030 53.6 76.8 4.6"
    if lifeExpectancy.le(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # Test 6 : A continuation of Test 5 to see if the new entry was actually inserted
    # We query the life_expectancy data for Canada in 2030 which should have been created in the previous test
    test_cmd = "life_expectancy get -code CA -year 2030"
    if lifeExpectancy.le(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1
    # ----------------------------------------------------------------------
    # Tests for: life_expectancy update
    # ----------------------------------------------------------------------
    # Test 7 : Update the life_expectancy for Canada in the year 2030 
    # In this case, it would be the life_expectancy value
    # The operation returns True if the update was successful
    test_cmd = "life_expectancy update -code CA -year 2030 -life_expectancy 0.7"
    if lifeExpectancy.le(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: life_expectancy delete
    # ----------------------------------------------------------------------
    # Test 8 : Deleting the entry created in Test 5
    # The delete operation will return True if the deletion was successful
    test_cmd = "life_expectancy delete -code CA -year 2030"
    if lifeExpectancy.le(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    print(str(tests_passed) + "/" + str(total_life_expectancy_tests) + " life_expectancy tests passed")

def education_tests(cnx):
    total_education_tests = 8
    tests_passed = 0

    # ----------------------------------------------------------------------
    # Tests for: education all
    # ----------------------------------------------------------------------
    # Test 1 : Get all entries in the education table
    test_cmd = "education all"
    if education.education(test_cmd.split(" ")[1:], cnx): 
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: education get
    # ----------------------------------------------------------------------

    # Test 2 : Query education data for Canada by country code
    # We know that the dataset contains education information for Canada, so we expect this test to pass
    # The operation returns True if any rows are found
    test_cmd = "education get -code CA" 
    if education.education(test_cmd.split(" ")[1:], cnx): 
        tests_passed += 1

    # Test 3 : Query education data for United States by country name, year 
    # This tests if we obtain data for multiple input flags
    # The operation returns True if any rows are found
    test_cmd = "education get -name United_States -year 2014" 
    if education.education(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # Test 4 : Query education for a country that does not exist 
    # The operation returns False, if no rows are found, so we should expect a False return below
    test_cmd = "education get -name University_of_Waterloo"
    if education.education(test_cmd.split(" ")[1:], cnx) == False:
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: education insert 
    # ----------------------------------------------------------------------
    
    # Test 5 : Insert education data for Canada for the year 2030
    # This operation returns True if the insertion was successful
    test_cmd = "education insert CA Canada 2030 M 30"
    if education.education(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # Test 6 : A continuation of Test 5 to see if the new entry was actually inserted
    # We query the education data for Canada in 2030 which should have been created in the previous test
    test_cmd = "education get -code CA -year 2030"
    if education.education(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1
    # ----------------------------------------------------------------------
    # Tests for: education update
    # ----------------------------------------------------------------------
    # Test 7 : Update the education for Canada in the year 2030 
    # In this case, it would be the education value
    # The operation returns True if the update was successful
    test_cmd = "education update -code CA -year 2030 -gender M -years_of_schooling 0.7"
    if education.education(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: education delete
    # ----------------------------------------------------------------------
    # Test 8 : Deleting the entry created in Test 5
    # The delete operation will return True if the deletion was successful
    test_cmd = "education delete -code CA -year 2030 -gender M"
    if education.education(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    print(str(tests_passed) + "/" + str(total_education_tests) + " education tests passed")

def gni_tests(cnx):
    total_gni_tests = 8
    tests_passed = 0

    # ----------------------------------------------------------------------
    # Tests for: gni all
    # ----------------------------------------------------------------------
    # Test 1 : Get all entries in the gni table
    test_cmd = "gni all"
    if gni.gni(test_cmd.split(" ")[1:], cnx): 
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: gni get
    # ----------------------------------------------------------------------

    # Test 2 : Query gni data for Canada by country code
    # We know that the dataset contains gni information for Canada, so we expect this test to pass
    # The operation returns True if any rows are found
    test_cmd = "gni get -code CA" 
    if gni.gni(test_cmd.split(" ")[1:], cnx): 
        tests_passed += 1

    # Test 3 : Query gni data for United States by country name, year, gender
    # This tests if we obtain data for multiple input flags
    # The operation returns True if any rows are found
    test_cmd = "gni get -name United_States -year 2014 -gender M" 
    if gni.gni(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # Test 4 : Query gni for a country that does not exist 
    # The operation returns False, if no rows are found, so we should expect a False return below
    test_cmd = "gni get -name University_of_Waterloo"
    if gni.gni(test_cmd.split(" ")[1:], cnx) == False:
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: gni insert 
    # ----------------------------------------------------------------------
    
    # Test 5 : Insert gni data for Canada for the year 2030
    # This operation returns True if the insertion was successful
    test_cmd = "gni insert CA Canada 2030 M 32532.00"
    if gni.gni(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # Test 6 : A continuation of Test 5 to see if the new entry was actually inserted
    # We query the gni data for Canada in 2030 which should have been created in the previous test
    test_cmd = "gni get -code CA -year 2030"
    if gni.gni(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1
    # ----------------------------------------------------------------------
    # Tests for: gni update
    # ----------------------------------------------------------------------
    # Test 7 : Update the gni for Canada in the year 2030 
    # In this case, it would be the gni value
    # The operation returns True if the update was successful
    test_cmd = "gni update -code CA -year 2030 -gender M -gni 50000.0"
    if gni.gni(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: gni delete
    # ----------------------------------------------------------------------
    # Test 8 : Deleting the entry created in Test 5
    # The delete operation will return True if the deletion was successful
    test_cmd = "gni delete -code CA -year 2030 -gender M"
    if gni.gni(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    print(str(tests_passed) + "/" + str(total_gni_tests) + " gni tests passed")

def hdi_tests(cnx):
    total_hdi_tests = 8
    tests_passed = 0

    # ----------------------------------------------------------------------
    # Tests for: hdi all
    # ----------------------------------------------------------------------
    # Test 1 : Get all entries in the hdi table
    test_cmd = "hdi all"
    if hdi.hdi(test_cmd.split(" ")[1:], cnx): 
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: hdi get
    # ----------------------------------------------------------------------

    # Test 2 : Query hdi data for Canada by country code
    # We know that the dataset contains hdi information for Canada, so we expect this test to pass
    # The operation returns True if any rows are found
    test_cmd = "hdi get -code CA" 
    if hdi.hdi(test_cmd.split(" ")[1:], cnx): 
        tests_passed += 1

    # Test 3 : Query hdi data for United States by country name, year
    # This tests if we obtain data for multiple input flags
    # The operation returns True if any rows are found
    test_cmd = "hdi get -name United_States -year 2014" 
    if hdi.hdi(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # Test 4 : Query hdi for a country that does not exist 
    # The operation returns False, if no rows are found, so we should expect a False return below
    test_cmd = "hdi get -name University_of_Waterloo"
    if hdi.hdi(test_cmd.split(" ")[1:], cnx) == False:
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: hdi insert 
    # ----------------------------------------------------------------------
    
    # Test 5 : Insert hdi data for Canada for the year 2030
    # This operation returns True if the insertion was successful
    test_cmd = "hdi insert CA Canada 2030 0.70"
    if hdi.hdi(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # Test 6 : A continuation of Test 5 to see if the new entry was actually inserted
    # We query the hdi data for Canada in 2030 which should have been created in the previous test
    test_cmd = "hdi get -code CA -year 2030"
    if hdi.hdi(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1
    # ----------------------------------------------------------------------
    # Tests for: hdi update
    # ----------------------------------------------------------------------
    # Test 7 : Update the hdi for Canada in the year 2030 
    # In this case, it would be the hdi value
    # The operation returns True if the update was successful
    test_cmd = "hdi update -code CA -year 2030 -hdi 0.90"
    if hdi.hdi(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: hdi delete
    # ----------------------------------------------------------------------
    # Test 8 : Deleting the entry created in Test 5
    # The delete operation will return True if the deletion was successful
    test_cmd = "hdi delete -code CA -year 2030"
    if hdi.hdi(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    print(str(tests_passed) + "/" + str(total_hdi_tests) + " hdi tests passed")

def gii_tests(cnx):
    total_gii_tests = 8
    tests_passed = 0

    # ----------------------------------------------------------------------
    # Tests for: gii all
    # ----------------------------------------------------------------------
    # Test 1 : Get all entries in the gii table
    test_cmd = "gii all"
    if gii.gii(test_cmd.split(" ")[1:], cnx): 
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: gii get
    # ----------------------------------------------------------------------

    # Test 2 : Query gii data for Canada by country code
    # We know that the dataset contains gii information for Canada, so we expect this test to pass
    # The operation returns True if any rows are found
    test_cmd = "gii get -code CA" 
    if gii.gii(test_cmd.split(" ")[1:], cnx): 
        tests_passed += 1

    # Test 3 : Query gii data for United States by country name, year
    # This tests if we obtain data for multiple input flags
    # The operation returns True if any rows are found
    test_cmd = "gii get -name United_States -year 2014" 
    if gii.gii(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # Test 4 : Query gii for a country that does not exist 
    # The operation returns False, if no rows are found, so we should expect a False return below
    test_cmd = "gii get -name University_of_Waterloo"
    if gii.gii(test_cmd.split(" ")[1:], cnx) == False:
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: gii insert 
    # ----------------------------------------------------------------------
    
    # Test 5 : Insert gii data for Canada for the year 2030
    # This operation returns True if the insertion was successful
    test_cmd = "gii insert CA Canada 2030 0.70"
    if gii.gii(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # Test 6 : A continuation of Test 5 to see if the new entry was actually inserted
    # We query the gii data for Canada in 2030 which should have been created in the previous test
    test_cmd = "gii get -code CA -year 2030"
    if gii.gii(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1
    # ----------------------------------------------------------------------
    # Tests for: gii update
    # ----------------------------------------------------------------------
    # Test 7 : Update the gii for Canada in the year 2030 
    # In this case, it would be the gii value
    # The operation returns True if the update was successful
    test_cmd = "gii update -code CA -year 2030 -gii 0.90"
    if gii.gii(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: gii delete
    # ----------------------------------------------------------------------
    # Test 8 : Deleting the entry created in Test 5
    # The delete operation will return True if the deletion was successful
    test_cmd = "gii delete -code CA -year 2030"
    if gii.gii(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    print(str(tests_passed) + "/" + str(total_gii_tests) + " gii tests passed")

def country_tests(cnx):

    total_country_tests = 8
    tests_passed = 0

    # ----------------------------------------------------------------------
    # Tests for: country all
    # ----------------------------------------------------------------------
    # Test 1 : Get all entries in the country table
    test_cmd = "country all"
    if countries.country(test_cmd.split(" ")[1:], cnx): 
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: country get
    # ----------------------------------------------------------------------

    # Test 2 : Query country data for Canada by country code
    # We know that the dataset contains country information for Canada, so we expect this test to pass
    # The operation returns True if any rows are found
    test_cmd = "country get -code CA" 
    if countries.country(test_cmd.split(" ")[1:], cnx): 
        tests_passed += 1

    # Test 3 : Query country data for United States by country name
    # This tests if we obtain data for multiple input flags
    # The operation returns True if any rows are found
    test_cmd = "country get -name United_States" 
    if countries.country(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # Test 4 : Query a country that does not exist 
    # The operation returns False, if no rows are found, so we should expect a False return below
    test_cmd = "country get -name University_of_Waterloo"
    if countries.country(test_cmd.split(" ")[1:], cnx) == False:
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: country insert 
    # ----------------------------------------------------------------------
    
    # Test 5 : Insert country data for Test_Country 
    # This operation returns True if the insertion was successful
    test_cmd = "country insert ZZ Test_Country 10000.0"
    if countries.country(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # Test 6 : A continuation of Test 5 to see if the new entry was actually inserted
    # We query the Test_Country with country code which should have been created in the previous test
    test_cmd = "country get -code ZZ"
    if countries.country(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1
    # ----------------------------------------------------------------------
    # Tests for: country update
    # ----------------------------------------------------------------------
    # Test 7 : Update the area for Test_Country 
    # The operation returns True if the update was successful
    test_cmd = "country update -code ZZ -area 99999.0"
    if countries.country(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: country delete
    # ----------------------------------------------------------------------
    # Test 8 : Deleting the entry created in Test 5
    # The delete operation will return True if the deletion was successful
    test_cmd = "country delete -code ZZ"
    if countries.country(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    print(str(tests_passed) + "/" + str(total_country_tests) + " country tests passed")

def fertility_rates_tests(cnx):
    total_fertility_rates_tests = 8
    tests_passed = 0

    # ----------------------------------------------------------------------
    # Tests for: fertility_rates get
    # ----------------------------------------------------------------------
    # Test 1 : Get all entries in the fertility_rates tables
    test_cmd = "fertility_rates all"
    if fertility_rates.operation(test_cmd.split(" ")[1:], cnx): 
        tests_passed += 1

    # Test 2 : Query fertility_rates data for Canada by country code
    # We know that the dataset contains fertility_rates information for Canada, so we expect this test to pass
    # The operation returns True if any rows are found
    test_cmd = "fertility_rates get -code CA" 
    if fertility_rates.operation(test_cmd.split(" ")[1:], cnx): 
        tests_passed += 1

    # Test 3 : Query fertility_rates data for United States by country name, year and gender
    # This tests if we obtain data for multiple input flags
    # The operation returns True if any rows are found
    test_cmd = "fertility_rates get -name United_States -year 2014" 
    if fertility_rates.operation(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # Test 4 : Query fertility_rates for a country that does not exist 
    # The operation returns False, if no rows are found, so we should expect a False return below
    test_cmd = "fertility_rates get -name University_of_Waterloo"
    if fertility_rates.operation(test_cmd.split(" ")[1:], cnx) == False:
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: fertility_rates get-range
    # ----------------------------------------------------------------------
    # Test 5 : Query fertility_rates data for a given range of years
    # The data for Canada exists in the table, so we expect this to be true
    test_cmd = "fertility_rates get-range -name Canada -start_year 2000 -end_year 2005" 
    if fertility_rates.operation(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # Test 6 : Query fertility_rates data for range of years that don't exist
    # There is no data for Canada's fertility_rates between the years 2030 and 2040, so we should expect a False return from the operation
    test_cmd = "fertility_rates get-range -name Canada -start_year 2030 -end_year 2040" 
    if fertility_rates.operation(test_cmd.split(" ")[1:], cnx) == False:
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: fertility_rates add
    # ----------------------------------------------------------------------
    # Test 7 : Update the fertility_rate_15_19 for Canada in the year 2000 
    # The operation returns True if the update was successful
    test_cmd = "fertility_rates add -code CA -name Canada -year 2000 -fertility_rate_15_19 100"
    if fertility_rates.operation(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    # ----------------------------------------------------------------------
    # Tests for: fertility_rates delete
    # ----------------------------------------------------------------------
    # Test 8 : Deleting the entry created in Test 8 
    # The delete operation will return True if the deletion was successful
    test_cmd = "fertility_rates delete -name Canada -year 2030"
    if fertility_rates.operation(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    print(str(tests_passed) + "/" + str(total_fertility_rates_tests) + " fertility_rates tests passed")

def run_tests(cnx, suite):
    if suite == "population": 
        population_tests(cnx)
    elif suite == "birth_death":
        birth_death_tests(cnx)
    elif suite == "infant_mortality":
        infant_mortality_tests(cnx)
    elif suite == "life_expectancy":
        life_expectancy_tests(cnx)
    elif suite == "education":
        education_tests(cnx)
    elif suite == "gni":
        gni_tests(cnx)
    elif suite == "hdi":
        hdi_tests(cnx)
    elif suite == "gii":
        gii_tests(cnx)
    elif suite == "country":
        country_tests(cnx)
    elif suite == "fertility_rates":
        fertility_rates_tests(cnx)
    else:
        print("Incorrect use of the test command.")

