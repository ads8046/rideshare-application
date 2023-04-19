-- We specify our primary key here to be as repeatable as possible
-- INSERT INTO example_table(id, foo) VALUES
--   (1, 'hello, world!');


INSERT INTO rideshare_drivers (driver_id, first_name, last_name, rating, mobile_number, special_instructions, is_available, zip_code, available_at)
        VALUES (1, 'Jane', 'Doe', 5, '4553737', 'have a fun ride', True, '14647', '2023-02-26 15:45:30'),
              (2, 'Mary', 'Dion', 3.2, '5954853737', 'drop me at the mall', True, '55632', '2023-02-26 15:45:30'),
              (3, 'Tom', 'Magliozzi', 3.5, '5964853657', 'Dont drive like my brother', True, '55632', '2023-02-26 15:45:30'),
              (4, 'Jon', 'Snow', 4.9, '5964853657', 'winter is coming, get the chains out', True, '44632', '2023-02-27 17:45:30');

INSERT INTO rides (ride_id, driver_id, start_point, destination, ride_ts, cost)
        VALUES (1, 4, '31.6', '51.6', '2023-02-26 15:45:30', 14.50),
              (2, 4, '5.5.5', '7.7.7', '2023-05-26 15:45:30', 23.95),
              (3, 1, '5.5.5', '7.7.7', '2023-06-26 15:45:30', 53.45);

INSERT INTO riders (rider_id, first_name, last_name, rating, mobile_number, special_instructions, is_available, zip_code, available_at)
        VALUES (2, 'Daisy', 'Werthan', 4.8, '404-555-1212', 'Rider', True, '30301', '1989-12-12 11:00:00'),
        (1, 'Vladimir', 'Rider', 4.0, '555-5678', 'Waiting for Godot', True, '90210', '2023-02-27 10:15:00');
-- Restart our primary key sequences here so inserting id=DEFAULT won't collide
-- ALTER SEQUENCE example_table_id_seq RESTART 1000;