-- =====================================================
-- Test 1 : Test UNIQUE constraint in the countries table
-- =====================================================
-- Should not be able to add a new country with a unique country code but same name to another country in the table
-- We know that Canada already exists in the countries table with country_code CA, so the following query should fail
INSERT INTO countries(code, name, area) VALUES('ZZ', 'Canada', 50); 

-- =====================================================
-- Test 2 : EXPLAIN ANALYZE to test that indexes exist for all tables
-- =====================================================
-- Should be index scans for all following queries
EXPLAIN ANALYZE SELECT * FROM countries WHERE country_code = 'CA'; 
EXPLAIN ANALYZE SELECT * FROM population WHERE country_code = 'CA' AND year < 2016; 
EXPLAIN ANALYZE SELECT * FROM infant_mortality WHERE country_code = 'CA' AND year < 2016;
EXPLAIN ANALYZE SELECT * FROM fertility_rates WHERE country_code = 'CA' AND year < 2016;
EXPLAIN ANALYZE SELECT * FROM human_development_index WHERE country_code = 'CA' AND year < 2016;
EXPLAIN ANALYZE SELECT * FROM gender_inequality_index WHERE country_code = 'CA' AND year < 2016;
EXPLAIN ANALYZE SELECT * FROM gross_national_income_by_gender WHERE country_code = 'CA' AND year < 2016;
EXPLAIN ANALYZE SELECT * FROM education WHERE country_code = 'CA' AND year < 2016;
EXPLAIN ANALYZE SELECT * FROM birth_death_rates WHERE country_code = 'CA' AND year < 2016;

-- =====================================================
-- Test 3 : Test Foreign Key Constraint on weak entity tables 
-- =====================================================
-- This should fail as there is no country in the countries table with country_code of ZZ
-- This is due to the foreign key on country_code referencing the ciountry_code in countries table
-- This constraint applies to all entities except countries
INSERT INTO human_development_index(country_code, country_name, year, hdi) VALUES('ZZ', 'Canada', 2010, 10)