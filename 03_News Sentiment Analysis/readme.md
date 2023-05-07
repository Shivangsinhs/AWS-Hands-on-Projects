# News Sentiment Analysis on AWS

This project aims to perform sentiment analysis on news articles using AWS services. The sentiment analysis will help determine the overall sentiment (positive, negative, or neutral) associated with news articles, enabling organizations to gain insights into public opinion and sentiment trends.

## Features

- **News Article Collection**: The project collects news articles from various sources using AWS Lambda, API Gateway, and Postman. It retrieves news articles based on specific keywords or categories to ensure a comprehensive dataset.

- **Sentiment Analysis**: The collected news articles undergo sentiment analysis using Amazon Comprehend, a natural language processing (NLP) service provided by AWS. Comprehend performs language detection, entity recognition, and sentiment analysis on the news articles to extract valuable sentiment-related insights.

- **Data Storage**: The project utilizes Amazon DynamoDB, a fully managed NoSQL database service, to store the collected news articles and their sentiment analysis results. DynamoDB provides a scalable and reliable storage solution for managing the data.

- **API Gateway**: API Gateway acts as the entry point for accessing the sentiment analysis functionality. It provides a RESTful API interface for integrating with external applications or services, allowing users to submit news articles for sentiment analysis.

## Architecture

The project follows a serverless architecture on AWS, leveraging the following services:

- **AWS Lambda**: It serves as the backend processing component, responsible for collecting news articles, triggering sentiment analysis, and storing the results in DynamoDB.

- **API Gateway**: It acts as a gateway for external systems or applications to interact with the sentiment analysis functionality. It exposes a RESTful API for submitting news articles and retrieving sentiment analysis results.

- **Amazon Comprehend**: It performs sentiment analysis on the news articles, providing sentiment scores and other NLP insights. Comprehend is integrated into the Lambda function for analyzing the textual content.

- **Amazon DynamoDB**: It stores the collected news articles, sentiment analysis results, and other relevant metadata. DynamoDB offers scalability, low-latency access, and automatic replication for high availability.


![Untitled Diagram](https://user-images.githubusercontent.com/116307753/236705702-f4fd4514-ae2c-41f5-b0ac-78b59317164b.jpg)
(Made from draw.io)

## Getting Started

To set up and run the News Sentiment Analysis project on AWS, follow these steps:

1. Clone the project repository to your local machine.

2. Set up an AWS account if you don't have one already.

3. Create an Amazon DynamoDB table to store the news articles and sentiment analysis results. Define the necessary attributes to store the required information.

4. Set up an AWS Lambda function that will be triggered by API Gateway or a scheduled event. Write the code to collect news articles, perform sentiment analysis using Amazon Comprehend, and store the results in DynamoDB.

5. Configure API Gateway to create a RESTful API endpoint for submitting news articles and retrieving sentiment analysis results. Define the necessary methods and integrate the API with the Lambda function.

6. Test the project functionality using Postman or any other REST client. Submit news articles to the API endpoint and verify the sentiment analysis results retrieved from DynamoDB.

7. Customize the project as per your requirements. You can enhance the sentiment analysis logic, add additional features, or integrate other AWS services as needed.

.

## Contact

For further information or inquiries, please contact Shivang Sinha at shivangsinha.aws@gmail.com
