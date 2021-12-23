import population

def population_tests(cnx):
    total_population_tests = 0
    tests_passed = 0

    # Test 1 : Get all entries in the population table
    if population.get_all_populations(cnx): 
        tests_passed += 1

    # Test 2 : Query population data for Canada by country code
    # We know that the dataset contains population information for Canada, so we expect this test to pass
    test_cmd = "population get -code CA" 
    if population.operation(test_cmd.split(" ")[1:], cnx): 
        tests_passed += 1

    # Test 3 : Query population data for United States by country name, year and gender
    # This tests if we obtain data for multiple input flags
    test_cmd = "population get -name United_States -year 2000 -gender F" 
    if population.operation(test_cmd.split(" ")[1:], cnx):
        tests_passed += 1

    print(str(tests_passed) + "/" + str(total_population_tests) + " population tests passed")

def run_tests(cnx): 
    population_tests(cnx)
