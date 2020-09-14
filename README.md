# efficient-learning-lambda
Backend system to support the Quizzes feature in BBC Bitesize

The following documentation is available:

 - [Development Environment](./devdocs/DevelopmentEnvironment.md)
 - [Continuous Deployment](./devdocs/ContinuousDeployment.md)
 - [Infrastructure](./devdocs/Infrastructure.md)


## PreRequisites

### Python 3

To install Python 3 visit https://www.python.org/downloads/mac-osx/ for instructions.

### Pip

This is the python package manager and is needed to install virtualenv and other Python packages:

Instructions on how to do this can be found here: https://pip.pypa.io/en/stable/installing/

### VirtualEnv

VirtualEnv is a virtual environment manager for Python that allows packages to be installed in isolated environments.

You should be able to install this using pip/pip3 install virtualenv

### AWS SAM CLI
SAM is used to build and run the lambda locally. Sam can be used for other tasks such as deployment however we will not be using it for this purpose.
Instructions on how to install SAM can be found here : https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html 

### Configuring AWS Credentials

Edit the aws-configuration.sh to include an AWS_ACCOUNT_NUMBER and then run the following:

```
$ ./scripts/aws-configuration.sh
```
Your credentials should now be configured and the path to it is ~/.aws/credentials

## Getting Started

There is a Makefile which shows all available tasks whiich can be executed for this lambda including testing and linting.

Before doing anything, the dependecies must be installed using virtualenv

```
$ make venv
```

This should generate a `venv/` directory in the root.

### Running the Lambda

```
$ make build-lambda
$ make run-lambda
```
This should show the lambda being invoked liked so:

```
efficient-learning-lambda on  BITESIZE-12607/Create-skeleton-python-lambda [?] via 🐍 system took 2s
➜ make run-lambda
sam local invoke -e events/event.json LambdaFunction --docker-network host
Invoking app.handler (python3.7)
Failed to download a new amazon/aws-sam-cli-emulation-image-python3.7:rapid-1.0.0 image. Invoking with the already downloaded image.
Mounting /Users/antonj04/Workspace/git/efficient-learning-lambda/.aws-sam/build/LambdaFunction as /var/task:ro,delegated inside runtime container
START RequestId: 7848c912-9618-1117-e563-b8aa2b5fc672 Version: $LATEST
{'message': 'This is an Event!'}
<bootstrap.LambdaContext object at 0x7fcd6f2a7510>
END RequestId: 7848c912-9618-1117-e563-b8aa2b5fc672
REPORT RequestId: 7848c912-9618-1117-e563-b8aa2b5fc672	Init Duration: 287.57 ms	Duration: 4.52 ms	Billed Duration: 100 ms	Memory Size: 128 MB	Max Memory Used: 22 MB

{"message":"This is an Event!"}
```

## Testing

Before doing anything, the dependecies must be installed using virtualenv

```
$ make venv
```

Run the Unit Tests via 
```
$ make test
```
