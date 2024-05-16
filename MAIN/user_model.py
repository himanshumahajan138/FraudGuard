from bson import ObjectId  # Import ObjectId for MongoDB object IDs

class User:
    def __init__(self, user_data):
        self.id = user_data.get("_id", None)  # Handle potential absence of "_id"
        if self.id:
            self.id = ObjectId(self.id)  # Convert string ID to ObjectId if present
        self.username = user_data.get("username")
        self.email = user_data.get("email")
        self.password_hash = user_data.get("password_hash")

    # Add methods for additional functionalities (optional)

    def is_authenticated(self):
        return True  # Assuming presence of password_hash indicates authenticated user
    def is_active(self):
        return True  # Assuming a user is active by default (adjust based on your logic)
    def get_id(self):
        return str(self.id) # Assuming 'id' attribute holds the unique user identifier
    def is_anonymous(self):
        return False
