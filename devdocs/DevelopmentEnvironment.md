# Overview

The Efficient Learning development environments documentation.

## PreRequisites

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

### AWS SAM CLI

SAM is used to build and run the lambda locally. Sam can be used for other tasks such as deployment however we will not be using it for this purpose.
Instructions on how to install SAM can be found here : https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html

You will also need to configure the AWS CLI.

You will need a `.curlrc` file in the home directory to supply your BBC AWS credentials. This file will look like : 

```
cacert=/etc/pki/tls/certs/ca-bundle.crt
cert=/etc/pki/certificate.pem
```

You can then add the AWS_ACCOUNT_NUMBER in `./scripts/aws-configuration.sh` and running the following :

```
$ ./scripts/aws-configuration.sh
```

You should see your credentials configured `.~/.aws/credentials`

## Getting Started

There is a Makefile which shows all available tasks whiich can be executed for this lambda including testing and linting.

Before doing anything, the dependecies must be installed using virtualenv

```
$ make venv
```

This should generate a `venv/` directory in the root.

### Running the Lambda


Before building and running the lambda you will need to add any Environment Variables in the `template.yaml` file

```
$ make build-lambda
$ make run-lambda
```

### Testing


To run the Unit Tests use the following :

```
$ make test
```
