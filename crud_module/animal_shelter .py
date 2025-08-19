from pymongo import MongoClient

class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB."""

    def __init__(self, username, password, host="nv-desktop-services.apporto.com", port=34734, db="AAC", collection="animals"):
        """
        Initialize the MongoClient and connect to the specified MongoDB database and collection.
        """
        try:
            # Construct the MongoDB connection string
            connection_string = f"mongodb://{username}:{password}@{host}:{port}/?authSource=admin"
            self.client = MongoClient(connection_string, serverSelectionTimeoutMS=5000)
            self.client.server_info()  # Force connection test
            self.database = self.client[db]
            self.collection = self.database[collection]
            print(f"Connected to MongoDB at {host}:{port}, Database: {db}, Collection: {collection}")
        except Exception as e:
            raise Exception(f"Failed to connect to MongoDB: {e}")

    def create(self, data):
        """Insert a single document into the collection."""
        if data:
            try:
                result = self.collection.insert_one(data)
                return result.acknowledged
            except Exception as e:
                raise Exception(f"Create operation failed: {e}")
        else:
            raise ValueError("No data provided to create.")

    def read(self, query={}):
        """Retrieve documents from the collection."""
        try:
            return list(self.collection.find(query))
        except Exception as e:
            raise Exception(f"Read operation failed: {e}")

    def update(self, search_query, update_data):
        """Update documents in the collection."""
        if search_query and update_data:
            try:
                result = self.collection.update_many(search_query, {"$set": update_data})
                return result.modified_count
            except Exception as e:
                raise Exception(f"Update operation failed: {e}")
        else:
            raise ValueError("Search query and update data must be provided.")

    def delete(self, search_query):
        """Delete documents from the collection."""
        if search_query:
            try:
                result = self.collection.delete_many(search_query)
                return result.deleted_count
            except Exception as e:
                raise Exception(f"Delete operation failed: {e}")
        else:
            raise ValueError("Search query must be provided for delete operation.")

