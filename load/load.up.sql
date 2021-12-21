-- ================================================================================

-- load countries data
CREATE TABLE IF NOT EXISTS countries (
    code    CHAR(2),
    name    VARCHAR(255), 
    area    DECIMAL(20,2),
    PRIMARY KEY (code)
);

LOAD DATA INFILE '/var/lib/mysql-files/22-Demographics/country_names_area.csv' 
INTO TABLE countries
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
-- ================================================================================

-- ================================================================================

-- load population table
CREATE TABLE IF NOT EXISTS population (
    country_code                CHAR(2),
    country_name                VARCHAR(255), 
    year                        INT, 
    gender                      CHAR(1), 
    total_midyear_population    INT, 
    population_between_0_10     INT, 
    population_between_11_20    INT, 
    population_between_21_30    INT, 
    population_between_31_40    INT, 
    population_between_41_50    INT, 
    population_between_51_60    INT, 
    population_between_61_70    INT, 
    population_between_71_80    INT, 
    population_between_81_90    INT, 
    population_between_91_100   INT,
    PRIMARY KEY (country_code, year, gender) 
);

LOAD DATA INFILE '/var/lib/mysql-files/Group35/population.csv' 
INTO TABLE population
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- ================================================================================

-- ================================================================================

-- load infant mortality data
CREATE TABLE IF NOT EXISTS infant_mortality (
    country_code                CHAR(2),
    country_name                VARCHAR(255), 
    year                        INT, 
    infant_mortality            DECIMAL(20,2), 
    infant_mortality_male       DECIMAL(20,2), 
    infant_mortality_female     DECIMAL(20,2),
    PRIMARY KEY (country_code, year)
);

LOAD DATA INFILE '/var/lib/mysql-files/Group35/infant_mortality.csv' 
INTO TABLE infant_mortality
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- ================================================================================

-- ================================================================================

-- load fertility data
CREATE TABLE IF NOT EXISTS fertility_rates (
    country_code                CHAR(2),
    country_name                VARCHAR(255), 
    year                        INT, 
    fertility_rate_15_19        DECIMAL(20,2), 
    fertility_rate_20_24        DECIMAL(20,2), 
    fertility_rate_25_29        DECIMAL(20,2),     
    fertility_rate_30_34        DECIMAL(20,2), 
    fertility_rate_35_39        DECIMAL(20,2),
    fertility_rate_40_44        DECIMAL(20,2),
    fertility_rate_45_49        DECIMAL(20,2),
    total_fertility_rate        DECIMAL(20,2), 
    gross_reproduction_rate     DECIMAL(20,2), 
    sex_ratio_at_birth          DECIMAL(20,2),
    PRIMARY KEY (country_code, year)
); 

LOAD DATA INFILE '/var/lib/mysql-files/22-Demographics/age_specific_fertility_rates.csv' 
INTO TABLE fertility_rates
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- ================================================================================

-- ================================================================================

-- load birth death rates
CREATE TABLE IF NOT EXISTS birth_death_rates (
    country_code                CHAR(2),
    country_name                VARCHAR(255), 
    year                        INT, 
    crude_birth_rate            DECIMAL(20,2), 
    crude_death_rate            DECIMAL(20,2), 
    net_migration               DECIMAL(20,2), 
    rate_natural_increase       DECIMAL(20,2), 
    growth_rate                 DECIMAL(20,2), 
    PRIMARY KEY (country_code, year)
);

LOAD DATA INFILE '/var/lib/mysql-files/22-Demographics/birth_death_growth_rates.csv' 
INTO TABLE birth_death_rates
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- ================================================================================

-- ================================================================================

-- load life expectancy
CREATE TABLE IF NOT EXISTS life_expectancy (
    country_code                CHAR(2),
    country_name                VARCHAR(255), 
    year                        INT, 
    life_expectancy             DECIMAL(20,2), 
    life_expectancy_male        DECIMAL(20,2), 
    life_expectancy_female      DECIMAL(20,2),
    PRIMARY KEY (country_code, year)
);

LOAD DATA INFILE '/var/lib/mysql-files/Group35/life_expectancy.csv' 
INTO TABLE life_expectancy
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- ================================================================================

-- ================================================================================

-- load gross national income by gender by year
CREATE TABLE IF NOT EXISTS gross_national_income_by_gender (
    country_code                CHAR(2), 
    country_name                VARCHAR(255), 
    year                        INT, 
    gender                      CHAR(1), 
    gni                         DECIMAL(20,2), 
    PRIMARY KEY (country_code, year, gender)
);

LOAD DATA INFILE '/var/lib/mysql-files/Group35/gni.csv' 
INTO TABLE gross_national_income_by_gender
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- ================================================================================

-- ================================================================================

-- load human development index
CREATE TABLE IF NOT EXISTS human_development_index (
    country_code                CHAR(2), 
    country_name                VARCHAR(255), 
    year                        INT, 
    hdi                         DECIMAL(20,2), 
    PRIMARY KEY (country_code, year)
);

LOAD DATA INFILE '/var/lib/mysql-files/Group35/hdi.csv' 
INTO TABLE human_development_index
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(country_code, country_name, year, @vhdi)
SET hdi = NULLIF(@vhdi, '');

-- ================================================================================

-- ================================================================================

-- load gender inequality index
CREATE TABLE IF NOT EXISTS gender_inequality_index (
    country_code                CHAR(2), 
    country_name                VARCHAR(255), 
    year                        INT, 
    gii                         DECIMAL(20,2), 
    PRIMARY KEY (country_code, year)
);

LOAD DATA INFILE '/var/lib/mysql-files/Group35/gie.csv' 
INTO TABLE gender_inequality_index
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(country_code, country_name, year, @vgii)
SET gii = NULLIF(@vgii, '');

-- ================================================================================

-- ================================================================================

-- load education data
CREATE TABLE IF NOT EXISTS education (
    country_code                CHAR(2), 
    country_name                VARCHAR(255), 
    year                        INT,
    gender                      CHAR(1), 
    years_of_schooling          DECIMAL(20,2), 
    PRIMARY KEY (country_code, year, gender)
);

LOAD DATA INFILE '/var/lib/mysql-files/Group35/education.csv' 
INTO TABLE education
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(country_code, country_name, year, gender, @vyears_of_schooling)
SET years_of_schooling = NULLIF(@vyears_of_schooling, '');

-- ================================================================================