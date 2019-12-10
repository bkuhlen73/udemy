#!/usr/bin/env python3
import boto3
from pprint import pprint

session = boto3.session.Session(profile_name="sandbox")

ec2_client = session.client(service_name="ec2", region_name="us-east-1")
list_of_volids = []
myfilter = {"Name": "tag:Prod", "Values": ["Backup"]}
# for each_vol in ec2_client.describe_volumes(Filters=[myfilter])['Volumes']:
#     list_of_volids.append(each_vol['VolumeId'])

# print(ec2_client.describe_volumes(Filters=[myfilter]))

paginator = ec2_client.get_paginator('describe_volumes')
for each_page in paginator.paginate(Filters=[myfilter]):
    print(each_page)
    for each_vol in each_page['Volumes']:
        list_of_volids.append(each_vol['VolumeId'])


print("The list of volids are: ", list_of_volids)
snapids = []
for each_volid in list_of_volids:
    res = ec2_client.create_snapshot(
        Description="Taking snap with Lambda and cw",
        VolumeId=each_volid,
        TagSpecifications=[
            {
                    'ResourceType': 'snapshot',
                'Tags': [
                    {
                        'Key': 'Delete-on',
                        'Value': '90'
                    },
                    {
                        'Key': 'backup',
                        'Value': 'yes'
                    }
                ]
            }
        ]
    )
    snapids.append(res.get('SnapshotId'))

print("The snap ids are: ", snapids)


waiter = ec2_client.get_waiter('snapshot_completed')
waiter.wait(SnapshotIds=snapids)

print("Successfully completed snaps for the volumes of {}".format(list_of_volids))
