#!/usr/bin/env python3
import boto3

session = boto3.session.Session(profile_name="sandbox")

ec2_con_re = session.resource(service_name="ec2", region_name="us-east-1")

f1 = {"Name": "availability-zone", "Values": ['us-east-1b']}
f2 = {"Name": "instance-state-name", "Values": ['running']}
for each_in in ec2_con_re.instances.filter(Filters=[f1, f2]):
    print(each_in.id, each_in.state)

# Filters using tags:
ftags = {"Name": 'tag:Name', "Values": [
    'EKS-course-cluster-eks-course-nodegroup-Node']}


for each_in in ec2_con_re.instances.filter(Filters=[ftags]):
    print(each_in.id, each_in.state)
