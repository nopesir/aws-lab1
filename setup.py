"""
SETUP
"""
import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="LAB1 Master",
    version="1.0.0",

    description="Create new VPC with an Autoscaling Web Server layer. Then, Publish it and benchmark it and Optimize the architecture with caching",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Ferrettino, Luigi",

    package_dir={"": "stacks"},
    packages=setuptools.find_packages(where="stacks"),

    install_requires=[
        "aws-cdk.core",
        "aws-cdk.aws-ec2",
        "aws-cdk.aws-elasticloadbalancingv2",
        "aws-cdk.aws-autoscaling",
        "aws-cdk.aws-rds",
        "aws_cdk.aws_elasticache"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)