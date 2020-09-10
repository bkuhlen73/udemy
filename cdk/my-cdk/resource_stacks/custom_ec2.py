from aws_cdk import (
    aws_ec2 as _ec2,
    aws_iam as _iam,
    core
)


class CustomEc2Stack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = _ec2.Vpc.from_lookup(self,
                                   "importedVPC",
                                   vpc_id="vpc-bc62dbc6")

        # Read BootStrap Script
        with open("bootstrap_scripts/install_httpd.sh", mode="r") as file:
            user_data = file.read()

        # Get the latest ami
        amzn_linux_ami = _ec2.MachineImage.latest_amazon_linux(
            generation=_ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=_ec2.AmazonLinuxEdition.STANDARD,
            storage=_ec2.AmazonLinuxStorage.EBS,
            virtualization=_ec2.AmazonLinuxVirt.HVM
        )

        # Webserver Instance 001
        web_server = _ec2.Instance(self,
                                   "webServer001Id",
                                   instance_type=_ec2.InstanceType(
                                       instance_type_identifier="t2.micro"),
                                   instance_name="WebServer001",
                                   # machine_image=_ec2.MachineImage.generic_linux(
                                   #     {"us-east-1": "ami-0c94855ba95c71c99"}
                                   # ),
                                   machine_image=amzn_linux_ami,
                                   vpc=vpc,
                                   vpc_subnets=_ec2.SubnetSelection(
                                       subnet_type=_ec2.SubnetType.PUBLIC
                                   ),
                                   user_data=_ec2.UserData.custom(user_data)
                                   )

        # Add EBS with provisioned IOPS Storage
        web_server.instance.add_property_override(
            "BlockDeviceMappings", [
                {
                    "DeviceName": "/dev/sdb",
                    "Ebs": {
                        "VolumeSize": "8",
                        "VolumeType": "io1",
                        "Iops": "400",
                        "DeleteOnTermination": "true"
                    }
                }
            ]
        )

        output_1 = core.CfnOutput(self,
                                  "webServer001Ip",
                                  description="WebServer 001 Public Ip Adress",
                                  value=f"http://{web_server.instance_public_ip}")

        # Allow Incoming Traffic to WebServer
        web_server.connections.allow_from_any_ipv4(
            _ec2.Port.tcp(80), description="Allow Web Traffic"
        )

        # Add permission to web server instance profile

        web_server.role.add_managed_policy(
            _iam.ManagedPolicy.from_aws_managed_policy_name(
                "AmazonSSMManagedInstanceCore"
            )
        )

        web_server.role.add_managed_policy(
            _iam.ManagedPolicy.from_aws_managed_policy_name(
                "AmazonS3ReadOnlyAccess"
            )
        )
