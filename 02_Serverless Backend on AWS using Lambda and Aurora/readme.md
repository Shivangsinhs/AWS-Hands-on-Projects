# Serverless Backend on AWS using Lambda and Aurora

This repository provides an example implementation of a serverless backend using AWS Lambda and Amazon Aurora. It demonstrates how to build a scalable and cost-effective backend architecture that can handle various types of applications.

## Overview

The serverless backend architecture consists of the following components:

1. **AWS Lambda**: Lambda is a serverless compute service that allows you to run your code without provisioning or managing servers. In this architecture, Lambda functions handle the business logic and respond to incoming requests.

2. **Amazon Aurora**: Aurora is a fully managed relational database service provided by AWS. It offers the performance and availability of traditional enterprise databases with the simplicity and cost-effectiveness of open-source databases. Aurora serves as the backend data storage for the application.

3. **API Gateway**: API Gateway is a fully managed service that makes it easy to create, publish, and manage APIs at any scale. It acts as the entry point for incoming requests and triggers the appropriate Lambda function.

## Prerequisites

Before getting started, ensure that you have the following:

- An AWS account with the necessary permissions to create Lambda functions, Aurora database, and API Gateway resources.
- The AWS Command Line Interface (CLI) installed and configured on your local machine.
- Basic knowledge of AWS Lambda, Amazon Aurora, and API Gateway concepts.



### Step 1: Create an Aurora Relational Database

1. Go to the AWS Management Console.
2. Navigate to the Amazon RDS service.
3. Click on "Create database".
4. Select "Amazon Aurora" as the engine.
5. Make sure you select Serverless v1 and Data APi is enabled
6. Choose the desired configuration for your Aurora database, such as instance size and storage capacity.
7. Set up the security groups and provide a master username and password for the database.
8. Complete the creation process and wait for the database to become available.
![image](https://user-images.githubusercontent.com/116307753/236712944-8c8574e2-26f4-404a-8380-21a0078ac423.png)

### Step 2: Test the Database

![image](https://user-images.githubusercontent.com/116307753/236713075-81c7569d-f4cf-46e7-9bfa-b46d30dc4ced.png)

1. Click on Query editor. Connect to the database by choosing relevant instance.
2. Choose Database username to 'Add new database credientials'. Enter Database id and passwords.
![image](https://user-images.githubusercontent.com/116307753/236713465-6a0fabe5-2035-4cdd-b9f1-aa387cb126c0.png)
3. Now database is created.
4. Create the table by putting the values.

![image](https://user-images.githubusercontent.com/116307753/236713628-d1c81852-a579-4c38-b5f2-828326ffa853.png)

### Step 3: Configure the Lambda Function

1. Create the lambda function. 

![image](https://user-images.githubusercontent.com/116307753/236713782-1215530d-6883-4706-a3ef-76711cb322b6.png)


### Step 4: Test the Lambda Function

1. Before deploying the function, test it locally using the AWS SAM CLI or other local testing frameworks.
2. Invoke the Lambda function and validate its behavior.
3. Ensure that the function can successfully connect to the Aurora database and perform the expected operations.
![image](https://user-images.githubusercontent.com/116307753/236713966-e4c0dde0-98a3-4fd0-9711-0f520a4a4577.png)

### Step 6: Deploy the Lambda Function

1. Once you are satisfied with the testing, deploy the Lambda function to AWS.
2. Use the AWS Management Console, AWS CLI, or AWS SDKs to upload your function code and configure its settings.
3. Select the appropriate execution role, and set the function timeout and memory requirements based on your needs.


### Step 9: Check the Execution result

![image](https://user-images.githubusercontent.com/116307753/236714173-167ad799-bee3-4e57-97ad-3b37b23bafe5.png)



## Folder Structure

The repository has the following structure:

```
├── lambda_function.py       # Sample Lambda function code
├── README.md                # This README file
└── .gitignore               # Git ignore file
```

## References

For more information on AWS Lambda, Amazon Aurora, and API Gateway, refer to the following documentation:

- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda)
- [Amazon Aurora Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide)
- [API Gateway Documentation](https://docs.aws.amazon.com/apigateway)
