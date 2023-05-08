# Lab for Serverless

##  Overview And High-Level Design

In this lab, we will create a serverless API using Amazon API Gateway, AWS Lambda, and DynamoDB. The API will perform various operations on a DynamoDB table, such as create, read, update, and delete items. The high-level design of the solution is as follows:


## Arichitecture



The key architecture components of the serverless API using Amazon API Gateway, AWS Lambda, and DynamoDB are as follows:

1. Amazon API Gateway: It acts as the entry point for the API, allowing clients to interact with the backend services. API Gateway provides features such as request routing, authentication, and rate limiting. It integrates with Lambda functions to process API requests.

2. AWS Lambda: It is a serverless compute service that allows you to run code without provisioning or managing servers. In this architecture, Lambda functions serve as the backend for the API. They handle the business logic and interact with DynamoDB to perform CRUD operations.

3. DynamoDB: It is a fully managed NoSQL database service provided by AWS. DynamoDB is used to store and retrieve data for the API. It provides scalability, high availability, and low-latency performance for read and write operations.

4. IAM Roles: IAM roles are used to provide permissions to the Lambda function to access AWS resources. In this case, an IAM role is created and associated with the Lambda function to grant it access to DynamoDB and CloudWatch Logs.

5. API Gateway Resource and Method: API Gateway allows you to define resources and methods to structure your API. In this architecture, a single resource named "DynamoDBManager" is created, and it has a single method "POST" associated with it. This method is integrated with the Lambda function to handle API requests.

6. Request Payload: The API requests sent to the API Gateway include a payload in JSON format. The payload specifies the DynamoDB operation to be performed (e.g., create, read, update, delete) and provides the necessary data for the operation.

7. Lambda Function Logic: The Lambda function is responsible for processing the API requests and performing the corresponding DynamoDB operations based on the payload. It uses the AWS SDK for Python (Boto3) to interact with DynamoDB and execute the requested operations.

Overall, this architecture allows you to create a scalable and cost-effective serverless API that leverages the benefits of AWS services like API Gateway, Lambda, and DynamoDB.


##

The API Gateway acts as the entry point for the API. It has a single resource named "DynamoDBManager" and a single method "POST" associated with it. When a request is made to the API through an HTTPS endpoint, API Gateway invokes a Lambda function called "LambdaFunctionOverHttps".

The request payload sent to the API specifies the DynamoDB operation to be performed and provides the necessary data. For example, to create an item, the payload would look like this:

```json
{
    "operation": "create",
    "tableName": "lambda-apigateway",
    "payload": {
        "Item": {
            "id": "1",
            "name": "Bob"
        }
    }
}
```

To read an item, the payload would look like this:

```json
{
    "operation": "read",
    "tableName": "lambda-apigateway",
    "payload": {
        "Key": {
            "id": "1"
        }
    }
}
```

## Setup

### Create Lambda IAM Role

First, we need to create an IAM role that will be used by the Lambda function to access AWS resources. Follow these steps to create the role:

1. Open the IAM console and go to the Roles page.
2. Click on "Create role".
3. Select "Lambda" as the trusted entity.
4. Set the role name to **lambda-apigateway-role**.
5. Attach the following custom policy to the role, which provides necessary permissions for DynamoDB and CloudWatch Logs:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Stmt1428341300017",
            "Action": [
                "dynamodb:DeleteItem",
                "dynamodb:GetItem",
                "dynamodb:PutItem",
                "dynamodb:Query",
                "dynamodb:Scan",
                "dynamodb:UpdateItem"
            ],
            "Effect": "Allow",
            "Resource": "*"
        },
        {
            "Sid": "",
            "Resource": "*",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Effect": "Allow"
        }
    ]
}
```

### Create Lambda Function

Next, we need to create the Lambda function that will serve as the backend for our API. Follow these steps:

1. Go to the AWS Lambda console and click on "Create function".
2. Select "Author from scratch".
3. Provide a name for the function, such as **LambdaFunctionOverHttps**.
4. Choose "Python 3.7" as the runtime.
5. Under "Permissions", select "Use an existing role" and choose the **lambda-apigateway-role** that we created earlier.
6. Click on "Create function".

Now, replace the default code in the function editor with the following code:

```python
import boto3
import json

def lambda_handler(event, context):
    operation = event['operation']
    
    if 'tableName' in event:
        dynamo = boto3.resource('dynamodb').Table(event['tableName'])
    
    operations = {
        'create': lambda x: dynamo.put_item(**x),
        'read
