#!/usr/bin/env python3
import boto3

session = boto3.session.Session(profile_name='sandbox')

bucket_name = 'wobk-testbucket'
cnt = 1
s3_cli = session.client(service_name='s3', region_name='us-east-1')
paginator = s3_cli.get_paginator('list_objects')
for each_page in paginator.paginate(Bucket=bucket_name):
    for each_object in each_page['Contents']:
        print(cnt, each_object['Key'])
        cnt = cnt + 1
