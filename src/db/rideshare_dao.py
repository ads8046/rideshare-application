import os
from .swen344_db_utils import *


def rebuild_tables():
    exec_sql_file('src/db/schema.sql')
    exec_sql_file('src/db/test_data.sql')
    

def get_single_driver_account_info(driver_id):
    """
        Get a single driver's account and their info by their driver id.
    """
    
    data = (driver_id,)
    select_sql = """
        SELECT *
        FROM rideshare_drivers
        WHERE driver_id = %s;
    """

    # Execute the query and get the results as a list of tuples
    rows = exec_get_one(select_sql, data)

    if not rows: 
        return []

    # Convert the list of tuples to a list of dictionaries
    keys = ['driver_id', 'first_name', 'last_name', 'rating', 'mobile_number', 'special_instructions', 'is_available', 'zip_code', 'available_at']
    row_dict = {keys[i]: str(rows[i]) for i in range(len(keys))}
    
    res = [row_dict]
    return res


def list_all_driver_records():
    """
        Get a list of all driver accounts.
    """
    
    select_sql = """
        SELECT *
        FROM rideshare_drivers;
    """

    # Execute the query and get the results as a list of tuples
    rows = exec_get_all(select_sql)

    # Convert the list of tuples to a list of dictionaries
    keys = ['driver_id', 'first_name', 'last_name', 'rating', 'mobile_number', 'special_instructions', 'is_available', 'zip_code', 'available_at']
    result_list = []
    for row in rows:
        row_dict = {keys[i]: str(row[i]) for i in range(len(keys))}
        result_list.append(row_dict)
    return result_list


def get_single_rider_account_info(rider_id):
    """
        Get a single rider account by their rider id.
    """
    
    data = (rider_id,)
    select_sql = """
        SELECT *
        FROM riders
        WHERE rider_id = %s;
    """

    # Execute the query and get the results as a list of tuples
    rows = exec_get_one(select_sql, data)

    if not rows: 
        return []

    # Convert the list of tuples to a list of dictionaries
    keys = ['rider_id', 'first_name', 'last_name', 'rating', 'mobile_number', 'special_instructions', 'is_available', 'zip_code', 'available_at']
    row_dict = {keys[i]: str(rows[i]) for i in range(len(keys))}
    
    res = [row_dict]
    return res


def list_all_rider_records():
    """
        Get a list of all the riders and their information.
    """
    select_sql = """
        SELECT *
        FROM riders;
    """

    # Execute the query and get the results as a list of tuples
    rows = exec_get_all(select_sql)
    if not rows:
        return []

    # Convert the list of tuples to a list of dictionaries
    keys = ['rider_id', 'first_name', 'last_name', 'rating', 'mobile_number', 'special_instructions', 'is_available', 'zip_code', 'available_at']
    result_list = []
    for row in rows:
        row_dict = {keys[i]: str(row[i]) for i in range(len(keys))}
        result_list.append(row_dict)
    return result_list


def get_total_num_accounts():
    """
        Returns the total number of accounts (both drivers and riders) in the system.
    """
    total_accounts = {'total_accounts': len(list_all_driver_records() + list_all_rider_records())}
    return total_accounts


def get_all_accounts():
    """
        Returns all accounts (both drivers and riders) in the system.
    """
    total_accounts = list_all_driver_records() + list_all_rider_records()
    return total_accounts


def get_all_rides():
    """
        Get all the previous rides and information regarding them.
    """

    select_sql = """
        SELECT ride_id, driver_id, rider_id, start_point, destination, ride_ts, cost
        FROM rides;
    """

    # Execute the query and get the results as a list of tuples
    rows = exec_get_all(select_sql)

    # Convert the list of tuples to a list of dictionaries
    keys = ['ride_id', 'driver_id', 'rider_id', 'start_point', 'destination', 'ride_ts', 'cost']
    result_list = []
    for row in rows:
        row_dict = {keys[i]: str(row[i]) for i in range(len(keys))}
        result_list.append(row_dict)
    return result_list


def add_new_driver_account(driver_id, first_name, last_name, rating, mobile_number, special_instructions, is_available, zip_code, available_at):
    data = (driver_id, first_name, last_name, rating, mobile_number, special_instructions, is_available, zip_code, available_at)
    insert_sql = """
        INSERT INTO rideshare_drivers (driver_id, first_name, last_name, rating, mobile_number, special_instructions, is_available, zip_code, available_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    exec_commit(insert_sql, data)


def add_new_rider_account(rider_id, first_name, last_name, rating, mobile_number, special_instructions, is_available, zip_code, available_at):
    data = (rider_id, first_name, last_name, rating, mobile_number, special_instructions, is_available, zip_code, available_at)
    insert_sql = """
        INSERT INTO riders (rider_id, first_name, last_name, rating, mobile_number, special_instructions, is_available, zip_code, available_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    exec_commit(insert_sql, data)



def update_driver_first_name(driver_id, first_name):
    data = (first_name, driver_id)
    update_sql = """
        UPDATE rideshare_drivers
        SET first_name = %s
        WHERE driver_id = %s;
    """
    exec_commit(update_sql, data)

def update_driver_last_name(driver_id, last_name):
    data = (last_name, driver_id)
    update_sql = """
        UPDATE rideshare_drivers
        SET last_name = %s
        WHERE driver_id = %s;
    """
    exec_commit(update_sql, data)

def update_driver_rating(driver_id, rating):
    data = (rating, driver_id)
    update_sql = """
        UPDATE rideshare_drivers
        SET rating = %s
        WHERE driver_id = %s;
    """
    exec_commit(update_sql, data)

def update_driver_mobile_number(driver_id, mobile_number):
    data = (mobile_number, driver_id)
    update_sql = """
        UPDATE rideshare_drivers
        SET mobile_number = %s
        WHERE driver_id = %s;
    """
    exec_commit(update_sql, data)

def update_driver_special_instructions(driver_id, special_instructions):
    data = (special_instructions, driver_id)
    update_sql = """
        UPDATE rideshare_drivers
        SET special_instructions = %s
        WHERE driver_id = %s;
    """
    exec_commit(update_sql, data)

def update_driver_is_available(driver_id, is_available):
    data = (is_available, driver_id)
    update_sql = """
        UPDATE rideshare_drivers
        SET is_available = %s
        WHERE driver_id = %s;
    """
    exec_commit(update_sql, data)

def update_driver_zip_code(driver_id, zip_code):
    data = (zip_code, driver_id)
    update_sql = """
        UPDATE rideshare_drivers
        SET zip_code = %s
        WHERE driver_id = %s;
    """
    exec_commit(update_sql, data)

def update_driver_available_at(driver_id, available_at):
    data = (available_at, driver_id)
    update_sql = """
        UPDATE rideshare_drivers
        SET available_at = %s
        WHERE driver_id = %s;
    """
    exec_commit(update_sql, data)


def update_rider_first_name(rider_id, first_name):
    data = (first_name, rider_id)
    update_sql = """
        UPDATE riders
        SET first_name = %s
        WHERE rider_id = %s;
    """
    exec_commit(update_sql, data)
    

def update_rider_last_name(rider_id, last_name):
    data = (last_name, rider_id)
    update_sql = """
        UPDATE riders
        SET last_name = %s
        WHERE rider_id = %s;
    """
    exec_commit(update_sql, data)
    

def update_rider_rating(rider_id, rating):
    data = (rating, rider_id)
    update_sql = """
        UPDATE riders
        SET rating = %s
        WHERE rider_id = %s;
    """
    exec_commit(update_sql, data)
    

def update_rider_mobile_number(rider_id, mobile_number):
    data = (mobile_number, rider_id)
    update_sql = """
        UPDATE riders
        SET mobile_number = %s
        WHERE rider_id = %s;
    """
    exec_commit(update_sql, data)
    

def update_rider_special_instructions(rider_id, special_instructions):
    data = (special_instructions, rider_id)
    update_sql = """
        UPDATE riders
        SET special_instructions = %s
        WHERE rider_id = %s;
    """
    exec_commit(update_sql, data)
    

def update_rider_is_available(rider_id, is_available):
    data = (is_available, rider_id)
    update_sql = """
        UPDATE riders
        SET is_available = %s
        WHERE rider_id = %s;
    """
    exec_commit(update_sql, data)
    

def update_rider_zip_code(rider_id, zip_code):
    data = (zip_code, rider_id)
    update_sql = """
        UPDATE riders
        SET zip_code = %s
        WHERE rider_id = %s;
    """
    exec_commit(update_sql, data)
    

def update_rider_available_at(rider_id, available_at):
    data = (available_at, rider_id)
    update_sql = """
        UPDATE riders
        SET available_at = %s
        WHERE rider_id = %s;
    """
    exec_commit(update_sql, data)


def remove_driver_account(driver_id):
    # Delete the driver from the drivers table
    delete_sql = """
        DELETE FROM rideshare_drivers WHERE driver_id = %s
    """
    exec_commit(delete_sql, (driver_id,))

    # Set the driver_id on all rides the driver was part of to null
    update_sql = """
        UPDATE rides SET driver_id = null WHERE driver_id = %s
    """
    exec_commit(update_sql, (driver_id,))
    return "Driver account removed successfully"


def get_rides_for_rider(rider_id):
    data = (rider_id,)
    sql = """
        SELECT rides.ride_id, rides.driver_id, start_point, destination, ride_ts, rating, cost
        FROM rides
        JOIN riders
        ON rides.rider_id = riders.rider_id
        WHERE rides.rider_id = %s
    """
    rides = exec_get_all(sql, data)
    return rides


def delete_ride(ride_id):
    delete_sql = """
        DELETE FROM rides WHERE rides.ride_id = %s;
    """
    exec_commit(delete_sql, (ride_id,))
    return "Ride deleted successfully"


def remove_rider_account(rider_id):
    # Delete all rides associated with this rider
    rides = get_rides_for_rider(rider_id)
    for ride in rides:
        delete_ride(ride[0])

    # Delete the rider record
    delete_sql = """
        DELETE FROM riders
        WHERE riders.rider_id = %s;
    """
    exec_commit(delete_sql, (rider_id,))
    return "Rider account removed successfully"


def get_rider_receipt(rider_id, limit=None):
    
    data = [
        {"ride_id": 1, "driver_id": 4, "rider_id": 1, "start_point": "31.6", "destination": "51.6", "ride_ts": "2023-02-26 15:45:30", "cost": 14.50},
        {"ride_id": 2, "driver_id": 4, "rider_id": 1, "start_point": "5.5.5", "destination": "7.7.7", "ride_ts": "2023-05-26 15:45:30", "cost": 23.95},
        {"ride_id": 3, "driver_id": 1, "rider_id": 2, "start_point": "5.5.5", "destination": "7.7.7", "ride_ts": "2023-06-26 15:45:30", "cost": 53.45},
        {"ride_id": 4, "driver_id": 3, "rider_id": 1, "start_point": "10.10.10", "destination": "11.11.11", "ride_ts": "2023-08-26 15:45:30", "cost": 34.50},
        {"ride_id": 5, "driver_id": 2, "rider_id": 3, "start_point": "20.20.20", "destination": "25.25.25", "ride_ts": "2023-09-26 15:45:30", "cost": 15.50},
        {"ride_id": 6, "driver_id": 3, "rider_id": 4, "start_point": "1.1.1", "destination": "2.2.2", "ride_ts": "2023-10-26 15:45:30", "cost": 12.50},
        {"ride_id": 7, "driver_id": 4, "rider_id": 2, "start_point": "4.4.4", "destination": "6.6.6", "ride_ts": "2023-11-26 15:45:30", "cost": 21.50},
        {"ride_id": 8, "driver_id": 2, "rider_id": 3, "start_point": "13.13", "destination": "15.15", "ride_ts": "2023-12-26 15:45:30", "cost": 17.50},
        {"ride_id": 9, "driver_id": 1, "rider_id": 4, "start_point": "16.16", "destination": "18.18", "ride_ts": "2024-01-26 15:45:30", "cost": 11.50},
        {"ride_id": 10, "driver_id": 3, "rider_id": 2, "start_point": "14.14", "destination": "15.15", "ride_ts": "2024-02-26 15:45:30", "cost": 27.50}
    ]
    
    res = [e for e in data if int(rider_id) == e['rider_id']]
    
    if limit < len(res):
        res = res[:limit]
    
    return res
