from troposphere import Template, Output, Ref, GetAtt, Parameter, Join, Export
from troposphere.constants import NUMBER, STRING
from troposphere.awslambda import Function, Code, MEMORY_VALUES, EventSourceMapping, Alias, Environment
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

questionsBucketName = template.add_parameter(Parameter(
    'QuestionsBucketName',
    Type=STRING,
    Description='Bucket name (minus ARN)',
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

questionsFolder = template.add_parameter(Parameter(
    "QuestionsFolder",
    Default="quizzes/questions",
    Description="Location of the questions in the S3 bucket",
    Type="String",
))

configFolder = template.add_parameter(Parameter(
    "ConfigFolder",    
    Default="quizzes/config",
    Description="Location of the config in the S3 bucket",
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
        Ref(pythonLayer),
        "arn:aws:lambda:eu-west-1:580247275435:layer:LambdaInsightsExtension:1"
    ],
    Runtime="python3.7",
    Environment=Environment(
        Variables={
            "S3_BUCKET": Ref(questionsBucketName),
            "S3_CONFIG": Ref(configFolder),
            "S3_FOLDER": Ref(questionsFolder)
        }
    ),
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
    Export=Export("efficient-learning-function-arn"),
    Value=GetAtt(efficientLearningFunction, "Arn"),
    Description="Function to generate speech files"
))

template.add_output(Output(
    "EfficientLearningRoleArn",
    Export=Export("efficient-learning-role-arn"),
    Value=GetAtt(lambdaExecutionRole, "Arn"),
    Description="Role to grant permissions needed to generate speech files"
))

print(template.to_json())
