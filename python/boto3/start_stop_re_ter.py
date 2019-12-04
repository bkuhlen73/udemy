#!/usr/bin/env python3
import boto3
session = boto3.session.Session(profile_name="sandbox")
ec2_con_re = session.resource(service_name="ec2", region_name="us-east-1")
instance = input("your ec2 id please: ")
my_inst = ec2_con_re.Instance(id=instance)
# print dir(my_inst)
my_inst.start()
# my_inst.stop()
