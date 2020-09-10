from aws_cdk import core

class CustomParametersSecretsStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        sandbox_configs = self.node.try_get_context('envs')['sandbox']

        