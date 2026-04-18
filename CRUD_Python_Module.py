# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser'
        PASS = 'OFLORES' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: 
            result =  self.database.animals.insert_one(data)  # data should be dictionary  
            if result.acknowledged:
                return True
            else:
                return False
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 

    # Create method to implement the R in CRUD.
    def read(self, query, projection=None):
        if query is not None:
            # If a projection is provided, use it in the find() method.
            if projection is not None:
                cursor = self.database.animals.find(query, projection)
            else:
                # If no projection, perform a normal find.
                cursor = self.database.animals.find(query)
                
            return cursor
        else:
            raise Exception("Search query is empty")
            
    # Method to implement the U in CRUD
    def update(self, query, new_data):
        if query is not None:
            # The update_many method can update multiple documents at once.
            result = self.database.animals.update_many(query, {"$set": new_data})
            # We can return the number of documents that were modified.
            return result.modified_count
        else:
            raise Exception("Update query is empty")
            
     # Method to implement the D in CRUD
    def delete(self, query):
        if query is not None:
            # The delete_many method can remove multiple documents at once.
            result = self.database.animals.delete_many(query)
            # We can return the number of documents that were deleted.
            return result.deleted_count
        else:
            raise Exception("Delete query is empty")