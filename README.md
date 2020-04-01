# RootAccess-login-tracker

Track AWs root login. A cloudwatch rule will be deployed in all accounts through stacksets, which tracks and notifies.

# Architecture diagram.

![](./images/Root_login_architecture.png?raw=true "")

## Quick Start
The below instructions are to install and deploy applications using Serverless Framework and AWS provider.

### Prerequisites
Install prerequisites:

	1.  Node.js
	2.  Serverless
	3.  An AWS  account with providers credentials

### Installation

**Installing Node.js**

Serverless is a [Node.js] (https://nodejs.org/en/) CLI tool, install node.js before dive into Serverless.

The platform specific version of nodejs can be download from [here](https://nodejs.org/en/download/) .

**Installing the Serverless Framework**

Install the Serverless Framework via npm command.

Type the following commands in terminal to install Serverless.

    npm install -g serverless

In order to check the version of installed serverless cli, follow the below command

    serverless --version

**Setting up AWS credentials**

To run serverless commands that interface with AWS account, to setup AWS account credentials on your machine.

[Follow these instruction on setting up AWS credential](https://serverless.com/framework/docs/providers/aws/guide/credentials/)
aws configure

## Deployments

**Instructions**

1. Before deploying the solution, make sure 'serverless-python-requirements' is installed.

2. 'serverless-python-requirements' plugin will automatically bundle the dependencies by reading from requirements.txt.

3. If the solution is deployed in local machine a virtual environment can be set up, please find the [instruction](https://serverless.com/blog/serverless-python-packaging/) to setup a virtual environment.

**Install 'serverless-python-requirements' plugin .**

    serverless plugin install -n serverless-python-requirements --aws-profile <profile-name>
    Example: serverless plugin install -n serverless-python-requirements --aws-profile Cerner-Duo

**Deploy the serverless project to cloud with profile name**

    serverless deploy --aws-profile <profile-name> --stage <dev/prod> --region <region-name>
    Example: serverless deploy --aws-profile Cerner-Duo --stage dev --region us-east-1

Deployment output

    Serverless: Generated requirements from github/RootAccess-tracker/requirements.txt in github/RootAccess-tracker/.serverless/requirements.txt...
    Serverless: Installing requirements from github/RootAccess-tracker/.serverless/requirements/requirements.txt ...
    Serverless: Packaging service...
    Serverless: Excluding development dependencies...
    Serverless: Injecting required Python packages to package...
    Serverless: Uploading CloudFormation file to S3...
    Serverless: Uploading artifacts...
    Serverless: Uploading service .zip file to S3 (263.44 KB)...
    Serverless: Validating template...
    Serverless: Creating Stack...
    Serverless: Checking Stack create progress...
    ....................
    Serverless: Stack create finished...
    Service Information
    service: RootAccess-tracker
    stage: dev
    region: us-east-1
    stack: RootAccess-tracker-dev
    api keys:
      None
    endpoints:
      None
    functions:
      root-access-tracker: RootAccess-tracker-dev-root-access-tracker
    layers:
      None
### Deploy stackset:

To deploy stack into other account, please goto cloudformation -->stackset-->create stackset, upload the cf file from the repo, and give the 
account name and region to be deployed, the stack should be created successfully.
