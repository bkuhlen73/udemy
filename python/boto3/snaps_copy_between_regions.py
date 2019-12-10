#!/usr/bin/env python3

import os
import sys
try:
    import boto3
    print("Imported boto3 sucessfully")
except Exception as e:
    print(e)
    sys.exit(1)

source_region = 'us-east-1'
dest_region = 'us-east-2'

session = boto3.session.Session(profile_name="sandbox")
ec2_source_client = session.client(
    service_name='ec2', region_name=source_region)

sts_client = session.client(service_name='sts', region_name='us-east-1')
account_id = sts_client.get_caller_identity().get('Account')
f_bkp = {'Name': 'tag:backup', 'Values': ['yes']}
bkp_snap = []

for each_snap in ec2_source_client.describe_snapshots(OwnerIds=[account_id], Filters=[f_bkp]).get('Snapshots'):
    # print(each_snap.get('SnapshotId'))
    bkp_snap.append(each_snap.get('SnapshotId'))

ec2_dest_client = session.client(service_name='ec2', region_name=dest_region)

for each_source_snapid in bkp_snap:
    print(
        f'Taging backup for id of {each_source_snapid} into region {dest_region}')
    ec2_dest_client.copy_snapshot(
        Description='For Disaster recovery',
        SourceRegion=source_region,
        SourceSnapshotId=each_source_snapid
    )

print("EBS Snapshot copy to destination region is completed")
print("Modifying tags for the snapshots in the source region")

for each_source_snapid in bkp_snap:
    # print(f"Deleting old tags for {each_source_snapid}")
    # ec2_source_client.delete_tags(
    #     Resources=[each_source_snapid],
    #     Tags=[
    #         {
    #             'Key': 'backup',
    #             'Value': 'yes'
    #         }
    #     ]
    # )
    print(f"Creating new tags for {each_source_snapid}")
    ec2_source_client.create_tags(
        Resources=[each_source_snapid],
        Tags=[
            {
                'Key': 'backup',
                'Value': 'yes'
            }
        ]
    )
