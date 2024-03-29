import boto3

client = boto3.client('ec2', region_name='eu-central-1')
resp = client.describe_instances()

print(resp)

for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        print("InstanceId is {} ".format(instance['InstanceId']))
