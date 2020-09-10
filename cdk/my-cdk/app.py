#!/usr/bin/env python3

from aws_cdk import core

#from my_cdk.my_cdk_stack import MyCdkStack
from resource_stacks.custom_vpc import CustomVpcStack
from resource_stacks.custom_ec2 import CustomEc2Stack
from resource_stacks.custom_parameters_secrets import CustomParametersSecretsStack
from app_stacks.web_server_stack import WebServerStack


app = core.App()
#MyCdkStack(app, "my-cdk")

env_sandbox = core.Environment(account="085415390296", region="us-east-1")

# #Custom VPC Stack
# CustomVpcStack(app, "my-custom-vpc-stack",
#                 env=core.Environment(account=app.node.try_get_context('envs')['sandbox']['account'], 
#                 region=app.node.try_get_context('envs')['sandbox']['region']))

# #Custom EC2 Stack
# CustomEc2Stack(app, "my-web-server-stack", env=env_sandbox)

# #Custom Web Server Stack
# WebServerStack(app, "my-web-server-alb-stack", env=env_sandbox)

# # Custom Parameters Secrets
# CustomParametersSecretsStack(app, "custom-parameters-secrets-stack", env=env_sandbox)

# Custom Users and Groups
CustomIamUsersGroupsStack(app, "custom-users-groups-stack", env=env_sandbox)

core.Tag.add(app, key="stack-team-support-email", value=app.node.try_get_context('envs')['sandbox']['support_email'])

app.synth()
#print(app.node.try_get_context('sandbox')['region'])