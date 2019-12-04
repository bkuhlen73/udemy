#!/usr/bin/env python3

import boto3
session = boto3.session.Session(profile_name="sandbox")
ec2_con_re = session.resource(service_name="ec2", region_name="us-east-1")

in_id = input("Enter your instance id: ")

my_instance = ec2_con_re.Instance(id=in_id)

print(my_instance.tags)
