from pymongo import MongoClient
from pymongo.errors import PyMongoError


class CRUD:
    """
    A class for performing CRUD operations in MongoDB.
    """

    def __init__(self, username, password, host="localhost", port=27017, database=None):
        """
        Initialize the MongoDB connection.
        """
        try:
            self.client = MongoClient(
                f"mongodb://{username}:{password}@{host}:{port}/?authSource=admin"
            )
            self.database = self.client[database] if database else None
        except PyMongoError as e:
            print(f"Error connecting to MongoDB: {e}")
            raise

    def create(self, collection, document):
        """
        Inserts a document into the specified collection.
        """
        try:
            if not self.database:
                raise ValueError("Database not selected.")
            result = self.database[collection].insert_one(document)
            return result.acknowledged
        except PyMongoError as e:
            print(f"Error inserting document: {e}")
            return False

    def read(self, collection, query):
        """
        Reads documents from the specified collection.
        """
        try:
            if not self.database:
                raise ValueError("Database not selected.")
            cursor = self.database[collection].find(query)
            return list(cursor)
        except PyMongoError as e:
            print(f"Error reading documents: {e}")
            return []

    def update(self, collection, query, update_values):
        """
        Updates documents in the specified collection.
        """
        try:
            if not self.database:
                raise ValueError("Database not selected.")
            result = self.database[collection].update_many(query, update_values)
            return result.modified_count
        except PyMongoError as e:
            print(f"Error updating documents: {e}")
            return 0

    def delete(self, collection, query):
        """
        Deletes documents from the specified collection.
        """
        try:
            if not self.database:
                raise ValueError("Database not selected.")
            result = self.database[collection].delete_many(query)
            return result.deleted_count
        except PyMongoError as e:
            print(f"Error deleting documents: {e}")
            return 0
