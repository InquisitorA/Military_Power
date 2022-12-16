

CREATE TABLE IF NOT EXISTS army{
    army_id int NOT NULL,
    combat_tanks int NOT NULL,
    armored_fighters int NOT NULL,
    self_propelled_artillery int NOT NULL,
    towered_artillery int NOT NULL,
    rocket_projectors int NOT NULL,
    CONSTRAINT army_key PRIMARY KEY (army_id)

};

CREATE TABLE IF NOT EXISTS navy{
    navy_id int NOT NULL,
    naval_assets int NOT NULL,
    aircraft_carriers int NOT NULL,
    frigates int NOT NULL,
    destroyers int NOT NULL,
    corvettes int NOT NULL,
    submarines int NOT NULL,
    patrol_crafts int NOT NULL,
    warfare_vessels int NOT NULL,
    CONSTRAINT navy_key PRIMARY KEY (navy_id)


};

CREATE TABLE IF NOT EXISTS airforce{

    airforce_id int NOT NULL,
    aircraft_rank int NOT NULL,
    aircrafts int NOT NULL,
    fighter_aircrafts int NOT NULL,
    attack_aircrafts int NOT NULL,
    transport_aircrafts int NOT NULL,
    trainer_aircrafts int NOT NULL,
    helicopters int NOT NULL,
    attack_helicopters int NOT NULL,
    CONSTRAINT airforce_key PRIMARY KEY (airforce_id)

  

};


CREATE TABLE IF NOT EXISTS economy{
    economy_id int NOT NULL,
    defence_budget bigint NOT NULL,
    external_debt bigint NOT NULL,
    forex bigint NOT NULL,
    purchasing_power bigint NOT NULL,
    gdp bigint NOT NULL,
    CONSTRAINT economy_key PRIMARY KEY (economy_id)  

};


CREATE TABLE IF NOT EXISTS manpower{

    manpower_id int NOT NULL,    
    population bigint NOT NULL,
    man_power_available bigint NOT NULL,
    fit_for_service bigint NOT NULL,
    reaching_military_age bigint NOT NULL,
    military_power bigint NOT NULL,
    active_personnel bigint NOT NULL,
    reserve_personnel bigint NOT NULL,
    CONSTRAINT manpower_key PRIMARY KEY (manpower_id)

  

};

CREATE TABLE IF NOT EXISTS geography{
    geography_id int NOT NULL,
    land_area bigint NOT NULL,
    coastline_length bigint NOT NULL,
    shared_border bigint NOT NULL,
    waterway bigint NOT NULL,
    CONSTRAINT geography_key PRIMARY KEY (geography_id)

  

};


CREATE TABLE IF NOT EXISTS country{
    id int NOT NULL,
    country_name text NOT NULL,
    iso3 text NOT NULL,
    iso2 text NOT NULL,
    capital text NOT NULL,
    currency text NOT NULL,
    region text NOT NULL,
    subregion text NOT NULL,
    fire_power_rank int NOT NULL,
    army_id int,
    navy_id int,
    airforce_id int,
    economy_id int,
    manpower_id int,
    geography_id int,
    CONSTRAINT country_key PRIMARY KEY (country_code),
    CONSTRAINT army_ref FOREIGN KEY (army_id) references army(army_id),
    CONSTRAINT navy_ref FOREIGN KEY (navy_id) references navy(navy_id),
    CONSTRAINT airforce_ref FOREIGN KEY (airforce_id) references airforce(airforce_id),
    CONSTRAINT economy_ref FOREIGN KEY (economy_id) references economy(economy_id),
    CONSTRAINT manpower_ref FOREIGN KEY (manpower_id) references manpower(manpower_id),
    CONSTRAINT geography_ref FOREIGN KEY (geography_id) references geography(geography_id)

};


CREATE TABLE IF NOT EXISTS states{
    id int NOT NULL,
    name text NOT NULL,
    country_id int,
    country_code int,
    state_code text NOT NULL,
    
    CONSTRAINT state_key PRIMARY KEY (id),
    CONSTRAINT country_ref_first FOREIGN KEY (country_id) references country(id),
    CONSTRAINT country_ref_second FOREIGN KEY (country_code) references country(iso2),
};



CREATE TABLE IF NOT EXISTS cities{
    id int NOT NULL,
    name text NOT NULL,
    state_id int,
    state_code text,
    country_id text,
    country_code text,
    CONSTRAINT city_key PRIMARY KEY (id),
    CONSTRAINT country_ref_first FOREIGN KEY (country_id) references country(id),
    CONSTRAINT country_ref_second FOREIGN KEY (country_code) references country(iso2),
    CONSTRAINT state_ref_first FOREIGN KEY (state_id) references states(id),
    CONSTRAINT state_ref_second FOREIGN KEY (state_code) references states(state_code),

};

