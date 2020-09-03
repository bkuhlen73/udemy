import boto3
client = boto3.client('ec2', region_name='eu-central-1')

resp = client.terminate_instances(InstanceIds=['i-02608fce70b4d3447'])

print(resp)

for instance in resp['TerminatingInstances']:
    print("The instance with id {} Terminated".format(instance['InstanceId']))

