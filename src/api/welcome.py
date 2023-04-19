from flask_restful import Resource, reqparse, request  #NOTE: Import from flask_restful, not python
from db.swen344_db_utils import *

class Home(Resource):
    def get(self):
        return ({'welcome': 'welcome to the rideshare API'})
