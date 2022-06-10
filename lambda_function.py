import json
import csv
# import s3fs

def lambda_handler(event, context):
    path = 's3a://aaabhishek/testusingpowershell.csv'
    file = open(path)
    type(file)
    print(path)