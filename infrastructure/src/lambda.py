from troposphere import Template, Output, Ref, GetAtt, Parameter, Join
from troposphere.constants import NUMBER, STRING
from troposphere.awslambda import Function, Code, MEMORY_VALUES, EventSourceMapping, Alias
from troposphere.iam import Role, Policy

FUNCTION_NAME="EfficientLearningFunction"

template = Template()

template.set_description("Lambda part of Intelligent Learning Experience to generate quizz questions and mastery scores")

timeout = template.add_parameter(Parameter(
    'LambdaTimeout',
    Type=NUMBER,
    Description='Timeout in seconds for the Lambda function',
    Default='20'
))

memorySize = template.add_parameter(Parameter(
    'LambdaMemorySize',
    Type=NUMBER,
    Description='Amount of memory to allocate to the Lambda Function',
    Default='128',
    AllowedValues=MEMORY_VALUES
))

questionsBucket = template.add_parameter(Parameter(
    'QuestionsBucket',
    Type=STRING,
    Description='ARN of the bucket where the questions are stored'
))

pythonLayer = template.add_parameter(Parameter(
    "PythonLayer",
    Default="arn:aws:lambda:eu-west-1:399891621064:layer:AWSLambda-Python37-SciPy1x:37",
    Description="ARN of AWS Python Lambda Layer",
    Type="String",
))

env = template.add_parameter(Parameter(
    "LambdaEnv",
    Default="test",
    Description="Environment this lambda represents - used for alias name",
    Type="String",
))

lambdaExecutionRole = template.add_resource(Role(
    "EfficientLearningRole",
    Path="/",
    Policies=[
        Policy(
            PolicyName="AllowLoggingPolicy",
            PolicyDocument={
                "Version": "2012-10-17",
                "Statement": [{
                    "Action": ["logs:*"],
                    "Resource": "arn:aws:logs:*:*:*",
                    "Effect": "Allow"
                }]
        }),
        Policy(
            PolicyName="AllowS3Policy",
            PolicyDocument={
                "Version": "2012-10-17",
                "Statement": [{
                    "Effect": "Allow",
                    "Action": "s3:GetObject",
                    "Resource": [
                        Ref(questionsBucket),
                        Join("", [Ref(questionsBucket), "/*"])
                    ]
                }]
        })],
    AssumeRolePolicyDocument={
        "Version": "2012-10-17",
        "Statement": [{
            "Action": ["sts:AssumeRole"],
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "lambda.amazonaws.com",
                ]
            }
        }]
    },
))

efficientLearningFunction = template.add_resource(Function(
    FUNCTION_NAME,
    FunctionName=FUNCTION_NAME,
    Description="Lambda returns quizz questions and mastery scores ",
    Handler="index.handler",
    Role=GetAtt(lambdaExecutionRole, "Arn"),
    Layers=[
        Ref(pythonLayer)
    ],
    Runtime="python3.7",
    MemorySize=Ref(memorySize),
    Timeout=Ref(timeout),
    Code=Code(
        ZipFile="$LATEST"
    ),
))

alias = template.add_resource(Alias(
    "LambdaAlias",
    Description="Cosmos Alias",
    FunctionName=Ref(efficientLearningFunction),
    FunctionVersion="$LATEST",
    Name=Ref(env)
))


template.add_output(Output(
    "EfficientLearningFunctionArn",
    Value=GetAtt(efficientLearningFunction, "Arn"),
    Description="Function to generate speech files"
))

template.add_output(Output(
    "EfficientLearningRoleArn",
    Value=GetAtt(lambdaExecutionRole, "Arn"),
    Description="Role to grant permissions needed to generate speech files"
))

print(template.to_json())
