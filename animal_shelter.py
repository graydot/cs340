from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        if not (username and password):
            raise Exception("Username or Password not present")
        USER = username #'aacuser'
        PASS = password #'Password123isstrong'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30489
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # Create object by passing in a dict of key value pairs
    def create(self, data):
        if data is not None:
            try:
                self.database.animals.insert_one(data)  # data should be dictionary            
                return True
            except Exception:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Read objects by passing in key/value pairs to find with
    def read(self, data):
        if data is not None:
            res = self.database.animals.find(data) # data should be a dictionary
            return list(res)
        else:
            raise Exception("Nothing to find, because data parameter is empty")

    # Update objects by pass in key value pairs to find with and update. 
    def update(self, find_data, update_data):
        if find_data is not None and update_data is not None:
            res = self.database.animals.update_many(find_data, {"$set": update_data})    
            return res.modified_count
        else:
            raise Exception("Nothing to find or update, because data parameter is empty")

    # Delete objects that match key value pairs passed as arguments
    def delete(self, data):
        if data is not None:
            res = self.database.animals.delete_many(data)
            return res.deleted_count
        else:
            raise Exception("Nothing to find, because data parameter is empty")