import io
import logging
import boto3
from botocore.exceptions import ClientError

# allows for print statements to log into Cloudwatch
# The --log option will show logs on the commandline
# eg:  serverless invoke -f upload --log
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def upload_fileobj(file_obj, bucket, object_name):
    """Upload a file to an S3 bucket

    :param file_obj: File object to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name.
    :return: True if file was uploaded, else False
    """

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_fileobj(file_obj, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True



def main(event, context):
    """
    upload content to an s3 bucket.
    :param event:
    :param context:
    :return: successful or unsuccessful http response
    """
    file_obj = io.BytesIO(b"test")
    bucket = 'not.implemented'
    object_name = '/also/not/implemented'
    upload_occured = upload_fileobj(file_obj, bucket, object_name)
    if upload_occured:
        return {
            "statusCode": 200,
            "body": {"message": "success"}
        }
    else:
        return {
            "statusCode": 500,
            "body": {"message": "InternalServerError: check AWS logging"}
        }

