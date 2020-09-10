from aws_cdk import ( 
    aws_s3 as _s3,
    aws_kms as _kms,
    core
)

class MyCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        _s3.Bucket(
            self,
            "myBucketId",
            bucket_name="mycdk-stack-0815", 
            versioned=False,
            encryption=_s3.BucketEncryption.S3_MANAGED,
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL
        )

        mybucket = _s3.Bucket(
            self,
            "myBucketId2"
        )

        # snstopicname = "abcdef1234567890"

        # if not core.Token.is_unresolved(snstopicname) and len(snstopicname) > 10:
        #     raise ValueError("Maximum value can be only 10 chars")

        output_1 = core.CfnOutput(
            self,
            "MyBucketOutput1",
            value = mybucket.bucket_name,
            description=f"My first CDK Bucket",
            export_name="myBucketOutput1"
        ) 
        # The code that defines your stack goes here
