#!/usr/bin/env python3
import boto3

session = boto3.session.Session(profile_name="sandbox")
sts_client = session.client("sts")

print(sts_client.get_caller_identity().get('Account'))
print(sts_client.get_caller_identity())
