#!/usr/bin/env python3
import boto3
import time
session = boto3.session.Session(profile_name="sandbox")
ec2_re = session.resource(service_name="ec2", region_name="us-east-1")
id = input("instance id, please ")
my_in = ec2_re.Instance(id=id)
my_in.start()
my_in.wait_until_running()
