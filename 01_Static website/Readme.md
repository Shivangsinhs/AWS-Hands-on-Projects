# Deploy a Static Website on AWS

This guide provides step-by-step instructions for deploying a static website on AWS using Amazon S3 (Simple Storage Service) and Amazon CloudFront. Hosting a static website in the cloud offers simplicity, speed, and security, as it eliminates the need for server-side scripting languages and databases commonly used in dynamic websites.

## Prerequisites

Before you begin, make sure you have the following:

1. An Amazon Web Services (AWS) account.
2. Website files (HTML, CSS, JavaScript, images, etc.) ready to be hosted on AWS.
3. Optional: A domain name if you want to use a custom domain for your website.

## Architecture

The architecture for deploying a static website on AWS consists of the following components:

- **Amazon S3**: Serves as the storage service for hosting the static website files. It provides high scalability, reliability, and low-cost storage.

- **Amazon CloudFront**: Acts as a content delivery network (CDN) to distribute the website files globally. It improves the website's performance by caching content and delivering it from the nearest edge location to the end user.

![Untitled Diagram (1)](https://user-images.githubusercontent.com/116307753/236707632-c3516638-1150-4826-9007-f86e0588f303.jpg)


## Steps

Follow these steps to deploy your static website on AWS:

1. Create an S3 Bucket:
   - Log in to your AWS account and navigate to the S3 console.
   - Click on "Create bucket" and follow the instructions to create a new bucket.
   - Choose a unique name for your bucket and select the region closest to your target audience.
<img width="957" alt="1" src="https://user-images.githubusercontent.com/116307753/236711678-38fc03c0-cdc7-422d-949e-627c48134e4f.png">

2. Enable Static Website Hosting:
   - Select your newly created bucket and click on the "Properties" tab.
   - Click on "Static website hosting" and select "Use this bucket to host a website."
   - Enter the index document (e.g., index.html) and error document (e.g., error.html) names.
<img width="964" alt="4" src="https://user-images.githubusercontent.com/116307753/236711705-50341faa-8541-443d-964b-6f866a322c90.png">

3. Upload Website Files:
   - Select your bucket and click on the "Upload" button.
   - Upload your website files and set the correct permissions (e.g., public read) to make them accessible.

<img width="951" alt="5" src="https://user-images.githubusercontent.com/116307753/236711733-958c28b2-2791-4f96-a7e6-2dfd40fd1307.png">

4. Build ARN policy:

<img width="946" alt="7" src="https://user-images.githubusercontent.com/116307753/236711767-07dcb694-4638-44af-8e96-3e890c9bbfaa.png">

5. Enable CloudFront:
   - Go to the AWS Management Console and navigate to the CloudFront service.
   - Create a new CloudFront distribution, selecting your S3 bucket as the origin.
   - Configure other settings such as caching behavior, SSL/TLS certificates, and distribution settings.

6. Test Your Website:
<img width="962" alt="10" src="https://user-images.githubusercontent.com/116307753/236711829-2bde98c6-3106-4c2f-a8ed-3b3e6ff3b567.png">
   - Test your website in a browser to ensure everything is working correctly.
<img width="976" alt="11" src="https://user-images.githubusercontent.com/116307753/236711806-338b5b2e-9c32-4c7e-9d0c-b238aa52328e.png">

## Conclusion

Deploying a static website on AWS using S3 and CloudFront offers a cost-effective, scalable, and secure solution. The architecture leverages the storage capabilities of S3 and the global content delivery network provided by CloudFront. By following the steps outlined in this guide, you can quickly set up and host your static website on AWS. 
