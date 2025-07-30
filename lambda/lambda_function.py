import json
import boto3
import os

s3 = boto3.client("s3")
#presignedurluserdocimages -> bucket name
BUCKET_NAME = os.environ["UPLOAD_BUCKET"]
URL_EXPIRATION = 900  # 15 minutes

def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])

        file_name = event["file_name"]
        profile_exists = event["profile_exists"]
        user_id = event["user_id"]

        if not file_name:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing file_name"}),
                "headers": {"Content-Type": "application/json"}
            }

        if profile_exists and not user_id:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing user_id for profile"}),
                "headers": {"Content-Type": "application/json"}
            }

        file_key = f"uploads/{user_id}/{file_name}"

        presigned_url = s3.generate_presigned_url(
            "put_object",
            Params={"Bucket": BUCKET_NAME, "Key": file_key},
            ExpiresIn=URL_EXPIRATION,
            HttpMethod="PUT"
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "upload_url": presigned_url,
                "file_key": file_key,
                "expires_in": URL_EXPIRATION
            }),
            "headers": {"Content-Type": "application/json"}
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
            "headers": {"Content-Type": "application/json"}
        }