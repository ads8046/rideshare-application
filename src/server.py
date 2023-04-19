"""
    Author: Atharva Shivankar <ads8046@rit.edu>
    SWEN 344 - REST API Project (Rideshare)
"""

from flask import Flask
from flask_restful import Resource, Api
from api.rideshare_api_svc import *
from api.management import *
from api.welcome import *

app = Flask(__name__)
api = Api(app)

# ---- Web application information and metadata ----
api.add_resource(Init, '/manage/init') #Management API for initializing the DB
api.add_resource(Version, '/manage/version') #Management API for checking DB version
api.add_resource(Home, '/')

# ---- Endpoints for using the Rideshare API ----
# Access and modify an individual account
api.add_resource(OneDriverAccount, '/rideshare/api/drivers/d_account/<id>')
api.add_resource(OneRiderAccount, '/rideshare/api/riders/r_account/<id>')

# Create a new account
api.add_resource(AddNewRiderAccount, '/rideshare/api/riders/new_rider')
api.add_resource(AddNewDriverAccount, '/rideshare/api/drivers/new_driver')

# Access all accounts and get total number of accounts
api.add_resource(AllDriverAccounts, '/rideshare/api/drivers/all')
api.add_resource(AllRiderAccounts, '/rideshare/api/riders/all')
api.add_resource(TotalAccounts, '/rideshare/api/total_acc')
api.add_resource(AllAccounts, '/rideshare/api/all_accounts')

# Access all rides
api.add_resource(AllRides, '/rideshare/api/all_rides')

# List receipts
# api.add_resource(Receipt, '/rideshare/api/receipts/<int:id>', defaults={'limit': 1})
api.add_resource(Receipt, '/rideshare/api/receipts/<int:id>/<int:limit>', defaults={'limit': 1})


if __name__ == '__main__':
    rebuild_tables()
    app.run(debug=True, port=4999)
