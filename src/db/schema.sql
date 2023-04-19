DROP TABLE IF EXISTS passengers;
DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS rides;
DROP TABLE IF EXISTS riders;
DROP TABLE IF EXISTS rideshare_drivers;
DROP TABLE IF EXISTS ride_riders;


CREATE TABLE rideshare_drivers (
    driver_id             INTEGER      NOT NULL PRIMARY KEY,
    first_name            VARCHAR(55)  NOT NULL,
    last_name             VARCHAR(55)  NOT NULL,
    rating                NUMERIC      NOT NULL,
    mobile_number         VARCHAR(15)  NOT NULL,
    special_instructions  VARCHAR(255),
    is_available          BOOLEAN,
    zip_code              VARCHAR(5)   NOT NULL,
    available_at          TIMESTAMP
);

CREATE TABLE riders (
    rider_id              INTEGER      NOT NULL PRIMARY KEY,
    first_name            VARCHAR(55)  NOT NULL,
    last_name             VARCHAR(55)  NOT NULL,
    rating                NUMERIC,
    mobile_number         VARCHAR(15)  NOT NULL,
    special_instructions  VARCHAR(255),
    is_available          BOOLEAN,
    zip_code              VARCHAR(5)   NOT NULL,
    available_at          TIMESTAMP
);

-- CREATE TABLE rides (
--     ride_id               SERIAL       NOT NULL PRIMARY KEY,
--     driver_id             INTEGER      NOT NULL,
--     start_point           VARCHAR(60),
--     destination           VARCHAR(60),
--     ride_ts               TIMESTAMP,
--     cost                  NUMERIC
-- );

CREATE TABLE rides (
    ride_id               SERIAL     NOT NULL PRIMARY KEY,
    driver_id             INTEGER,
    rider_id              INTEGER,
    start_point           VARCHAR(60),
    destination           VARCHAR(60),
    ride_ts               TIMESTAMP,
    cost                  NUMERIC
);

CREATE TABLE ride_riders (
    ride_id INTEGER NOT NULL,
    rider_id INTEGER NOT NULL,
    cost NUMERIC
);