import json
import boto3
import config
from battery import Battery
from location import Location
from pet import Pet

dynamodb = boto3.resource(
        "dynamodb",
        region_name="us-east-1",
        aws_access_key_id=config.aws_access_key_id,
        aws_secret_access_key=config.aws_secret_access_key
    )

table = dynamodb.Table("cmulready_2023")

def getEntry(uuid, timestamp):
    response = dynamodb.get_item(
        Key={
            "uuid": uuid, "timestamp": timestamp
        }
    )
    return response

def lambda_handler(event, context):

    if event["path"] == "getbattery" and event["httpMethod"] == "GET":
        b = Battery()
        return
    elif event["path"] == "getlocation" and event["httpMethod"] == "GET":
        l = Location()
        # getLatest Location entry
        return
    elif event["path"] == "getpet" and event["httpMethod"] == "GET":
        p = Pet()
        # getLatest pet entry
        return