"""
Aurora stack
"""
from aws_cdk import core
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_rds as rds
import aws_cdk.aws_elasticache as ec


class CdkRdsStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, vpc, asg_security_groups, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Ceate Aurora Cluster with 2 instances with CDK High Level API
        # Secrets Manager auto generate and keep the password, don't put password in cdk code directly
        db_Aurora_cluster = rds.DatabaseCluster(self, "MyAurora",
                                                default_database_name="MyAurora",
                                                engine=rds.DatabaseClusterEngine.aurora_mysql(
                                                    version=rds.AuroraMysqlEngineVersion.VER_5_7_12
                                                ),
                                                instance_props=rds.InstanceProps(
                                                    vpc=vpc,
                                                    vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.ISOLATED),
                                                    instance_type=ec2.InstanceType(instance_type_identifier="t2.small")
                                                ),
                                                instances=2,
                                                parameter_group=rds.ParameterGroup.from_parameter_group_name(
                                                    self, "para-group-aurora",
                                                    parameter_group_name="default.aurora-mysql5.7"
                                                ),
                                                )
        for asg_sg in asg_security_groups:
            db_Aurora_cluster.connections.allow_default_port_from(asg_sg, "EC2 Autoscaling Group access Aurora")
            
        ec_Memcached_cluster = ec.CfnCacheCluster(self, "Wordpress-Memcached",
                                                  engine="memcached",
                                                  cluster_name="Wordpress-Memcached",
                                                  az_mode="cross-az",
                                                  cache_node_type ="cache.t2.small",
                                                  num_cache_nodes=1,
                                                  port=11211
                                                 )
