#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collections, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'gtung1234' 
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 34716
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
# Complete this create method to implement the C in CRUD.
    def create(self, data = None):
        # Checks if dict is empty, and if not empty inserts dict to database
        if data is not None:
            self.database.animals.insert_one(data) # data should be dictionary
            print("success")
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
                 
            
# Create method to implement the R in CRUD. 
    def read(self, data = None):
        if data is not None: 
            # If query argument is not None, then we query the collection and 
            # If there are matching documents, we create a variable to hold the 
            # matching documents and iterate and print through each 
            # document (since find() uses a cursor).
            animal = self.database.animals.find(data)
            list = []
            for each in animal:
                list.append(each)
            return list
        else:
            raise Exception("Nothing to read, because data parameter is empty")
            
# Create method to implement the U in CRUD.
    def update(self, data = None, update = None):
        if data and update is not None:         
            # Since data and update are not None, we create a suitable syntax
            # with the update input arguement to use for update_many().
            updateData = {"$set" : update}    
            result = self.database.animals.update_many(data, updateData)
            # Prints the number of documents modified using attribute of update_many()
            print(f"Documents modified: {result.modified_count}")
        else:
            raise Exception("No query entered")
            
            
# Create method to implement the D in CRUD.
    def delete(self, data = None):
        if data is not None:
            # Create count variable to determine if query finds matching documents.
            # If one document is found, we use delete_one(), but if more is found,
            # we use delete_many().
            # Output is the number of documents deleted or if no documents are matched. 
            count = self.database.animals.count(data)
            if count == 1:
                result = self.database.animals.delete_one(data)
                print(f"Documents deleted: {result.deleted_count}")
            elif count > 1:
                result = self.database.animals.delete_many(data)
                print(f"Documents deleted: {result.deleted_count}")
            else:
                print("No matching documents")
        else:
            raise Exception("No query entered")
                
            
                

            
