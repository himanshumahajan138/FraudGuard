from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, current_user, logout_user
from user_model import User
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv
from Main import CHECK
from flask_bcrypt import Bcrypt


load_dotenv()
MONGODB_URI = os.environ.get("MONGODB_URI")
SECRET_KEY = os.environ.get("SECRET_KEY")
DATABASE_NAME = os.environ.get("DATABASE_NAME")
COLLECTION_NAME = os.environ.get("COLLECTION_NAME")

if not SECRET_KEY:
    raise RuntimeError(
        "SECRET_KEY is not set! Set an environment variable named 'SECRET_KEY'"
    )

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY  # Replace with a strong secret key
# Define the upload folder
app.config["UPLOAD_FOLDER"] = "uploads"
# Configure Bcrypt
bcrypt = Bcrypt(app)

# Configure LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"  # Redirect to login route for unauthorized access

# Connect to MongoDB
client = MongoClient(
    MONGODB_URI, server_api=ServerApi("1"), tls=True, tlsAllowInvalidCertificates=True
)
# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    raise e ("Database connection problem !")

db = client[DATABASE_NAME]  # Replace with your database name


def save_file(file):
    # Save the file to the upload folder and return the file path
    if file:
        filename = file.filename
        # Create the upload folder if it doesn't exist
        upload_folder = app.config["UPLOAD_FOLDER"]
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        return file_path
    else:
        return None


# User loader function
@login_manager.user_loader
def load_user(user_id):
    users_collection = db[
        COLLECTION_NAME
    ]  # Replace with your collection name (if different)
    user_data = users_collection.find_one({"_id": ObjectId(user_id)})
    return User(user_data) if user_data else None


@app.route("/", methods=["GET", "POST"])
def home():

    if not current_user.is_authenticated:
        return redirect(url_for("login"))  # Redirect to login if not authenticated
    result = None
    if request.method == "POST":
        # Check if the file is present in the request
        if "image_path" in request.files:
            # Get the file data
            image_file = request.files["image_path"]
            # Save the file to a temporary location or process it directly
            image_path = save_file(image_file)
        else:
            return "No file provided"

        # Get the document type from the form
        document_type = request.form.get("document_type")

        result = CHECK(document_type, image_path)  # Capture the result
        return render_template("result.html", result=result)
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        # Basic validation (you can add more checks)
        if username == "" or email == "" or password == "" or confirm_password == "":
            # Show error message
            return render_template("register.html", error="Please fill out all fields.")
        if password != confirm_password:
            # Show error message
            return render_template("register.html", error="Passwords do not match.")

        # Check for existing user
        users_collection = db[
            COLLECTION_NAME
        ]  # Replace with your collection name (if different)
        existing_userid = users_collection.find_one({"username": username})
        existing_useremail = users_collection.find_one({"email": email})

        if existing_userid or existing_useremail:
            # Show warning message (explained later)
            return render_template("register.html", error="User already exists.")

        # hashing password using Bcrypt
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        # Create a new user document
        new_user = {
            "username": username,
            "email": email,
            "password_hash": hashed_password,
        }
        users_collection = db[
            COLLECTION_NAME
        ]  # Replace with your collection name (if different)

        # Insert the user document into the collection
        users_collection.insert_one(new_user)

        # Redirect to confirmation or login page
        return redirect(url_for("login"))  # redirect to login
    else:
        return render_template("register.html")


# Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Implement logic to validate user credentials against database
        users_collection = db[
            COLLECTION_NAME
        ]  # Replace with your collection name (if different)
        user_data = users_collection.find_one({"username": username})

        if user_data and bcrypt.check_password_hash(
            user_data["password_hash"], password
        ):
            user = User(user_data)  # Create User object from MongoDB data
            login_user(user)
            return redirect(url_for("home"))  # Redirect to your home page

        # Handle failed login attempt
        flash("Invalid username/password!", "error")
    return render_template("login.html")


# Logout route
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
