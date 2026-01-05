create database crime ;
use crime ;

CREATE TABLE crimedetail(
    case_id VARCHAR(50) PRIMARY KEY,
    crime_year INT NOT NULL,
    crime_month INT NOT NULL,
    crime_day INT NOT NULL,
    crime_time_slot VARCHAR(50),
    zone VARCHAR(50),
    police_station VARCHAR(100),
    area_type VARCHAR(50),
    population_density int ,
    festival_season TINYINT,
	prior_criminal_record TINYINT,
    victim_age INT,
    victim_gender VARCHAR(10),
    crime_type VARCHAR(100)
    
);
select * from crimedetail;
delete from crimedetail where case_id = 'Case ID: JPR-2026-0105';
select * from crimedetail;





