##########################################################
#   Sort collections in ascending battery voltage order  #
##########################################################


# Import modules
import collections
import smtplib
from pymongo import MongoClient
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Specify MongoDB conenction details
uri = "mongodb+srv://" #Credentials
database = 'UBC_Dendrometer'

# Create a new client and connect to the server
client = MongoClient(uri)
db = client[database]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")
except Exception as e:
    print(e)

# We will add report content to these variable
report = []
first_line = ''
new_line = ''
unsorted_list = []

collections = db.list_collection_names()


# Create a while loop to iterate for each collection
for collection in collections:
    print(collection)
