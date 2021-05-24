"""
AWS Lab1 from the Master Reply/Polito
"""
#!/usr/bin/env python3

from aws_cdk import core

from stacks.vpc_stack import CdkVpcStack
from stacks.ec2_stack import CdkEc2Stack
from stacks.aurora_stack import CdkRdsStack

app = core.App(outdir="./cdk.out")

vpc_stack = CdkVpcStack(app, "cdk-vpc")
ec2_stack = CdkEc2Stack(app, "cdk-ec2",
                        vpc=vpc_stack.vpc)
rds_stack = CdkRdsStack(app, "cdk-aurora",
                        vpc=vpc_stack.vpc,
                        asg_security_groups=ec2_stack.asg.connections.security_groups)

print(app.outdir)
app.synth()