#!/bin/bash
set -eo pipefail
FUNCTION=$(aws cloudformation describe-stack-resource --stack-name nl-news --logical-resource-id function --query 'StackResourceDetail.PhysicalResourceId' --output text)

while true; do
  aws lambda invoke --function-name $FUNCTION --payload fileb://event.json out.json
  cat out.json
  echo ""
  sleep 2
done

arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole\",\
arn:aws:iam::aws:policy/AWSXrayWriteOnlyAccess\"
\"AWSLambdaReadOnlyAccess\"