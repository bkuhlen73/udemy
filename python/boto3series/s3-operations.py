import boto3
import json
import os
import threading
import sys
import pprint

from boto3.s3.transfer import TransferConfig


BUCKET_NAME = 'bkuhlen-s3-boto3series-bucket'
WEBSITE_BUCKET_NAME = 'YOUR_OWN_DOMAIN_NAME_OR_BUCKET_NAME'


def s3_client():
    s3 = boto3.client('s3')
    """ :type : pyboto3.s3 """

    return s3


def s3_resource():
    s3 = boto3.resource('s3')
    return s3


def create_bucket(bucket_name):
    return s3_client().create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'eu-central-1'
        }
    )


def create_bucket_policy(bucket_name):
    bucket_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AddPerm",
                "Effect": "Allow",
                "Principal": "*",
                "Action": ["s3:*"],
                # "Resource": ["arn:aws:s3:::niyazi-s3-2018-bucket/*"]
                'Resource': 'arn:aws:s3:::' + bucket_name + '/*'
            }
        ]
    }

    policy_string = json.dumps(bucket_policy)

    return s3_client().put_bucket_policy(
        Bucket=bucket_name,
        Policy=policy_string
    )


def list_buckets():
    return s3_client().list_buckets()


def get_bucket_policy():
    return s3_client().get_bucket_policy(Bucket=BUCKET_NAME)


def get_bucket_encryption():
    return s3_client().get_bucket_encryption(Bucket=BUCKET_NAME)


def update_bucket_policy(bucket_name):
    bucket_policy = {
        'Version': '2012-10-17',
        'Statement': [
            {
                'Sid': 'AddPerm',
                'Effect': 'Allow',
                'Principal': '*',
                'Action': [
                    's3:DeleteObject',
                    's3:GetObject',
                    's3:PutObject'
                ],
                'Resource': 'arn:aws:s3:::' + bucket_name + '/*'
            }
        ]
    }

    policy_string = json.dumps(bucket_policy)

    return s3_client().put_bucket_policy(
        Bucket=bucket_name,
        Policy=policy_string
    )


def server_side_encrypt_bucket():
    return s3_client().put_bucket_encryption(
        Bucket=BUCKET_NAME,
        ServerSideEncryptionConfiguration={
            'Rules': [
                {
                    'ApplyServerSideEncryptionByDefault': {
                        'SSEAlgorithm': 'AES256'
                    }
                }
            ]
        }
    )


def delete_bucket():
    return s3_client().delete_bucket(Bucket=BUCKET_NAME)


def upload_small_file():
    file_path = os.path.dirname(__file__) + './readme.txt'
    print(file_path)
    return s3_client().upload_file(file_path, BUCKET_NAME, 'readme.txt')


def upload_large_file():
    config = TransferConfig(multipart_threshold=1024 * 25, max_concurrency=10,
                            multipart_chunksize=1024 * 25, use_threads=True)
    file_path = os.path.dirname(__file__) + '/largefile.pdf'
    key_path = 'multipart_files/largefile.pdf'
    s3_resource().meta.client.upload_file(file_path, BUCKET_NAME, key_path,
                                          ExtraArgs={
                                              'ACL': 'public-read', 'ContentType': 'text/pdf'},
                                          Config=config,
                                          Callback=ProgressPercentage(file_path))


class ProgressPercentage(object):
    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size, percentage
                )
            )
            sys.stdout.flush()


def read_object_from_bucket():
    object_key = 'readme.txt'
    return s3_client().get_object(Bucket=BUCKET_NAME, Key=object_key)


def version_bucket_files():
    s3_client().put_bucket_versioning(
        Bucket=BUCKET_NAME,
        VersioningConfiguration={
            'Status': 'Enabled'
        }
    )


def upload_a_new_version():
    file_path = os.path.dirname(__file__) + '/readme.txt'
    return s3_client().upload_file(file_path, BUCKET_NAME, 'readme.txt')


def put_lifecycle_policy():
    lifecycle_policy = {
        "Rules": [
            {
                "ID": "Move readme file to Glacier",
                "Prefix": "readme",
                "Status": "Enabled",
                "Transitions": [
                    {
                        "Date": "2019-01-01T00:00:00.000Z",
                        "StorageClass": "GLACIER"
                    }
                ]
            },
            {
                "Status": "Enabled",
                "Prefix": "",
                "NoncurrentVersionTransitions": [
                    {
                        "NoncurrentDays": 2,
                        "StorageClass": "GLACIER"
                    }
                ],
                "ID": "Move old versions to Glacier"
            }
        ]
    }

    s3_client().put_bucket_lifecycle_configuration(
        Bucket=BUCKET_NAME,
        LifecycleConfiguration=lifecycle_policy
    )


def host_static_website():
    s3 = boto3.client('s3', region_name='eu-central-1')
    """ :type : pyboto3.s3 """

    s3.create_bucket(
        Bucket=WEBSITE_BUCKET_NAME,
        CreateBucketConfiguration={
            'LocationConstraint': 'eu-central-1'
        }
    )

    update_bucket_policy(WEBSITE_BUCKET_NAME)

    website_configuration = {
        'ErrorDocument': {'Key': 'error.html'},
        'IndexDocument': {'Suffix': 'index.html'}
    }

    s3_client().put_bucket_website(
        Bucket=WEBSITE_BUCKET_NAME,
        WebsiteConfiguration=website_configuration
    )

    index_file = os.path.dirname(__file__) + '/index.html'
    error_file = os.path.dirname(__file__) + '/error.html'

    s3_client().put_object(Bucket=WEBSITE_BUCKET_NAME, ACL='public-read', Key='index.html',
                           Body=open(index_file).read(), ContentType='text/html')
    s3_client().put_object(Bucket=WEBSITE_BUCKET_NAME, ACL='public-read', Key='error.html',
                           Body=open(error_file).read(), ContentType='text/html')


def route_53_record_for_s3_website():
    website_dns_name = "s3-website.eu-central-1.amazonaws.com"
    redirect_dns_name = "s3-website.eu-central-1.amazonaws.com"

    route53 = boto3.client('route53')
    """ :type : pyboto3.route53 """

    domain = WEBSITE_BUCKET_NAME
    www_redirect = 'www.' + WEBSITE_BUCKET_NAME

    change_batch_payload = {
        'Changes': [
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': domain,
                    'Type': 'A',
                    'AliasTarget': {
                        'HostedZoneId': 'Z21DNDUVLTQW6Q',
                        'DNSName': website_dns_name,
                        'EvaluateTargetHealth': False
                    }
                }
            },
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': www_redirect,
                    'Type': 'A',
                    'AliasTarget': {
                        'HostedZoneId': 'Z21DNDUVLTQW6Q',
                        'DNSName': redirect_dns_name,
                        'EvaluateTargetHealth': False
                    }
                }
            }
        ]
    }

    return route53.change_resource_record_sets(
        HostedZoneId='YOUR_OWN_HOSTED_ZONE_ID_ON_ROUTE_53',
        ChangeBatch=change_batch_payload
    )


if __name__ == '__main__':
    # print(create_bucket(BUCKET_NAME))
    # print(create_bucket_policy(BUCKET_NAME))
    # print(list_buckets())
    # parsed = get_bucket_policy()
    # print(json.dumps(parsed, indent=4))
    # print(get_bucket_encryption())
    # print(update_bucket_policy(BUCKET_NAME))
    # print(server_side_encrypt_bucket())
    # print(delete_bucket())
    print(upload_small_file())
    # upload_large_file()
    # print(read_object_from_bucket())
    # version_bucket_files()
    # upload_a_new_version()
    # put_lifecycle_policy()
    # host_static_website()
    # route_53_record_for_s3_website()
    # create_bucket(BUCKET_NAME)
