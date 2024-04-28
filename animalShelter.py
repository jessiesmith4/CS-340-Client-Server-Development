from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps

# Jessie Smith
# SNHU
# CS 340
# 4 April 2024


class AnimalShelter(object):

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the AAC database, the
        # animals collection, and the aacuser.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        # username = 'aacuser'
        # password = 'PASS_24'
        host = 'nv-desktop-services.apporto.com'
        port = 31974
        db = 'AAC'
        col = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username, password, host, port))
        self.database = self.client['%s' % (db)]
        self.collection = self.database['%s' % (col)]
        print("Connection Successful")

    # Create method to implement the C in CRUD.
    def create(self, data):
        if data:
            self.database.animals.insert(data)
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Read method to implement the R in CRUD.
    def readId(self, pid):
        data = self.database.find({'_id': ObjectId(pid)})
        return pid
    
    def read(self, query):
        if query:
            data = self.database.animals.find(query, {'_id': 0})
        else:
            data = self.database.animals.find({}, {'_id': 0})
        return data
    
    # Update method to implement the U in CRUD
    def update(self, query, update):
        if query:
            data = self.database.animals.update_many(query, { "$set": update})
            print("Update successful")
        else:
            raise Exception("Update unsuccessful")
        return data.raw_result
    
    # Delete method to implement the D in CRUD
    def delete(self, delete):
        if delete:
            data = self.database.animals.delete_many(delete)
            print("Delete successful")
        else:
            raise Exception("Delete unsuccessful")
        return data.raw_result