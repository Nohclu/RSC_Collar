import json
import boto3
import config
from entry import Entry
# import requests

dynamodb = boto3.resource(
        "dynamodb",
        region_name="us-east-1",
        aws_access_key_id=config.aws_access_key_id,
        aws_secret_access_key=config.aws_secret_access_key
    )

table = dynamodb.Table("cmulready_2023")

def lambda_handler(event, context):
    """Transforms and stores SQS messages into DynamoDb

    Parameters
    ----------
    event: dict, required
    context: object, required

    Return
    ------
    statusCode: dict
    """

    entry = Entry(event)    
    table.put_item(Item=entry.getEntry())

    return {
        "statusCode": 200
    }
