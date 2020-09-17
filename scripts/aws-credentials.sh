#!/bin/bash

curl --version

AWS_LOGIN_CREDENTIAL=$(curl ~/.curlrc -s)

AWS_ACCESS_KEY_ID=$(python <<< "print($AWS_LOGIN_CREDENTIAL['accessKeyId'])")
AWS_SECRET_KEY=$(python <<< "print($AWS_LOGIN_CREDENTIAL['secretAccessKey'])")
AWS_SECURITY_TOKEN=$(python <<< "print($AWS_LOGIN_CREDENTIAL['sessionToken'])")

aws configure set default.region eu-west-1
aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
aws configure set aws_secret_access_key $AWS_SECRET_KEY
aws configure set aws_session_token $AWS_SECURITY_TOKEN
