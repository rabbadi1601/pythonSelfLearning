import logging
from random import random

import boto3
from botocore.exceptions import ClientError
import boto3
'''
s3 = boto3.resource('s3')
s3.create_bucket(Bucket='selftest-python2'+str(random()))

s3.create_bucket(Bucket='selftest-python3'+str(random()), CreateBucketConfiguration={
    'LocationConstraint': 'us-west-2'})
'''

def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

#bucket_name="selftest-python2"+str(random())

create_bucket("selftest-python4"+str(random()))
create_bucket("selftest-python4"+str(random()),"us-west-2")