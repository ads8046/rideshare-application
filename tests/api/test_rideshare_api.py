import unittest
from tests.test_utils import *
import requests
import json


class TestExample(unittest.TestCase):

    def setUp(self):  
        """Initialize DB using API call"""
        post_rest_call(self, 'http://127.0.0.1:4999/manage/init')
        print("DB Should be reset now")


    def test_get_single_driver_account(self):
        """
            Test case to verify the functionality of the `get_single_driver_account_info` function.
            It checks if the function returns the correct dictionary object of a single driver record
            for the given driver id. 
        """
        
        expected = [{
            "driver_id": "2",
            "first_name": "Mary",
            "last_name": "Dion",
            "rating": "3.2",
            "mobile_number": "5954853737",
            "special_instructions": "drop me at the mall",
            "is_available": "True",
            "zip_code": "55632",
            "available_at": "2023-02-26 15:45:30"
        }]
        actual = get_rest_call(self, 'http://127.0.0.1:4999/rideshare/api/drivers/d_account/2')
        self.assertEqual(expected, actual)


    def test_list_all_driver_records(self):
        """
            Test case to verify the functionality of the `list_all_driver_records` function.
            It checks if the function returns the correct list of all driver JSON records.
        """
        
        expected = [
            {
                "driver_id": "1",
                "first_name": "Jane",
                "last_name": "Doe",
                "rating": "5",
                "mobile_number": "4553737",
                "special_instructions": "have a fun ride",
                "is_available": "True",
                "zip_code": "14647",
                "available_at": "2023-02-26 15:45:30"
            },
            {
                "driver_id": "2",
                "first_name": "Mary",
                "last_name": "Dion",
                "rating": "3.2",
                "mobile_number": "5954853737",
                "special_instructions": "drop me at the mall",
                "is_available": "True",
                "zip_code": "55632",
                "available_at": "2023-02-26 15:45:30"
            },
            {
                "driver_id": "3",
                "first_name": "Tom",
                "last_name": "Magliozzi",
                "rating": "3.5",
                "mobile_number": "5964853657",
                "special_instructions": "Dont drive like my brother",
                "is_available": "True",
                "zip_code": "55632",
                "available_at": "2023-02-26 15:45:30"
            },
            {
                "driver_id": "4",
                "first_name": "Jon",
                "last_name": "Snow",
                "rating": "4.9",
                "mobile_number": "5964853657",
                "special_instructions": "winter is coming, get the chains out",
                "is_available": "True",
                "zip_code": "44632",
                "available_at": "2023-02-27 17:45:30"
            }
        ]
        
        actual = get_rest_call(self, 'http://127.0.0.1:4999/rideshare/api/drivers/all')
        self.assertEqual(expected, actual)


    def test_get_single_rider_account(self):
        """
            Test case to verify the functionality of the `get_single_rider_account_info` function.
            It checks if the function returns the correct dictionary object of a single rider record
            for the given driver id. 
        """
        
        expected = [
            {
                "rider_id": "2",
                "first_name": "Daisy",
                "last_name": "Werthan",
                "rating": "4.8",
                "mobile_number": "404-555-1212",
                "special_instructions": "Rider",
                "is_available": "True",
                "zip_code": "30301",
                "available_at": "1989-12-12 11:00:00"
            }
        ]
        actual = get_rest_call(self, 'http://127.0.0.1:4999/rideshare/api/riders/r_account/2')
        self.assertEqual(expected, actual)


    def test_list_all_rider_records(self):
        expected = [
            {
                "rider_id": "2",
                "first_name": "Daisy",
                "last_name": "Werthan",
                "rating": "4.8",
                "mobile_number": "404-555-1212",
                "special_instructions": "Rider",
                "is_available": "True",
                "zip_code": "30301",
                "available_at": "1989-12-12 11:00:00"
            },
            {
                "rider_id": "1",
                "first_name": "Vladimir",
                "last_name": "Rider",
                "rating": "4.0",
                "mobile_number": "555-5678",
                "special_instructions": "Waiting for Godot",
                "is_available": "True",
                "zip_code": "90210",
                "available_at": "2023-02-27 10:15:00"
            }
        ]
    
        actual = get_rest_call(self, 'http://127.0.0.1:4999/rideshare/api/riders/all')
        self.assertEqual(expected, actual)


    def test_driver_record_count(self):
        """
            Test case to verify the functionality of the `list_all_driver_records` function.
            It checks if the function returns the correct count of all driver accounts.
        """
        
        expected_count = 4
        actual = get_rest_call(self, 'http://127.0.0.1:4999/rideshare/api/drivers/all')
        actual_count = len(actual)
        self.assertEqual(expected_count, actual_count)
        
    
    def test_unavailable_driver_record(self):
        expected = []
        actual = get_rest_call(self, 'http://127.0.0.1:4999/rideshare/api/drivers/d_account/404')
        self.assertEqual(expected, actual)
    
    
    def test_unavailable_rider_record(self):
        expected = []
        actual = get_rest_call(self, 'http://127.0.0.1:4999/rideshare/api/riders/r_account/404')
        self.assertEqual(expected, actual)
      
    
    def test_all_rides(self):
        expected = [
            {
                "ride_id": "1",
                "driver_id": "4",
                "rider_id": "None",
                "start_point": "31.6",
                "destination": "51.6",
                "ride_ts": "2023-02-26 15:45:30",
                "cost": "14.50"
            },
            {
                "ride_id": "2",
                "driver_id": "4",
                "rider_id": "None",
                "start_point": "5.5.5",
                "destination": "7.7.7",
                "ride_ts": "2023-05-26 15:45:30",
                "cost": "23.95"
            },
            {
                "ride_id": "3",
                "driver_id": "1",
                "rider_id": "None",
                "start_point": "5.5.5",
                "destination": "7.7.7",
                "ride_ts": "2023-06-26 15:45:30",
                "cost": "53.45"
            }
        ]

        actual = get_rest_call(self, 'http://127.0.0.1:4999/rideshare/api/all_rides')
        self.assertEqual(expected, actual)
        
    
    def test_count_total_accounts(self):
        expected = {'total_accounts': 6}
        actual = get_rest_call(self, 'http://127.0.0.1:4999/rideshare/api/total_acc')
        self.assertEqual(expected, actual)
        
        
    def test_add_existing_driver(self):
        # Define the existing user's data
        test_driver_account = {
            "driver_id": "2",
            "first_name": "Mary",
            "last_name": "Dion",
            "rating": "3.2",
            "mobile_number": "5954853737",
            "special_instructions": "drop me at the mall",
            "is_available": "True",
            "zip_code": "55632",
            "available_at": "2023-02-26 15:45:30"
        }
        
        # Send a POST request to add the existing user
        response = requests.post(url="http://127.0.0.1:4999/rideshare/api/drivers/new_driver", json=test_driver_account)
        
        actual = json.loads(response.content)
        
        expected = {
            "Unsuccessful": "Driver with ID 2 already exists"
        }
        self.assertEqual(actual, expected)
        
    
    def test_add_existing_rider(self):
        # Define the existing user's data
        test_rider_account = {
            "rider_id": "2",
            "first_name": "Daisy",
            "last_name": "Werthan",
            "rating": "4.8",
            "mobile_number": "404-555-1212",
            "special_instructions": "Rider",
            "is_available": "True",
            "zip_code": "30301",
            "available_at": "1989-12-12 11:00:00"
        }
        
        # Send a POST request to add the existing user
        response = requests.post(url="http://127.0.0.1:4999/rideshare/api/riders/new_rider", json=test_rider_account)
        
        actual = json.loads(response.content)
        
        expected = {
            "Unsuccessful": "Rider with ID 2 already exists"
        }
        self.assertEqual(actual, expected, "FAIL: The rider account is already registered in the system")


    def test_remove_driver_account(self):
        test_driver_account = {
            "driver_id": "1",
            "first_name": "Jane",
            "last_name": "Doe",
            "rating": "5",
            "mobile_number": "4553737",
            "special_instructions": "have a fun ride",
            "is_available": "True",
            "zip_code": "14647",
            "available_at": "2023-02-26 15:45:30"
        }
        
        response = requests.delete(url="http://127.0.0.1:4999/rideshare/api/drivers/d_account/1", json=test_driver_account)
        actual = json.loads(response.content)
        expected = 'Driver account removed successfully'
        self.assertEqual(actual, expected, "FAIL: The rider account is already registered in the system")

    
    def test_update_driver_account(self):
        # Object being updated: (1, 'Jane', 'Doe', 5, '4553737', 'have a fun ride', True, '14647', '2023-02-26 15:45:30')
        test_driver_update = {
            "driver_id": "1",
            "first_name": "Elizabeth",
            "last_name": "Homes",
            "rating": "4.8",
            "mobile_number": "4553737",
            "special_instructions": "have a fancy ride",
            "is_available": "True",
            "zip_code": "14647",
            "available_at": "2023-02-26 15:45:30"
        }
        
        resp = requests.put(url="http://127.0.0.1:4999/rideshare/api/drivers/d_account/1", json=test_driver_update)
        actual = json.loads(resp.content)
        expected = [{
            "driver_id": "1",
            "first_name": "Elizabeth",
            "last_name": "Homes",
            "rating": "4.8",
            "mobile_number": "4553737",
            "special_instructions": "have a fancy ride",
            "is_available": "True",
            "zip_code": "14647",
            "available_at": "2023-02-26 15:45:30"
        }]
        
        self.assertEqual(actual, expected, "FAIL: Driver record did not update properly")

    
    def test_update_rider_account(self):
        # Object being updated: (1, 'Vladimir', 'Rider', 4.0, '555-5678', 'Waiting for Godot', True, '90210', '2023-02-27 10:15:00')
        test_rider_update = {
            "rider_id": "1",
            "first_name": "Ivan",
            "last_name": "Petrov",
            "rating": "3.5",
            "mobile_number": "404-888-1414",
            "special_instructions": "Rider",
            "is_available": "True",
            "zip_code": "30301",
            "available_at": "1989-12-12 11:00:00"
        }
            
        resp = requests.put(url="http://127.0.0.1:4999/rideshare/api/riders/r_account/1", json=test_rider_update)
        actual = json.loads(resp.content)
        expected = [{
            "rider_id": "1",
            "first_name": "Ivan",
            "last_name": "Petrov",
            "rating": "3.5",
            "mobile_number": "404-888-1414",
            "special_instructions": "Rider",
            "is_available": "True",
            "zip_code": "30301",
            "available_at": "1989-12-12 11:00:00"
        }]
          
        self.assertEqual(actual, expected, "FAIL: Rider record did not update properly")


    def test_list_receipts(self):
        expected = [
            {
                "ride_id": 1,
                "driver_id": 4,
                "rider_id": 1,
                "start_point": "31.6",
                "destination": "51.6",
                "ride_ts": "2023-02-26 15:45:30",
                "cost": 14.5
            }
        ]
        resp = requests.get(url="http://127.0.0.1:4999/rideshare/api/receipts/1/1")
        actual = json.loads(resp.content)
        
        self.assertEqual(actual, expected)
        