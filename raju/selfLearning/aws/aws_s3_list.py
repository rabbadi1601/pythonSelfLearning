from random import random

import boto3

s3 = boto3.client('s3')

response = s3.list_buckets()
# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(bucket["Name"])
    #print(f'  {bucket["Name"]}')



s3 = boto3.client('s3')
#s3.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')
s3.download_file('selftest-python3', 'RAJU ABBADI_RESUME-Varite.pdf', 'RAJU ABBADI_RESUME-Varite.pdf')