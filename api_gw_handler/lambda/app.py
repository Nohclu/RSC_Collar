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

def lambda_handler(event, context):

    if event["path"] == "getbattery" and event["httpMethod"] == "GET":
        # GetLatest Battery Entry
        pass
    elif event["path"] == "getlocation" and event["httpMethod"] == "GET":
        # getLatest Location entry
        pass
    elif event["path"] == "getpet" and event["httpMethod"] == "GET":
        # getLatest pet entry
        pass

    return {
        "statusCode": 200
    }
