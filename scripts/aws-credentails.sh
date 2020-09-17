#!/bin/bash

curl --version

AWS_ACCOUNT_NUMBER=192774014475

if [ -z $AWS_ACCOUNT_NUMBER ]; then
printf "\e[31mError:\e[0m Invalid account"
return 0
fi

AWS_LOGIN_CREDENTIAL=$(curl ~/.curlrc -s https://wormhole.api.bbci.co.uk/account/$AWS_ACCOUNT_NUMBER/credentials)

AWS_ACCESS_KEY_ID=$(echo $AWS_LOGIN_CREDENTIAL | jq -r .accessKeyId)
AWS_SECRET_KEY=$(echo $AWS_LOGIN_CREDENTIAL | jq -r .secretAccessKey)
AWS_SECURITY_TOKEN=$(echo $AWS_LOGIN_CREDENTIAL | jq -r .sessionToken)

aws configure set default.region eu-west-1
aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
aws configure set aws_secret_access_key $AWS_SECRET_KEY
aws configure set aws_session_token $AWS_SECURITY_TOKEN