# Overview

The Efficient Learning infrastructure stacks documentation

# Stacks

## EfficientLearningLambdaFunction

### Parameters
| Parameter                | Description                                                                |
| ------------------------ | -------------------------------------------------------------------------- |
| LambdaEnv                | Environment the lambda is deployed to, used for Cosmos alias, test or live |
| LambdaMemorySize         | Amount of memory to allocate to the Lambda Function                        |
| LambdaTimeout            | Timeout in seconds for the Lambda function                                 |
| QuestionsBucketArn       | Arn of the bucket the lambda fetches data from                             |
| PythonLayer              | Arn of the Python Layer containing lambda dependencies                     |

### Outputs
| Output               | Description                                       |
| -------------------- | ------------------------------------------------- |
| EfficientLearningFunctionArn | The Arn of the lambda function |
| EfficientLearningRoleArn | The Role which grants permissions to the lambda|

### Policies
| Policy   | Description                                       |
| -------- | ------------------------------------------------- |
| AllowLoggingPolicy | Allows the lambda to provide logs  |
| AllowS3Policy | Allows the lambda access to the S3 bucket |

## Infrastructure Development

You will need the following installed:

### Python 3

To install Python 3 visit https://www.python.org/downloads/mac-osx/ for instructions.

### Pip

This is the python package manager and is needed to install virtualenv and other Python packages:

Instructions on how to do this can be found here: https://pip.pypa.io/en/stable/installing/

### VirtualEnv

VirtualEnv is a virtual environment manager for Python that allows packages to be installed in isolated environments.

You should be able to install this using `pip3 install virtualenv`

__Note: You need version 20.0.0 or greater__

If you have any issues see here for further instructions on installing: https://virtualenv.pypa.io/en/latest/

For pip if you have a version older than v20.0.0 install, run ```pip3 install --upgrade virtualenv```

### Troposphere

We are using Troposphere for the CloudFormation templates:

https://github.com/cloudtools/troposphere

As part of the make script troposphere will be installed

### Generating the Stack Templates

The infastructure hold the src to generate the stack template and the generated templates that can depolyed via cosmos.

To generate new templates from the src files run the below command in the root of the project.

```make build-infra```

This will generate all the template json files in the /infastructure/templates folder.

### Deploying to Cosmos

To deploy changes to the stack the Cosmos UI needs to be used.

1. Go to https://cosmos.tools.bbc.co.uk/lambdas/efficient-learning-lambda
1. Select the Stacks option for the environment you want to update
1. Select the stack you want to update
1. Delete the existing JSON and paste in the contents of the file created above
1. Click 'Update Stack'
1. The stack update progress can then be viewed on the AWS Console in the CloudFormation service

#### Required Config Values in Cosmos

S3_BUCKET - Arn of the S3 Bucket the lambda fetches data from.