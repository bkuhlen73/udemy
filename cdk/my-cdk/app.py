#!/usr/bin/env python3

from aws_cdk import core

#from my_cdk.my_cdk_stack import MyCdkStack
from resource_stacks.custom_vpc import CustomVpcStack
from resource_stacks.custom_ec2 import CustomEc2Stack
from resource_stacks.custom_parameters_secrets import CustomParametersSecretsStack
from resource_stacks.custom_iam_users_groups import CustomIamUsersGroupsStack
from resource_stacks.custom_iam_roles_policies import CustomRolesPoliciesStack
from resource_stacks.custom_s3_resource_policy import CustomS3ResourcePolicyStack
from resource_stacks.custom_sns import CustomSnsStack
from resource_stacks.custom_sqs import CustomSqsStack
from app_stacks.web_server_stack import WebServerStack
from serverless_stacks.custom_lambda import CustomLambdaStack
from serverless_stacks.custom_cloudwatch_loggroups import CustomLoggroupStack
from serverless_stacks.custom_lambda_src_from_s3 import CustomLambdaSrcFromS3Stack
from serverless_stacks.custom_lambda_as_cron import CustomLambdaAsCronStack
from serverless_stacks.custom_dynamodb import CustomDynamoDBStack
from serverless_stacks.custom_privileges_to_lambda import CustomPrivilegesToLambdaStack
from serverless_stacks.custom_apigw import CustomApiGatewayStack
from monitoring_stacks.custom_ec2_with_alarms import CustomEc2WithAlarmsStack
from monitoring_stacks.custom_cloudwatch_metrics import CustomMetricsStack
from monitoring_stacks.custom_cloudwatch_live_dashboard import CustomCloudwatchLiveDashboardStack
from advanced_use_cases.deploy_static_site import DeployStaticSiteStack
from advanced_use_cases.deploy_cloudfront_oai_static_site import DeployCloudfrontOaiStaticSiteStack
from advanced_use_cases.serverless_event_processor_architecture_with_s3_events import ServerlessEventProcessorArchitectureWithS3EventsStack
from advanced_use_cases.serverless_rest_api_architecture import ServerlessRestApiArchitectureStack
from advanced_use_cases.serverless_data_stream_processor_architecture_with_kinesis import ServerlessStreamProcessorArchitectureWithKinesisStack
from advanced_use_cases.serverless_dynamo_event_processor_architecture_with_ddb_streams import ServerlessDdbStreamProcessorArchitectureWithSteamsStack
# VPC, EC2, ALB, RDS Stack
from app_db_stack.vpc_3tier_stack import Vpc3TierStack
from app_db_stack.web_server_3tier_stack import WebServer3TierStack
from app_db_stack.rds_3tier_stack import RdsDatabase3TierStack

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
#CustomParametersSecretsStack(app, "custom-parameters-secrets-stack", env=env_sandbox)

# # Custom Users and Groups
# CustomIamUsersGroupsStack(app, "custom-iam-users-groups-stack", env=env_sandbox)

# custom Roles and Policies
#CustomRolesPoliciesStack(app, "custom-iam-roles-policies-stack", env=env_sandbox)

# S3 Resource Policy
#CustomS3ResourcePolicyStack(app, "custom-s3-resource-policy-stack", env=env_sandbox)

# #Create 3Tier App with App Servers in ASG and Backend as RDS Database
# vpc_3tier_stack = Vpc3TierStack(app, "multi-tier-app-vpc-stack")
# app_3tier_stack = WebServer3TierStack(
#     app, "multi-tier-app-web-server-stack", vpc=vpc_3tier_stack.vpc)
# db_3tier_stack = RdsDatabase3TierStack(
#     app,
#     "multi-tier-app-db-stack",
#     vpc=vpc_3tier_stack.vpc,
#     asg_security_groups=app_3tier_stack.web_server_asg.connections.security_groups,
#     description="Create Custom RDS Database"
# )

# SNS
#CustomSnsStack(app, "custom-sns-topic-stack", env=env_sandbox)

# SQS
#CustomSqsStack(app, "custom-sqs-stack", env=env_sandbox)

# Serverless
#CustomLambdaStack(app, "custom-lambda-stack", env=env_sandbox)
#CustomLoggroupStack(app, "custom-logroup-stack", env=env_sandbox)
#CustomLambdaSrcFromS3Stack(app, "custom-lambda-src-from-s3", env=env_sandbox)
#CustomLambdaAsCronStack(app, "custom-lambda-as-cron-stack", env=env_sandbox)
#CustomDynamoDBStack(app, "custom-dynamodb-stack", env=env_sandbox)
#CustomPrivilegesToLambdaStack(app, "custom-privileges-to-lambda-stack", env=env_sandbox)
#CustomApiGatewayStack(app,"custom-apigw-stack", env=env_sandbox)

#Monitoring
#CustomEc2WithAlarmsStack(app,"custom-ec2-with-alarms-stack", env=env_sandbox)
#CustomMetricsStack(app,"custom-metrics-stack", env=env_sandbox)
#CustomCloudwatchLiveDashboardStack(app,"custom-cloudwatch-live-dashboard", env=env_sandbox)

#Advanced
#DeployStaticSiteStack(app,"custom-static-site", env=env_sandbox)
#DeployCloudfrontOaiStaticSiteStack(app, "custom-static-cloudfront-oai-site", env=env_sandbox)
#ServerlessEventProcessorArchitectureWithS3EventsStack(app,"custom-serverless-event-processor-arch-with-s3-events", env=env_sandbox)
#ServerlessRestApiArchitectureStack(app,"custom-serverlesss-rest-api-arch", env=env_sandbox)
#ServerlessStreamProcessorArchitectureWithKinesisStack(app,"custom-serverless-processor-arch-with-kinesis-stack", env=env_sandbox)
ServerlessDdbStreamProcessorArchitectureWithSteamsStack(app,"custom-serverless-dynamodb-stream-processor-arch", env=env_sandbox)
core.Tag.add(app, key="stack-team-support-email",
             value=app.node.try_get_context('envs')['sandbox']['support_email'])

app.synth()
# print(app.node.try_get_context('sandbox')['region'])
