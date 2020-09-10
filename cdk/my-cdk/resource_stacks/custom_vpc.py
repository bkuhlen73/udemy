from aws_cdk import ( 
    aws_ec2 as _ec2,
    aws_s3 as _s3,
    core
)

class CustomVpcStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        sandbox_configs = self.node.try_get_context('envs')['sandbox']

        custom_vpc = _ec2.Vpc(
            self,
            "customVpcId",
            cidr=sandbox_configs['vpc_configs']['vpc_cidr'],
            max_azs=2,
            nat_gateways=1,
            subnet_configuration=[
                _ec2.SubnetConfiguration(
                    name="publicSubnet", cidr_mask=sandbox_configs['vpc_configs']['cidr_mask'], subnet_type=_ec2.SubnetType.PUBLIC
                ),
                _ec2.SubnetConfiguration(
                    name="privateSubnet", cidr_mask=sandbox_configs['vpc_configs']['cidr_mask'], subnet_type=_ec2.SubnetType.PRIVATE
                ),
                _ec2.SubnetConfiguration(
                    name="dbSubnet", cidr_mask=sandbox_configs['vpc_configs']['cidr_mask'], subnet_type=_ec2.SubnetType.ISOLATED
                )
            ]
        )

        core.Tag.add(custom_vpc, "Owner", "bernd.kuhlen@wetteronline.de")

        #resource in same account
        bkt1 = _s3.Bucket.from_bucket_name(
            self,
            "MyImportedBucket",
            "wobk-testbucket"
        )

        

        vpc2 = _ec2.Vpc.from_lookup(self,
                                    "importedVPC",
                                    vpc_id="vpc-bc62dbc6")

        core.CfnOutput(self,
                        "customVpcOutput",
                        value=custom_vpc.vpc_id,
                        export_name="customVpcId"
        )

        core.CfnOutput(self,
                        "importedVpc2",
                        value=vpc2.vpc_id,
        )

        peer_vpc = _ec2.CfnVPCPeeringConnection(self,
                                                "peerVpc12",
                                                peer_vpc_id=custom_vpc.vpc_id,
                                                vpc_id=vpc2.vpc_id)

        core.CfnOutput( self,
                        "myimportedbucket",
                        value=bkt1.bucket_name)
