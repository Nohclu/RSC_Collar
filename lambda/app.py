import json
import boto3
import config
# import requests

dynamodb = boto3.resource(
        "dynamodb",
        region_name="us-east-1",
        aws_access_key_id=config.aws_access_key_id,
        aws_secret_access_key=config.aws_secret_access_key
    )

table = dynamodb.Table("cmulready_2023")

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
    context: object, required
    """

    table.put_item(Item=event)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
