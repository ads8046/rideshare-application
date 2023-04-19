from flask_restful import Resource, reqparse
from flask_restful import abort
from db import rideshare_dao as dao
import json

class OneDriverAccount(Resource):
    def get(self, id):
        return dao.get_single_driver_account_info(id)
    
    def delete(self, id):
        if dao.get_single_driver_account_info(id):
            return dao.remove_driver_account(id)
        return {"Unsuccessful": f"Driver with ID {id} does not exist in the records."}

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', type=str)
        parser.add_argument('last_name', type=str)
        parser.add_argument('rating', type=float)
        parser.add_argument('mobile_number', type=str)
        parser.add_argument('special_instructions', type=str)
        parser.add_argument('is_available', type=bool)
        parser.add_argument('zip_code', type=str)
        parser.add_argument('available_at', type=str)
        args = parser.parse_args()

        # Update the driver record in the database
        # Use id from URL parameter and args from request body
        dao.update_driver_first_name(id, args["first_name"])
        dao.update_driver_last_name(id, args["last_name"])
        dao.update_driver_rating(id, args["rating"])
        dao.update_driver_mobile_number(id, args["mobile_number"])
        dao.update_driver_special_instructions(id, args["special_instructions"])
        dao.update_driver_is_available(id, args["is_available"])
        dao.update_driver_zip_code(id, args["zip_code"])
        dao.update_driver_available_at(id, args["available_at"])

        # Return the updated driver record
        updated_driver_record = dao.get_single_driver_account_info(id)
        return updated_driver_record, 200


class AllDriverAccounts(Resource):
    def get(self):
        return dao.list_all_driver_records()
    
    
class OneRiderAccount(Resource):
    def get(self, id):
        return dao.get_single_rider_account_info(id)
    
    def delete(self, id):
        if dao.get_single_rider_account_info(id):
            return json.dumps(dao.remove_rider_account(id))
        return {"Unsuccessful": f"Rider with ID {id} does not exist in the records."}
    
    def put(self, id):
        if dao.get_single_rider_account_info(id):
            parser = reqparse.RequestParser()
            parser.add_argument('first_name', type=str)
            parser.add_argument('last_name', type=str)
            parser.add_argument('rating', type=float)
            parser.add_argument('mobile_number', type=str)
            parser.add_argument('special_instructions', type=str)
            parser.add_argument('is_available', type=bool)
            parser.add_argument('zip_code', type=str)
            parser.add_argument('available_at', type=str)
            args = parser.parse_args()

            # Update the rider record in the database
            # Use id from URL parameter and args from request body
            dao.update_rider_first_name(id, args["first_name"])
            dao.update_rider_last_name(id, args["last_name"])
            dao.update_rider_rating(id, args["rating"])
            dao.update_rider_mobile_number(id, args["mobile_number"])
            dao.update_rider_special_instructions(id, args["special_instructions"])
            dao.update_rider_is_available(id, args["is_available"])
            dao.update_rider_zip_code(id, args["zip_code"])
            dao.update_rider_available_at(id, args["available_at"])

            # Return the updated rider record
            updated_rider_record = dao.get_single_rider_account_info(id)
            return updated_rider_record, 200
        
        return {"Unsuccessful": f"Rider with ID {id} does not exist in the records."}
    
    
class AllRiderAccounts(Resource):
    def get(self):
        return dao.list_all_rider_records()
    
    
class AllRides(Resource):
    def get(self):
        return dao.get_all_rides()


class TotalAccounts(Resource):
    def get(self):
        return dao.get_total_num_accounts()
    

class AllAccounts(Resource):
    def get(self):
        return dao.get_all_accounts()
    

class AddNewDriverAccount(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('driver_id', type=int, required=True)
            parser.add_argument('first_name', type=str, required=True)
            parser.add_argument('last_name', type=str, required=True)
            parser.add_argument('rating', type=float, required=True)
            parser.add_argument('mobile_number', type=str, required=True)
            parser.add_argument('special_instructions', type=str)
            parser.add_argument('is_available', type=bool, required=True)
            parser.add_argument('zip_code', type=str, required=True)
            parser.add_argument('available_at', type=str, required=True)
            
            args = parser.parse_args()
            
            driver_id = args["driver_id"]
            first_name = args["first_name"]
            last_name = args["last_name"]
            rating = args["rating"]
            mobile_number = args["mobile_number"]
            special_instructions = args.get("special_instructions", "")  # use .get() method to handle optional parameter
            is_available = args["is_available"]
            zip_code = args["zip_code"]
            available_at = args["available_at"]
            
            # Check whether the driver already exists
            if dao.get_single_driver_account_info(driver_id):
                return {"Unsuccessful": f"Driver with ID {driver_id} already exists"}
                
                
            # Add the new driver account
            dao.add_new_driver_account(driver_id, first_name, last_name, rating, mobile_number, special_instructions, is_available, zip_code, available_at)
            return {"Successful": "new driver account created", "driver_id": driver_id}

        except Exception as e:
            print(f"An exception occurred while creating a new driver record: {e}")
            return {"Unsuccessful": f"An exception occurred while creating a new driver account: {e}"}
    

class AddNewRiderAccount(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('rider_id', type=int, required=True)
            parser.add_argument('first_name', type=str, required=True)
            parser.add_argument('last_name', type=str, required=True)
            parser.add_argument('rating', type=float, required=True)
            parser.add_argument('mobile_number', type=str, required=True)
            parser.add_argument('special_instructions', type=str)
            parser.add_argument('is_available', type=bool, required=True)
            parser.add_argument('zip_code', type=str, required=True)
            parser.add_argument('available_at', type=str, required=True)
            
            args = parser.parse_args()
            
            rider_id = args["rider_id"]
            first_name = args["first_name"]
            last_name = args["last_name"]
            rating = args["rating"]
            mobile_number = args["mobile_number"]
            special_instructions = args.get("special_instructions", "")  # use .get() method to handle optional parameter
            is_available = args["is_available"]
            zip_code = args["zip_code"]
            available_at = args["available_at"]
            
            # Check whether the rider already exists
            if dao.get_single_rider_account_info(rider_id):
                return {"Unsuccessful": f"Rider with ID {rider_id} already exists"}
                
            # Add the new rider account
            dao.add_new_rider_account(rider_id, first_name, last_name, rating, mobile_number, special_instructions, is_available, zip_code, available_at)
            return {"Successful": "new driver account created", "driver_id": rider_id}
        
        except Exception as e:
            print(f"An exception occured while creating a new rider record: {e}")
            return {"Unsuccessful": f"An exception occured while creating a new rider account: {e}"}


class Receipt(Resource):
    def get(self, id, limit):
        if dao.get_single_rider_account_info(id):
            return dao.get_rider_receipt(id, limit)
        return {"Unsuccessful": f"Rider with {id} does not exist."}
    