# Importing the OS module
import os 

# creation of base directory for application
basedir = os.path.abspath(os.path.dirname(__file__))


# Config Class
# Configure the database (when we have one) AND configure the 
# secret key for the encryption of our submitted forms
class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess this....'
    # we want sqlalchemy to setup where our database is going to be: which will be local to this project in our class folder
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False