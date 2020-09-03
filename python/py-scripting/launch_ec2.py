import boto3
client = boto3.client('ec2', region_name='eu-central-1')

resp = client.run_instances(ImageId='ami-077d109dee4cdf8cf',
                     InstanceType='t2.micro',
                     MinCount=1,
                     MaxCount=1)
for instance in resp['Instances']:
    print(instance['InstanceId'])